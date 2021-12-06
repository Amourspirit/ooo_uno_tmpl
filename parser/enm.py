#!/usr/bin/env python
import os
import sys
import argparse
from typing import Dict, List
from bs4.element import ResultSet, Tag
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw, RequireArgs, TypeCheckKw
from kwhelp import rules
from collections import namedtuple
from base import TagsStrObj, Util, WriteBase, ParserBase, SoupObj, UrlObj, BlockObj
from pathlib import Path
import textwrap
import xerox # requires xclip - sudo apt-get install xclip
from logger.log_handle import get_logger
from parser import __version__, JSON_ID
import pprint

logger = get_logger(Path(__file__).stem)

EnumDataItem = namedtuple(
    'EnumDataItem',
    ['name', 'value', 'desc']
)

class EnumUrl(UrlObj):
    """Gets Url data for enum"""
    def _get_ns(self) -> List[str]:
        # UrlObj strips off the last part of ns
        # because is is the component name in most cases.
        # enums do not have ther own page therefore no component name.
        result = []
        try:
            ns_part = self._page_link.split('.')[0].lower()
            s = ns_part.replace('_1_1', '.').lstrip('.')
            # the frist part on the str usually is prefixe with namespace, interface or whatever.
            # namespace always start with com so just drop the first part to clean it up.
            s = 'com.' + s.split('.', maxsplit=1)[1]
            result = s.split('.')
        except Exception as e:
            logger.error(e)
            logger.info('EnumUrl._get_ns() returning empty list.')
        return result

class EnumBlock(BlockObj):
    """
    Get Enum Block. The block contains all the details of the enum
    """
    def __init__(self, soup:SoupObj):
        super().__init__(soup=soup)
        self._obj_data = None
    
    def _get_url_obj(self):
        # override base class.
        return EnumUrl(self._url)
    
    def get_obj(self) -> Tag:
        """
        Gets enum block as Tag

        Raises:
            Exception: if unable to find at least 2 matches for search element
            Exception: If element is not found

        Returns:
            Tag: [description]
        """
        if self._obj_data:
            return self._obj_data
        _up_steps = 8
        _cls = 'el'
        links = self._soup.soup.find_all('a', class_=_cls, attrs={"href" : self._urlobj.page_link})
        if len(links) < 2:
            raise Exception(f"Second match ont found: Class: {_cls}, href: {self._urlobj.page_link}")
        link = links[1]
        if not link:
            raise Exception(f"Element not found: Class: {_cls}, href: {self._urlobj.page_link}")
        result = link
        for _ in range(_up_steps):
            result = result.parent
        self._obj_data = result
        return self._obj_data


class EnumName:
    """Class manages getting Name of Enum"""
    def __init__(self, block: EnumBlock):
        self._block = block
        self._cls = 'el'
        self._el = 'a'
    
    def get_data(self) -> str:
        """
        Gets Element Name

        Returns:
            str: Name such as ``BreakType``
        """
        _cls = self._cls
        _url = self._block.url
        self._urlobj = EnumUrl(url=_url)
        _block_obj = self._block.get_obj()
        text = _block_obj.find(self._el, class_=_cls, attrs={"href" : self._urlobj.page_link}).text
        return text.strip()



class EnumDesc:
    """Gets Enum Description"""
    def __init__(self, block: EnumBlock):
        self._block = block
        self._cls = 'memdoc'
        self._el = 'div'

    def get_data(self) -> str:
        _block_obj = self._block.get_obj()
        tag = _block_obj.find(self._el, class_=self._cls)
        lines_found: ResultSet = tag.select(f'{self._el}.{self._cls} > p')
        p_obj = TagsStrObj(tags=lines_found)
        desc = p_obj.get_data()
        if not desc:
            e_obj = EnumName(block=self._block)
            e_name = e_obj.get_data()
            desc = "ENUM " + e_name
        return desc

class EnumItemsBlock:
    """
    Get Enum ItemsBlock. The block contains details of each enum
    """
    def __init__(self, block: EnumBlock):
        self._block = block
        self._cls = 'fieldtable'
        self._el = 'table'
    
    def get_obj(self) -> Tag:
        _block_obj = self._block.get_obj()
        return _block_obj.find(self._el, class_=self._cls)


class EnumItems:
    def __init__(self, block: EnumBlock, sort: bool = True):
        self._enum_block = EnumItemsBlock(block=block)
        self._sort = sort
    
    def get_data(self) -> List[EnumDataItem]:
        tag = self._enum_block.get_obj()
        # body > div.contents > div:nth-child(11) > div.memdoc > table > tbody > tr
        rows = tag.select('tr')
        # the first row is a header with a td that has a comlum span
        result = []
        for row in rows:
            if not self._is_valid_row(row=row): continue
            di = self._process_row(row=row)
            result.append(di)
        if self._sort:
            result.sort()
        return result

    def _is_valid_row(self, row: Tag) -> bool:
        tag = row.find('td', class_='fieldname')
        return not tag is None

    def _process_row(self, row: Tag) -> EnumDataItem:
        tag = row.find('td', class_='fieldname')
        name:str = tag.text.strip()
        p_lines = row.select('td.fielddoc > p')
        t_obj = TagsStrObj(tags=p_lines)
        di = EnumDataItem(name=name,
                          value=name,
                          desc=t_obj.get_lines())
        return di

class ParserEnum(ParserBase):
    # region init
    @RequireArgs('url', ftype=DecFuncEnum.METHOD)
    @RuleCheckAllKw(arg_info={"url": 0, "sort": 1, "replace_dual_colon": 1},
                    rules=[rules.RuleStrNotNullEmptyWs, rules.RuleBool],
                    ftype=DecFuncEnum.METHOD)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._data = None
        self._data_formated = None
        self._soup = SoupObj(url=self._url)
        self._block = None
        self._data_formated = None
        self._data_items = None

    def _get_enum_block(self) -> EnumBlock:
        if not self._block:
            self._block = EnumBlock(soup=self._soup)
        return self._block

    # region Data
    def get_dict_data(self) -> dict:
        info = self.get_info()
        items = self._get_data_items()
        # set to list for json
        info['items'] = items
        return info
    # endregion Data

    def get_info(self) -> Dict[str, object]:
        """
        Gets Enum Info

        Returns:
            Dict[str, object]:
            {
                "name": "name of enum",
                "desc": "Description of enum",
                "url": "Url of Enum",
                "ns": "Namesapce of Enum"
            }
        """
        try:
            block = self._get_enum_block()
            n_obj = EnumName(block=block)
            d_obj = EnumDesc(block=block)
            name = n_obj.get_data()
            desc = d_obj.get_data()
            result = {
                "name": name,
                "desc": desc,
                "url": self._url,
                'ns': self._block.url_obj.namespace_str
            }
            return result
        except Exception as e:
            logger.error(e)
            raise e
    
    def get_parser_args(self) -> dict:
        args = {
            "sort": self._sort
        }
        return args

    def get_formated_data(self):
        if not self._data_formated is None:
            return self._data_formated
        try:
            block = self._get_enum_block()
            e_obj = EnumItems(block=block, sort=self._sort)
            enums = e_obj.get_data()
            s = ''
            lst_indent = self._indent * 2
            for i, e in enumerate(enums):
                if i > 0:
                    s += ',\n'
                s_desc = textwrap.indent(Util.get_string_list(e.desc), lst_indent).lstrip()

                s += f'{self._indent}"{e.name}": {s_desc}'
            self._data_formated = s
        except Exception as e:
            logger.error(e)
        return self._data_formated
    
    def _get_data_items(self) -> List[dict]:
        if not self._data_items is None:
            return self._data_items
        result = []
        try:
            block = self._get_enum_block()
            e_obj = EnumItems(block=block, sort=self._sort)
            enums = e_obj.get_data()
            for e in enums:
                result.append(
                    {
                        "name": e.name,
                        "value": e.value,
                        "desc": e.desc
                    }
                )
        except Exception as e:
            logger.error(e)
            raise e
        self._data_items = result
        return self._data_items
class EnumWriter(WriteBase):
    # region constructor
    @TypeCheckKw(arg_info={
        "copy_clipboard": 0,
        "write_template": 0,
        "print_template": 0,
        "print_json": 0,
        "write_json": 0
    },
        types=[bool],
        ftype=DecFuncEnum.METHOD)
    def __init__(self, parser: ParserEnum, **kwargs):
        super().__init__(**kwargs)
        self._parser = parser
        self._copy_clipboard = kwargs.get('copy_clipboard', False)
        self._sort = kwargs.get('sort', True)
        self._print_template = kwargs.get('print_template', True)
        self._write_file = kwargs.get('write_template', False)
        self._print_json = kwargs.get('print_json', True)
        self._write_json = kwargs.get('write_json', False)
        self._indent_amt = 4
        self._json_str = None
        self._file_full_path = None
        self._p_name = None
        self._p_namespace = None
        self._p_url = None
        self._p_desc = None
        self._p_data = None
        self._path_dir = Path(os.path.dirname(__file__))
        _path = Path(self._path_dir, 'template', 'enum.tmpl')
        if not _path.exists():
            raise FileNotFoundError(f"unable to find templae file '{_path}'")
        self._template_file = _path
        self._template: str = self._get_template()
    # enregion constructor

    def _get_template(self):
        with open(self._template_file) as f:
            contents = f.read()
        return contents

    def write(self):
        self._set_info()
        self._set_template_data()
        logger.info("Processing %s.%s", self._p_namespace, self._p_name)
        try:
            if self._copy_clipboard:
                xerox.copy(self._template)
                logger.debug('copied to clipbord')
            if self._print_template or self._print_json:
                logger.debug('Printing to terminal')
                os.system('cls' if os.name == 'nt' else 'clear')
            if self._print_template:
                print(self._template)
            if self._print_json:
                print(self._get_json())
            if self._write_file:
                self._write_to_file()
            if self._write_json:
                self._write_to_json()
        except Exception as e:
            logger.exception(e)

    def _get_json(self) -> str:
        if not self._json_str is None:
            return self._json_str
        p_dict = self._parser.get_dict_data()
        json_dict = {
            "id": JSON_ID,
            "version": __version__,
            "name": p_dict['name'],
            "type": "enum",
            "namespace": p_dict['ns'],
            "parser_args": self._parser.get_parser_args(),
            "writer_args": {},
            "data": p_dict
        }
        str_jsn = Util.get_formated_dict_list_str(obj=json_dict, indent=2)
        self._json_str = str_jsn
        return self._json_str

    def _write_to_file(self):
        with open(self._file_full_path, 'w') as f:
            f.write(self._template)
        logger.info("Created file: %s", self._file_full_path)
    
    def _write_to_json(self):
        p = self._file_full_path.parent
        jsn_p = p / (str(self._file_full_path.stem) + '.json')
        jsn_str = self._get_json()
        with open(jsn_p, 'w') as f:
            f.write(jsn_str)
        logger.info("Created file: %s", jsn_p)

    def _set_template_data(self):
        self._template = self._template.replace('{sort}', str(self._sort))
        self._template = self._template.replace('{ns}', str(self._p_namespace))
        self._template = self._template.replace('{name}', self._p_name)
        self._template = self._template.replace('{link}', self._p_url)
        indent = ' ' * self._indent_amt
        # self._template = self._template.replace('{desc}', self._p_desc)
        indented = textwrap.indent(self._p_desc, indent).lstrip()
        self._template = self._template.replace('{desc}', indented)
        # indented = textwrap.indent(self._p_data, indent)
        # self._template = self._template.replace('{data}', indented)
        self._template = self._template.replace('{data}', self._p_data)

    def _set_info(self):
        data = self._parser.get_info()
        self._p_name = data['name']
        self._p_desc = data['desc']
        self._p_url = data['url']
        self._p_namespace = data['ns']
        self._p_data = self._parser.get_formated_data()
        if self._write_file or self._write_json:
            self._file_full_path = self._get_uno_obj_path()
        

    def _get_uno_obj_path(self) -> Path:
        if not self._p_name:
            try:
                raise Exception(
                    "EnumWriter._get_uno_obj_path() Parser provided a name the is an empty string.")
            except Exception as e:
                logger.error(e)
                raise e
        uno_obj_path = Path(self._path_dir.parent, 'uno_obj')
        name_parts:List[str] = self._p_namespace.split('.')
        # ignore com, sun, star
        path_parts = name_parts[3:]
        path_parts.append(self._p_name + '.tmpl')
        obj_path = uno_obj_path.joinpath(*path_parts)
        self._mkdirp(obj_path.parent)
        return obj_path


def _main():
    url = 'https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1uno.html#a00683ed3ec24b47c36ead10a20d6f328'

    p = ParserEnum(
        url=url)
    w = EnumWriter(
        parser=p,
        print=True,
        write_file=False)
    w.write()
    
    # t = TagsStrObj(tags=["ones", "twos", "Three", "four"], indent=8)
    # print(t.get_string_list())
def main():
    logger.info('Executing command: %s', sys.argv[1:])
    parser = argparse.ArgumentParser(description='enum')
    parser.add_argument(
        '-u', '--url',
        help='Source Url',
        type=str,
        required=True)
    parser.add_argument(
        '-s', '--no-sort',
        help='No sorting of results',
        action='store_false',
        dest='sort',
        default=True)
    parser.add_argument(
        '-d', '--no-dual',
        help='Do NOT replace :: with .',
        action='store_false',
        dest='dual_colon',
        default=True)
    parser.add_argument(
        '-c', '--clipboard',
        help='Copy to clipboard',
        action='store_true',
        dest='clipboard',
        default=False)
    parser.add_argument(
        '-n', '--print-json',
        help='Print json to terminal',
        action='store_true',
        dest='print_json',
        default=False)
    parser.add_argument(
        '-m', '--print-template',
        help='Print template to terminal',
        action='store_true',
        dest='print_template',
        default=False)
    parser.add_argument(
        '-t', '--write-template',
        help='Write template file into obj_uno subfolder',
        action='store_true',
        dest='write_template',
        default=False)
    parser.add_argument(
        '-j', '--write-json',
        help='Write json file into obj_uno subfolder',
        action='store_true',
        dest='write_json',
        default=False)

    args = parser.parse_args()
    logger.info('Parsing Url %s' % args.url)
    p = ParserEnum(
        url=args.url, sort=args.sort,
        replace_dual_colon=args.dual_colon)
    w = EnumWriter(
        parser=p,
        print_template=args.print_template,
        print_json=args.print_json,
        copy_clipboard=args.clipboard,
        write_template=args.write_template,
        write_json=args.write_json
        )
    if args.print_template is False and args.print_json is False:
        print('')
    w.write()

if __name__ == '__main__':
    main()
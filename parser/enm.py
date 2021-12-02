#!/usr/bin/env python
import os
import argparse
from typing import Dict, List
from bs4.element import ResultSet, Tag
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw, RequireArgs
from kwhelp import rules
from collections import namedtuple
from base import TagsStrObj, WriteBase, ParserBase, SoupObj, UrlObj, BlockObj
from pathlib import Path
import textwrap
import xerox # requires xclip - sudo apt-get install xclip

EnumDataItem = namedtuple(
    'EnumDataItem',
    ['name', 'value', 'desc']
)

class EnumBlock(BlockObj):
    """
    Get Enum Block. The block contains all the details of the enum
    """
    def __init__(self, soup:SoupObj):
        super().__init__(soup=soup)
        self._obj_data = None
    
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
        self._urlobj = UrlObj(url=_url)
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
                          desc=t_obj.get_string_list())
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

    def _get_enum_block(self) -> EnumBlock:
        if not self._block:
            self._block = EnumBlock(soup=self._soup)
        return self._block

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

    def get_formated_data(self):
        block = self._get_enum_block()
        e_obj = EnumItems(block=block, sort=self._sort)
        enums = e_obj.get_data()
        s = ''
        lst_indent = self._indent * 2
        for i, e in enumerate(enums):
            if i > 0:
                s += ',\n'
            s_desc = textwrap.indent(e.desc, lst_indent).lstrip()

            s += f'{self._indent}"{e.name}": {s_desc}'
        return s

class EnumWriter(WriteBase):
    
    def __init__(self, parser: ParserEnum, **kwargs):
        self._parser = parser
        self._copy_clipboard = kwargs.get('copy_clipboard', False)
        self._sort = kwargs.get('sort', True)
        self._print = kwargs.get('print', True)
        self._indent_amt = 4
        self._write_file = kwargs.get('write_file', False)
        self._file_full_path = None
        self._p_name = None
        self._p_namespace = None
        self._p_url = None
        self._p_desc = None
        self._path_dir = Path(os.path.dirname(__file__))
        _path = Path(self._path_dir, 'template', 'enum.tmpl')
        if not _path.exists():
            raise FileNotFoundError(f"unable to find templae file '{_path}'")
        self._template_file = _path
        self._template: str = self._get_template()
    
    def _get_template(self):
        with open(self._template_file) as f:
            contents = f.read()
        return contents

    def write(self):
        self._set_info()
        self._set_template_data()
        if self._copy_clipboard:
            xerox.copy(self._template)
        if self._print:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self._template)
        if self._write_file:
            self._write_to_file()

    def _write_to_file(self):
        with open(self._file_full_path, 'w') as f:
            f.write(self._template)

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
        if self._write_file:
            self._file_full_path = self._get_uno_obj_path()
        

    def _get_uno_obj_path(self) -> Path:
        uno_obj_path = Path(self._path_dir.parent, 'uno_obj')
        name_parts:List[str] = self._p_namespace.split('.')
        # ignore com, sun, star
        path_parts = name_parts[3:]
        path_parts.append(self._p_name + '.tmpl')
        obj_path = uno_obj_path.joinpath(*path_parts)
        self._mkdirp(obj_path.parent)
        return obj_path


def _main():
    p = ParserEnum(url='https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1style.html#a3ae28cb49c180ec160a0984600b2b925')
    w = EnumWriter(parser=p)
    w._set_info()
    _path = w._get_uno_obj_path()
    print(_path)
    
    # t = TagsStrObj(tags=["ones", "twos", "Three", "four"], indent=8)
    # print(t.get_string_list())
def main():
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
        '-p', '--no-print',
        help='Do NOT print to terminal',
        action='store_false',
        dest='print',
        default=True)
    parser.add_argument(
        '-w', '--write',
        help='Write file into obj_uno subfolder',
        action='store_true',
        dest='write',
        default=False)

    args = parser.parse_args()
    
    p = ParserEnum(
        url=args.url, sort=args.sort,
        replace_dual_colon=args.dual_colon)
    w = EnumWriter(
        parser=p,
        print=args.print,
        copy_clipboard=args.clipboard,
        sort=args.sort,
        write_file=args.write)
    print('')
    w.write()

if __name__ == '__main__':
    main()
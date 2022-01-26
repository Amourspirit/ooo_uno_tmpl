#!/usr/bin/env python
# coding: utf-8
"""
Process a link to a page that contains enums
"""
from dataclasses import dataclass, field
import enum
import os
import sys
import logging
import argparse
from typing import Dict, List, Union
from bs4.element import ResultSet, Tag
from kwhelp.decorator import DecFuncEnum, TypeCheckKw
from collections import namedtuple
from pathlib import Path
import xerox # requires xclip - sudo apt-get install xclip
try:
    import base
except ModuleNotFoundError:
    import parser.base as base
from logger.log_handle import get_logger
from parser import __version__, JSON_ID

logger = None

def _set_loggers(l: Union[logging.Logger, None]):
    global logger, base
    logger = l
    base.logger = l


_set_loggers(None)


@dataclass
class EnumDataItem:
    name: str
    value: str
    desc: List[str] = field(default_factory=list)

    def __lt__(self, other: object):
        if not isinstance(other, EnumDataItem):
            return NotImplemented
        return self.name < other.name

class EnumUrl(base.UrlObj):
    """Gets Url data for enum"""

    def get_split_ns(self) -> List[str]:
        # UrlObj strips off the last part of ns
        # because is is the component name in most cases.
        # enums do not have ther own page therefore no component name.
        result = []
        try:
            ns_part = self._page_link.split('.')[0].lower()
            s = ns_part.replace(base.URL_SPLIT, '.').lstrip('.')
            
            # in some cases such as generics the name can have _3_01 and or _01_4 in the last part of the name
            # best guess _3 is < and _4 is > and _01 is space.
            # just split _3 dropping the end
            s = s.rsplit(sep='_3', maxsplit=1)[0]
            # the frist part on the str usually is prefixe with namespace, interface or whatever.
            # namespace always start with com so just drop the first part to clean it up.
            s = 'com.' + s.split('.', maxsplit=1)[1]
            result = s.split('.')
        except Exception as e:
            logger.error(e, exc_info=True)
            logger.info('EnumUrl._get_ns() returning empty list.')
        return result


class EnumBlock(base.BlockObj):
    """
    Get Enum Block. The block contains all the details of the enum
    """

    def __init__(self, soup: base.SoupObj):
        super().__init__(soup=soup)
        self._obj_data = False
    
    def _get_url_obj(self):
        # override base class.
        return EnumUrl(self._url)

    def _is_valid_block(self, tag: Tag) -> bool:
        # it is possible not to find the correct block using url when there are typedef
        # such as https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#af3965fa427851bc02bfe32c5d95d7406
        # for additional validation look for table
        if not tag:
            return False
        tbl = tag.find('table', class_='fieldtable')
        return not tbl is None
    
    def get_obj(self) -> Tag:
        """
        Gets enum block as Tag

        Raises:
            Exception: if unable to find at least 2 matches for search element
            Exception: If element is not found

        Returns:
            Tag: [description]
        """
        if not self._obj_data is False:
            return self._obj_data
        self._obj_data = None
        try:
            _cls = 'el'
            links = self._soup.soup.find_all('a', class_=_cls, attrs={"href" : self._urlobj.page_link})
            for link in links:
                # if len(links) < 2:
                #     raise Exception(f"Second match ont found: Class: {_cls}, href: {self._urlobj.page_link}")
                # link = links[1]
                if not link:
                    raise Exception(f"Element not found: Class: {_cls}, href: {self._urlobj.page_link}")
                result:Tag = link
                class_ = result.get('class', [])
                class_name = "" if len(class_) == 0 else class_[0].lower()
                too_far = False
                while class_name != 'memitem':
                    result = result.parent
                    if not result:
                        break
                    class_ = result.get('class', [])
                    class_name = "" if len(class_) == 0 else class_[0].lower()
                    if class_name == 'contents':
                        too_far = True
                        break
                if too_far:
                    continue
                # for _ in range(_up_steps):
                #     result = result.parent
                try:
                    class_ = result.get('class', [])
                    class_name = "" if len(class_) == 0 else class_[0].lower()
                    if class_name == 'memitem':
                        if not self._is_valid_block(result):
                            continue
                        self._obj_data = result
                        break
                except Exception:
                    continue
        except Exception as e:
            url = self.url_obj.url
            logger.error(
                "EnumBlock.get_obj() Error parsing Link: '%s' Error: %s", url, str(e))
            raise e
        if self._obj_data is None:
            msg = f"EnumBlock.get_obj() Error parsing Link: {self.url_obj.url}"
            logger.error(msg)
            raise Exception(msg)
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
        text = _block_obj.find(self._el, class_=_cls, attrs={"href" : self._urlobj.page_link}).text.replace("::",'.')
        text = base.Util.get_clean_ns(input=text,ltrim=True)
        text = base.Util.get_last_part(input=text)
        return text



class EnumDesc:
    """Gets Enum Description"""
    def __init__(self, block: EnumBlock):
        self._block = block
        self._cls = 'memdoc'
        self._el = 'div'
        self._data = None

    def get_data(self) -> str:
        if not self._data is None:
            return self._data
        self._data = ''
        try:
            _block_obj = self._block.get_obj()
            tag = _block_obj.find(self._el, class_=self._cls)
            lines_found: ResultSet = tag.select(f'{self._el}.{self._cls} > p')
            p_obj = base.TagsStrObj(tags=lines_found)
            desc = p_obj.get_data()
            if not desc:
                e_obj = EnumName(block=self._block)
                e_name = e_obj.get_data()
                desc = "ENUM " + e_name
                self._data = desc
        except Exception as e:
            msg = f"EnumDesc: An error as occured processing link: {self._block.url_obj.url}. Error {e}"
            logger.error(msg)
            raise e
        return self._data

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
        self._block = block
        self._enum_block = EnumItemsBlock(block=self._block)
        self._sort = sort
    
    def get_data(self) -> List[EnumDataItem]:
        tag = self._enum_block.get_obj()
        # body > div.contents > div:nth-child(11) > div.memdoc > table > tbody > tr
        rows = None
        try:
            if not rows:
                rows = tag.select('tr')
            # body > div.contents > div:nth-child(110) > div.memdoc > table
            # the first row is a header with a td that has a comlum span
            result = []
            for row in rows:
                if not self._is_valid_row(row=row): continue
                di = self._process_row(row=row)
                result.append(di)
            if self._sort:
                result.sort()
        except Exception as e:
            msg = f"EnumItems.get_data() error processing '{self._block.url_obj.url}' Error: {e}"
            logger.error(msg)
            raise e
        return result

    def _is_valid_row(self, row: Tag) -> bool:
        tag = row.find('td', class_='fieldname')
        return not tag is None

    def _process_row(self, row: Tag) -> EnumDataItem:
        tag = row.find('td', class_='fieldname')
        name:str = tag.text.strip()
        p_lines = row.select('td.fielddoc > p')
        t_obj = base.TagsStrObj(tags=p_lines)
        di = EnumDataItem(
            name=name,
            value=name,
            desc=t_obj.get_lines())
        return di


class ParserEnum(base.ParserBase):
    # region init
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._data = None
        self._data_formated = None
        self._soup = base.SoupObj(url=self.url, allow_cache=self.allow_cache)
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
                "namespace": "Namesapce of Enum"
            }
        """
        try:
            block = self._get_enum_block()
            n_obj = EnumName(block=block)
            d_obj = EnumDesc(block=block)
            name = n_obj.get_data()
            desc = d_obj.get_data()
            ns = base.UrlObj(self.url,has_name=False)
            result = {
                "name": name,
                "desc": desc,
                "url": self._url,
                # 'ns': self._block.url_obj.namespace_str
                'namespace': ns.namespace_str
            }
            return result
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
    
    def get_parser_args(self) -> dict:
        args = {
            "sort": self.sort
        }
        return args

    def get_formated_data(self):
        if not self._data_formated is None:
            return self._data_formated
        result = {}
        di: List[dict] = self._get_data_items()
        for itm in di:
            result[itm['name']] = itm['desc']
        s = base.Util.get_formated_dict_list_str(result)
        self._data_formated =s
        return self._data_formated
    
    def _get_data_items(self) -> List[dict]:
        if not self._data_items is None:
            return self._data_items
        result = []
        try:
            block = self._get_enum_block()
            e_obj = EnumItems(block=block, sort=self.sort)
            enums: List[EnumDataItem] = e_obj.get_data()
            # sort for consistency in json
            # enum.sort()
            for e in enums:
                result.append(
                    {
                        "name": e.name,
                        "value": e.value,
                        "desc": e.desc
                    }
                )
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        self._data_items = result
        return self._data_items


class EnumWriter(base.WriteBase):
    # region constructor
    @TypeCheckKw(arg_info={
        "copy_clipboard": 0,
        "write_template": 0,
        "print_template": 0,
        "print_json": 0,
        "write_json": 0,
        "write_template_long": 0
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
        self._print_json = kwargs.get('print_json', False)
        self._write_json = kwargs.get('write_json', False)
        self._include_desc: bool = kwargs.get('include_desc', True)
        self._json_out: bool = kwargs.get('json_out', True)
        self._allow_db = kwargs.get('allow_db', True)
        self._write_template_long: bool = kwargs.get(
            'write_template_long', False)
        self._write_path: Union[str, None] = kwargs.get('write_path', None)
        self._indent_amt = 4
        self._cache = {}
        self._json_str = None
        self._file_full_path = None
        self._p_name = None
        self._p_namespace = None
        self._p_url = None
        self._p_desc = None
        self._p_data = None
        self._path_dir = Path(os.path.dirname(__file__))
        t_file = 'enum'
        if not self._write_template_long:
            t_file += '_stub'
        t_file += '.tmpl'
        _path = Path(self._path_dir, 'template', t_file)
        if not _path.exists():
            raise FileNotFoundError(f"unable to find templae file '{_path}'")
        self._template_file = _path
        self._template: str = self._get_template()
    # endregion constructor

    def _get_template(self):
        with open(self._template_file) as f:
            contents = f.read()
        return contents

    def write(self) -> Union[str, None]:
        """
        Writes files/templates according to parameters

        Returns:
            Union[str, None]: Returns json string if ``json_out`` is ``True``
        """
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
            if self._json_out:
                return self._get_json()
        except Exception as e:
            logger.exception(e)

    def _get_json(self) -> str:
        if not self._json_str is None:
            return self._json_str
        p_dict = {
            "name": 'place holder',
            "namespace": 'place holder',
            "url": 'place holder',
            "allow_db": self._allow_db,
            "quote": [],
            "typings": []
        }
        p_dict.update(self._parser.get_dict_data())
        json_dict = {
            "id": JSON_ID,
            "version": __version__,
            # "timestamp": str(base.Util.get_timestamp_utc()),
            "libre_office_ver": base.APP_CONFIG.libre_office_ver,
            "name": p_dict['name'],
            "type": "enum",
            "namespace": p_dict['namespace'],
            "parser_args": self._parser.get_parser_args(),
            "writer_args": {
                "include_desc": self._include_desc
                },
            "data": p_dict
        }
        str_jsn = base.Util.get_formated_dict_list_str(obj=json_dict, indent=2)
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
        if self._write_template_long is False:
            return
        self._template = self._template.replace(
            '{libre_office_ver}', base.APP_CONFIG.libre_office_ver)
        self._template = self._template.replace('{sort}', str(self._sort))
        self._template = self._template.replace(
            '{allow_db}', str(self._allow_db))
        self._template = self._template.replace('{ns}', str(self._p_namespace))
        self._template = self._template.replace('{name}', self._p_name)
        self._template = self._template.replace('{link}', self._p_url)
        str_json_desc = base.Util.get_formated_dict_list_str(self._p_desc)
        self._template = self._template.replace('{quote}', 'set()')
        self._template = self._template.replace('{typings}','set()')
        self._template = self._template.replace('{desc}', str_json_desc)
        self._template = self._template.replace('{data}', self._p_data)

    def _set_info(self):
        data = self._parser.get_info()
        self._p_name = data['name']
        self._p_desc = data['desc']
        self._p_url = data['url']
        self._p_namespace = data['namespace']
        self._p_data = self._parser.get_formated_data()
        if self._write_file or self._write_json:
            self._file_full_path = self._get_uno_obj_path()
        

    def _get_uno_obj_path(self) -> Path:
        key = '_get_uno_obj_path'
        if key in self._cache:
            return self._cache[key]
        if not self._p_name:
            try:
                raise Exception(
                    "EnumWriter._get_uno_obj_path() Parser provided a name the is an empty string.")
            except Exception as e:
                logger.error(e, exc_info=True)
                raise e
        if self._write_path:
            write_path = self._write_path
        else:
            write_path = base.APP_CONFIG.uno_base_dir
        uno_obj_path = Path(self._path_dir.parent, write_path)
        name_parts:List[str] = self._p_namespace.split('.')
        # ignore com, sun, star
        path_parts = name_parts[3:]
        path_parts.append(self._p_name + base.APP_CONFIG.template_enum_ext)
        obj_path = uno_obj_path.joinpath(*path_parts)
        self._mkdirp(obj_path.parent)
        self._cache[key] = obj_path
        return self._cache[key]

# region Parse method
def get_kwargs_from_args(args: argparse.ArgumentParser) -> dict:
    """
    Converts argparse args into dictionary that can be passed to ``parse()``

    Args:
        args (argparse.ArgumentParser): args

    Returns:
        dict: dictionary that contain key values matching ``parser()`` args.
    """
    d = {
        "url": args.url,
        "sort": args.sort,
        "cache": args.cache,
        "copy_clipboard": args.clipboard,
        "print_template": args.print_template,
        "write_template": args.write_template,
        "write_template_long": args.long_format,
        "print_json": args.print_json,
        "write_json": args.write_json,
        "include_desc": args.desc,
        "log_file": args.log_file,
        "verbose": args.verbose
    }
    if args.write_path:
        d['write_path'] = args.write_path
    return d

def parse(**kwargs) -> Union[str, None]:
    """
    Parses data, alternative to running on command line.

    Keyword Arguments:
        url (str): url to parse
        sort (str, optional): Sorting of results. Default ``True``
        cache (str, optional): Caching. Default ``True``
        include_desc (str, optional): Description will be outputed in template. Default ``True``
        json_out (bool, optional): returns json to caller if ``True``. Default ``False``
        long_template (str, optional): Writes a long format template.
            Requires write_template is set. Default ``False``
        clipboard (str, optional): Copy to clipboard. Default ``False``
        print_json (str, optional): Print json to termainl. Default ``False``
        print_template (str, optional): Print template to terminal. Default ``False``
        write_template (str, optional): Write template file into obj_uno subfolder. Default ``False``
        write_json (str, optional): Write json file into obj_uno subfolder. Default ``False``
        write_path (str, optional): The root path to write data files (json, tmpl) into. Defaut set in config ``uno_base_dir``
        verbose (str, optional): Verobose output.
        log_file (str, optional): Log File
    
    Returns:
        Union[str, None]: Returns json string if json_out is ``True``
    """
    global logger
    _url = str(kwargs['url'])
    _sort = bool(kwargs.get('sort', True))
    _cache = bool(kwargs.get('cache', True))
    _clipboard = bool(kwargs.get('copy_clipboard', False))
    _print_template = bool(kwargs.get('print_template', False))
    _write_template = bool(kwargs.get('write_template', False))
    _long_template = bool(kwargs.get('write_template_long', False))
    _print_json = bool(kwargs.get('print_json', False))
    _write_json = bool(kwargs.get('write_json', bool))
    _include_desc = bool(kwargs.get('include_desc', True))
    _log_file = kwargs.get('log_file', None)
    _verbose = bool(kwargs.get('verbose', False))
    _json_out = bool(kwargs.get('json_out', False))
    _write_path= kwargs.get('write_path', None)

    if logger is None:
        log_args = {}
        if _log_file:
            log_args['log_file'] = _log_file
        else:
            log_args['log_file'] = 'enum.log'
        if _verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))


    p = ParserEnum(
        url=_url,
        sort=_sort,
        replace_dual_colon=True,
        cache=_cache
    )
    w = EnumWriter(
        parser=p,
        print_template=_print_template,
        print_json=_print_json,
        copy_clipboard=_clipboard,
        write_template=_write_template,
        write_json=_write_json,
        write_template_long=_long_template,
        include_desc=_include_desc,
        json_out=_json_out,
        write_path=_write_path
    )
    return w.write()
# endregion Parse method


def _main():
    # url = 'https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt.html#aa6b9d577a1700f29923f49f7b77d165f'
    # url = 'https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart2.html#aa17c0b28cca2adc2be9b3c5954111489'
    url = 'https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt.html#ad249d76933bdf54c35f4eaf51a5b7965'
    kwargs = {
        "url": url,
        "log_file": "debug.log",
        'verbose': True,
        "write_json": True
    }
    parse(**kwargs)
    # sys.argv.extend(['--log-file', 'debug.log', '-v', '-n', '-u', url])
    # main()

# region Parser


def set_cmd_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-u', '--url',
        help='Source Url',
        type=str,
        required=True)
    parser.add_argument(
        '-o', '--out',
        help=f"Out path of templates and json data. Default: '{base.APP_CONFIG.uno_base_dir}'",
        type=str,
        dest='write_path',
        default=None,
        required=False)
    parser.add_argument(
        '-x', '--no-cache',
        help='No caching',
        action='store_false',
        dest='cache',
        default=True)
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
        '-g', '--long-template',
        help='Writes a long format template. Requires --write-template is set. No Autoload',
        action='store_true',
        dest='long_format',
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

def set_cmd_args_local(parser) -> None:
    parser.add_argument(
        '-v', '--verbose',
        help='verbose logging',
        action='store_true',
        dest='verbose',
        default=False)
    parser.add_argument(
        '-L', '--log-file',
        help='Log file to use. Defaults to enum.log',
        type=str,
        required=False)

# endregion Parser

def main():
    global logger

    parser = argparse.ArgumentParser(description='enum')
    set_cmd_args(parser)
    set_cmd_args_local(parser)
    args = parser.parse_args()

    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        else:
            log_args['log_file'] = 'enum.log'
        if args.verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))

    if not args.no_print_clear:
        os.system('cls' if os.name == 'nt' else 'clear')

    logger.info('Executing command: %s', sys.argv[1:])
    logger.info('Parsing Url %s' % args.url)
    args_dict = get_kwargs_from_args(args)

    if args.print_template is False and args.print_json is False:
        print('')
    parse(**args_dict)

if __name__ == '__main__':
    main()
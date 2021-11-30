#!/usr/bin/env python
import os
import argparse
from typing import Dict, List, Union
from bs4 import BeautifulSoup
from bs4.element import ResultSet, SoupStrainer, Tag
import requests
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw, TypeCheckKw
from kwhelp import rules
from collections import namedtuple
from base import WriteBase
from pathlib import Path
import textwrap
# import pyperclip as pc
dataitem = namedtuple(
    'dataitem', ['value', 'raw_value', 'name', 'datatype', 'lines'])


    


class Parser:
    
    # region init
    @RuleCheckAllKw(arg_info={"url": 0, "sort": 1, "replace_dual_colon": 1},
                    rules=[rules.RuleStrNotNullEmptyWs, rules.RuleBool],
                    ftype=DecFuncEnum.METHOD)
    def __init__(self, **kwargs):
        self._indent = '    '
        self._url = kwargs.get('url', '')
        self._raw = ''
        self._sort = kwargs.get('sort', True)
        self._replace_dual_colon = kwargs.get('replace_dual_colon', True)
        self._title_full = None

    # endregion init

    # region request
    def get_request_text(self, url: str) -> str:
        response = requests.get(url=url)
        if response.status_code != 200:
            raise Exception('bad response code:' + str(response.status_code))
        html_text = response.text
        return html_text
    # endregion request

    # region Info
    def get_info(self) -> Dict[str, str]:
        """
        Gets info

        Returns:
            Dict[str, str]: {
                "name": "name of constant",
                "desc": "description of constant",
                "url": "Url to LibreOffice of constant"
            }
        """
        if not self._url:
            raise ValueError('URL is not set')
        soup = BeautifulSoup(self.get_raw_html(), 'lxml')
        name = self._get_name(soup=soup)
        desc = self._get_desc(soup=soup)
        info = {
            "name": name,
            "desc": desc,
            "url": self.url
        }
        return info
    
    def _get_desc(self, soup: BeautifulSoup):
        contents = soup.find('div', class_='contents')
        block = contents.find('div', class_='textblock')
        soup_lines:ResultSet = block.find_all('p')
        lines = []
        for i, ln in enumerate(soup_lines):
            s = ln.text.strip()
            if i > 0:
                lines.append("")
            lines.append(s)
        since = self._get_since(block=block)
        if len(since) > 0:
            lines.append('')
            lines.extend(since)
        result = "\n".join(lines)
        return result
    
    def _get_since(self, block: Tag) -> List[str]:
        result = []
        since = block.find('dl', class_='section since')
        if since:
            s = since.find('dd').text.strip()
            result.append("**Since**")
            result.append("")
            result.append(self._indent + s)
        return result
            
    
    
    def _get_name(self, soup: BeautifulSoup):
        full = self._get_full_title(soup=soup)
        parts = full.split('.')
        return parts[len(parts) - 1]
    
    def _get_full_title(self, soup: BeautifulSoup):
        if self._title_full is None:
            header = soup.find('div', class_='title').text.strip()
            header = header.replace('::', '.')
            self._title_full = header.split()[0]
        return self._title_full
        
        
        
    # endregion Info

    # region Data

    def get_table_data(self) -> List[dataitem]:
        """
        Gets constants data

        Returns:
            List: list of tuple (value:number|str, raw_value:str, name:str, type:str, lines:[])

        Raises:
            ValueError: If url is not set.
        """
        if not self._url:
            raise ValueError('URL is not set')
        soup = BeautifulSoup(self.get_raw_html(), 'lxml')

        items = self._get_memitems(soup=soup)
        const_info = self._get_const_details(memitetms=items)
        return const_info

    def _clean_desc(self, desc: str) -> str:
        result = desc
        if self._replace_dual_colon:
            result = result.replace("::", ".")
        result = result.replace('\\n', '\\\\\\\\n').replace('\\r', '\\\\\\\\r')
        result = result.replace('"', '\\"')
        return result.strip()

    def get_formated_data(self):
        data = self.get_table_data()
        lines = []
        for itm in data:
            s = f'"{itm.name}": ["{itm.raw_value}"'
            if len(itm.lines) > 0:
                s_ln = ', [\n'
                for j, line in enumerate(itm.lines):
                    if j > 0:
                        s_ln += ',\n    "",\n'
                    s_ln += f'    "{self._clean_desc(line)}"'
                s_ln += '\n]'
                s += s_ln
            s += ']'
            lines.append(s)
        result = ',\n'.join(lines)
        return result

    def _get_const_details(self, memitetms: ResultSet) -> List[dataitem]:
        results = []
        for itm in memitetms:
            text: str = itm.find("td", class_='memname',
                                 recursive=True).text.replace(' ', ',')
            parts = text.split(',')
            _type = parts[1]
            name = parts[2]
            raw_value = parts[4]
            value = self._get_number(raw_value)
            docs = itm.find('div', class_='memdoc')
            lines = []
            if docs:
                doc_lines = docs.find_all('p')
                if doc_lines:
                    for ln in doc_lines:
                        lines.append(ln.text)
            di = dataitem(value=value, raw_value=raw_value, name=name,
                          datatype=_type, lines=lines)
            results.append(di)
        if self._sort:
            results.sort()
        return results

    def _get_memitems(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all('div', class_='memitem')

    def _get_tbl(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find('table', class_='memberdecls')

    def _get_rows_memitem(self, tbl: ResultSet) -> ResultSet:
        def check_row(tag: Tag) -> bool:
            if tag.has_attr('class'):
                _class = tag['class']
                if isinstance(_class, str):
                    return _class.startswith('memitem')
                else:
                    return _class[0].startswith('memitem')
            return False

        return tbl.find_all(check_row)
    # endregion Data

    # region internal Non specific methods
    def _get_number(self, input: str) -> Union[str, int, float]:
        if not input:
            return ''
        try:
            return int(input)
        except ValueError:
            pass
        try:
            return int(input, 16)
        except ValueError:
            pass
        try:
            return float(input)
        except ValueError:
            pass
        return input
    # endregion internal Non specific methods

    # region raw html

    def get_raw_html(self) -> str:
        if not self._url:
            return ''
        if not self._raw:
            self._raw = self.get_request_text(self.url)
        return self._raw

    # endregion raw html

    # region Properties
    @property
    def url(self) -> str:
        """Specifies url

            :getter: Gets url value.
            :setter: Sets url value.
        """
        return self._url

    @url.setter
    def url(self, value: str):
        self._url = value

    # endregion Properties


class ConstWriter(WriteBase):
    def __init__(self, parser:Parser, **kwargs):
        self._parser = parser
        self._hex = kwargs.get('hex', False)
        self._sort = kwargs.get('sort', True)
        self._flags = kwargs.get('flags', False)
        self._copy_clipboard = kwargs.get('copy_clipboard', False)
        self._print = kwargs.get('print', False)
        self._indent_amt = 4
        self._p_name = None
        self._p_url = None
        self._p_desc = None
        _path = Path(os.path.dirname(__file__), 'template', 'const.tmpl')
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
        # if self._copy_clipboard:
        #     pc.copy(self._template)
        if self._print:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self._template)

    def _set_template_data(self):
        self._template = self._template.replace('{hex}', str(self._hex))
        self._template = self._template.replace('{sort}', str(self._sort))
        self._template = self._template.replace('{flags}', str(self._flags))
        self._template = self._template.replace('{name}', self._p_name)
        self._template = self._template.replace('{link}', self._p_url)
        indent = ' ' * self._indent_amt
        indented = textwrap.indent(self._p_desc, indent).lstrip()
        self._template = self._template.replace('{desc}', indented)
        indented = textwrap.indent(self._p_data, indent)
        # indented = indented.lstrip()
        self._template = self._template.replace('{data}', indented)
        

    def _write_file(self):
        pass

    def _set_info(self):
        data = self._parser.get_info()
        self._p_name = data['name']
        self._p_desc = data['desc']
        self._p_url = data['url']
        self._p_data = self._parser.get_formated_data()


def main():
    parser = argparse.ArgumentParser(description='const')
    parser.add_argument('-u', '--url',
                        help='Url to parse', type=str, required=True)
    parser.add_argument(
        '-s', '--sort', help='Sort results', type=bool, default=True)
    parser.add_argument(
        '-d', '--dual-colon', help='Replace :: with .', type=bool, default=True)
    
    parser.add_argument(
        '-f', '--flags', help='Treat as flags', type=bool, default=False)
    parser.add_argument(
        '-x', '--hex', help='Treat as hex', type=bool, default=False)
    
    args = parser.parse_args()
    p = Parser(url=args.url, sort=args.sort,
               replace_dual_colon=args.dual_colon)
    print('')
    w = ConstWriter(parser=p, copy_clipboard=True, print=True, flags=args.flags, hex=args.hex)
    w.write()
 


if __name__ == '__main__':
    main()

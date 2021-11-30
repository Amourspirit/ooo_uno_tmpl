#!/usr/bin/env python
import argparse
from typing import List, Union
from bs4 import BeautifulSoup
from bs4.element import ResultSet, SoupStrainer, Tag
import requests
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw
from kwhelp import rules
from collections import namedtuple

dataitem = namedtuple(
    'dataitem', ['value', 'raw_value', 'name', 'datatype', 'lines'])


class ConstWriter:
    pass


class Parser:
    
    # region init
    @RuleCheckAllKw(arg_info={"url": 0, "sort": 1, "replace_dual_colon": 1},
                    rules=[rules.RuleStrNotNullEmptyWs, rules.RuleBool],
                    ftype=DecFuncEnum.METHOD)
    def __init__(self, **kwargs):
        self._url = kwargs.get('url', '')
        self._raw = ''
        self._sort = kwargs.get('sort', True)
        self._replace_dual_colon = kwargs.get('replace_dual_colon', True)

    # endregion init

    # region request
    def get_request_text(self, url: str) -> str:
        response = requests.get(url=url)
        if response.status_code != 200:
            raise Exception('bad response code:' + str(response.status_code))
        html_text = response.text
        return html_text
    # endregion request

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
        data = self.get_data()
        lines = []
        for itm in data:
            s = f'"{itm.name}": ("{itm.raw_value}"'
            if len(itm.lines) > 0:
                s_ln = ', [\n'
                for j, line in enumerate(itm.lines):
                    if j > 0:
                        s_ln += ',\n    "",\n'
                    s_ln += f'    "{self._clean_desc(line)}"'
                s_ln += '\n]'
                s += s_ln
            s += ')'
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

def main():
    parser = argparse.ArgumentParser(description='const')
    parser.add_argument('-u', '--url',
                        help='Url to parse', type=str, required=True)
    parser.add_argument(
        '-s', '--sort', help='Sort results', type=bool, default=True)
    parser.add_argument(
        '-d', '--dual-colon', help='Replace :: with .', type=bool, default=True)
    args = parser.parse_args()
    p = Parser(url=args.url, sort=args.sort,
               replace_dual_colon=args.dual_colon)

    # print(p._get_data())
    f_data = p.get_formated_data()
    print('')
    print(f_data)


if __name__ == '__main__':
    main()

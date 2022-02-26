import time
import calendar
import re
import json
import textwrap
import logging
from deprecated import deprecated
from typing import Iterable, Optional, Set, Tuple, Union, List
from kwhelp.decorator import AcceptedTypes, DecArgEnum, DecFuncEnum, RuleCheckAllKw, TypeCheckKw
from kwhelp import rules
from bs4.element import Tag
from pathlib import Path
from datetime import datetime, timezone
from rel import mod_rel as RelInfo
from . import log_load
from .constants import URL_SPLIT
from .. import mod_type as ModType
from ..dataclass.name_info import NameInfo
# region Logger
logger: logging.Logger = log_load.get_logger()
# endregion Logger

# region util
py_name_pattern = re.compile('[\W_]+')
pattern_generic_name = re.compile(r"([a-zA-Z0-9_]+)(<[A-Z, ]+>)")
py_ns_pattern = re.compile(r'[^a-zA-Z0-9\._]+')
curly_brace_close_pattern = re.compile(r'[^};]')
pattern_sq_braket = re.compile(r"\[.*\]")


def str_clean(input: str, **kwargs) -> str:
    """
    Cleans and encodes string for template replacemnt

    Keyword Arguments:
        replace_dual (bool, optional): Replace ``::`` with ``.`` Default ``True``
    """
    _replace_dual = bool(kwargs.get('replace_dual', True))
    result = input
    if _replace_dual:
        result = result.replace("::", ".")
    result = result.replace('\\n', '\\\\\\\\n').replace('\\r', '\\\\\\\\r')
    result = result.replace('"', '\\"')
    return result.strip()


class Util:
    """Utility class of static methods for operations"""

    TYPE_RULES: ModType.TypeRules = None

    @staticmethod
    def is_fragment_url(in_str: str) -> bool:
        """
        Gets if an input string contains ``#`` character

        Args:
            in_str (str): input to test

        Returns:
            bool: ``True`` if ``#`` is found; Otherwise, ``False``
        """
        if not in_str:
            return False
        i = in_str.find('#')
        return i >= 0

    @staticmethod
    def get_ns_from_url(url: str, name: Optional[str] = None) -> str:
        """
        Gets full name form a realitive for full url string.

        ``com.sun.star.awt`` from ``namespacecom_1_1sun_1_1star_1_1awt.html#ad249d76933bdf54c35f4eaf51a5b7965``.

        ``com.sun.star.awt.XMessageBoxFactory`` from ``com_1_1sun_1_1star_1_1awt_1_1XMessageBoxFactory``.

        Args:
            url (str): full or realitve Url string
            name (str, optional): Optional name that is use to replace or appnd to namespace return.
                Some urls may have a unexpected ending such as ``structcom_1_1sun_1_1star_1_1beans_1_1Pair_3_01T_00_01U_01_4.html``.
                Defaults to ``None``.

        Returns:
            str: namespace format sucha as ``com.sun.star.awt`` or ``com.sun.star.awt.XMessageBoxFactory``

        Note:
            ``name`` param is appended with urls that contain a fragment ( # ).
            ``name`` param replaces name part of urls that do not have a fragment.
        """
        parts = url.split(URL_SPLIT)
        parts[0] = 'com'
        if Util.is_fragment_url(url):
            # fragment such as: namespacecom_1_1sun_1_1star_1_1awt.html#ad249d76933bdf54c35f4eaf51a5b7965
            last = parts.pop()  # awt.html#ad249d76933bdf54c35f4eaf51a5b7965
            parts.append(last.split(sep='.', maxsplit=1)[0])
            if name:
                parts.append(name)
        else:
            # No fragment sucha as: interfacecom_1_1sun_1_1star_1_1awt_1_1XMessageBoxFactory.html
            last = parts.pop()  # XMessageBoxFactory.html
            if name:
                parts.append(name)
            else:
                # caution to be used with not providing a name.
                # some url are not ending in a clean name such as
                # urls for generic types Pair < U, T > ect...
                parts.append(last.split(sep='.', maxsplit=1)[0])
        return ".".join(parts)

    @staticmethod
    @RuleCheckAllKw(arg_info={'ns': 0, "name": 0}, rules=[rules.RuleStrNotNullOrEmpty], ftype=DecFuncEnum.METHOD_STATIC)
    def get_full_import(ns: str, name: str) -> str:
        """
        Get a full import name such as ``com.sun.star.uno.XInterface``

        Args:
            ns (str): Namespace to prepend to name if it is not a full namespace
            name (str): name or namespace

        Returns:
            str: full namesapce such as ``com.sun.star.uno.XInterface``
        """
        if not name.startswith('com.'):
            return ns + '.' + name
        return name

    @staticmethod
    def get_ns_from_a_tag(a_tag: Tag) -> Union[str, None]:
        """
        Gets a namespace from an anchor tag

        Args:
            a_tag (Tag): Anchor Tag

        Returns:
            Union[str, None]: Namesapce if Valid anchor tag. Otherwise ``None``

        See also:
            ``Util.get_ns_from_url()``
        """
        if not a_tag:
            return None
        href: str = a_tag.get('href', None)
        if not href:
            return None
        text = a_tag.text.strip().replace('::', '.').rstrip('.')
        name = None
        if text:
            parts = text.rsplit(sep='.', maxsplit=1)
            name = parts.pop()
        return Util.get_ns_from_url(url=href, name=name)

    @staticmethod
    def encode_file_name(name: Union[Path, str]) -> str:
        _name = str(name)
        _name = _name.replace(' ', '_').replace('<', '').replace('>', '')
        return _name

    @staticmethod
    def get_timestamp_utc() -> datetime:
        """
        Gets utc timestamp in format of ``2021-12-16 11:37:50+00:00``

        Returns:
            datetime: utc timestamp
        """
        current_GMT = time.gmtime()
        ts = calendar.timegm(current_GMT)
        return datetime.fromtimestamp(ts, tz=timezone.utc)

    @staticmethod
    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD_STATIC)
    def get_timestamp_from_str(input: str) -> datetime:
        """
        Converts input in the format of ``2021-12-16 11:37:50+00:00`` into datetime

        Args:
            input (str): input date string

        Returns:
            datetime: input converted to ``datetime``
        """
        try:
            dt_object = datetime.strptime(input, "%Y-%m-%d %H:%M:%S%z")
            return dt_object
        except ValueError as e:
            logger.error("Util.get_timestamp_from_str() Error: %s", str(e))
            raise e

    @AcceptedTypes(int, opt_all_args=True, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def is_enum_nums(*args: int) -> bool:
        """
        Test to see if a sequence of numbers can be combinded a flags

        Returns:
            bool: ``True`` if can be combined as flags; Otherwise ``False``
        """
        # get the biggest number and then find all its possible flags.
        # if any smaller number is not a possible flag then return false
        num_in = [*args]
        num_len = len(num_in)
        num_in.sort()
        if num_len < 2:
            return False
        if num_len == 3:
            tmp_lst = [0, 1, 2]
            is_simple = True
            for i, y in enumerate(tmp_lst):
                is_simple = num_in[i] == y
                if not is_simple:
                    break
            if is_simple:
                return False
            tmp_lst = [1, 2, 3]
            is_simple = True
            for i, y in enumerate(tmp_lst):
                is_simple = num_in[i] == y
                if not is_simple:
                    break
            if is_simple:
                return False
        num = num_in.pop()
        mod = num % 2
        if mod != 0:
            return False
        nums = set()
        shift_num = num
        while shift_num > 0:
            shift_num = shift_num >> 1
            nums.add(shift_num)
        is_flags = True
        for i in num_in:
            if i < 0:
                is_flags = False
                break
            if not i in nums:
                is_flags = False
                break
        return is_flags

    @AcceptedTypes(str, opt_all_args=True, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def get_clean_name(input: str, sub: str = '') -> str:
        """
        Removes all char from a string except for ``a-zA-Z0-9_``

        Args:
            input (str): string to clean
            sub (str, optional): replacement string for non matching characters.
                Default is empty string.

        Returns:
            str: input with any other chars replaced
        """
        # https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
        return py_name_pattern.sub(sub, input)

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD_STATIC)
    def get_clean_method_name(input: str) -> str:
        """
        Clean a methpd/property name and changes name suah as ``Pair< T, U >`` to ``Pair``

        Args:
            input (str): name

        Returns:
            str: cleaned name
        """
        return Util.get_clean_classname(input=input)

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD_STATIC)
    def get_clean_classname(input: str) -> str:
        """
        Clean a class name and changes name suah as ``Pair< T, U >`` to ``Pair``

        Args:
            input (str): name

        Returns:
            str: cleaned name
        """
        # convert 'Pair< T, U >' to 'Pair'
        s = pattern_generic_name.sub(r'\g<1>', input)
        s = s.replace(" ", "_")
        return s

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def get_clean_filename(input: str) -> str:
        """
        Clean a file name and changes name suah as ``Pair< T, U >`` to ``Pair``

        Args:
            input (str): filename

        Returns:
            str: cleaned file name
        """
        # convert 'Pair< T, U >' to 'Pair'
        s = pattern_generic_name.sub(r'\g<1>', input)
        s = s.replace(" ", "_")
        return s

    @AcceptedTypes(str, str, bool, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def get_clean_ns(input: str, sub: str = '', ltrim=False) -> str:
        """
        Removes all char from a string except for ``a-zA-Z0-9_.``

        Args:
            input (str): string to clean
            sub (str, optional): replacement string for non matching characters.
                Default is empty string.
            ltrim (bool, optonal): if ``True`` leading ``.`` are removed. Default ``False``

        Returns:
            str: input with any other chars replaced
        """
        # https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
        if ltrim is False:
            return py_ns_pattern.sub(sub, input)
        return py_ns_pattern.sub(sub, input).lstrip('.')

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def clean_curly_brace_close(input: str) -> str:
        """
        Removes all char from a string except for ``};``

        Args:
            input (str): string to clean

        Returns:
            str: input with any other chars replaced
        """
        return curly_brace_close_pattern.sub('', input)

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def clean_sq_braces(input: str) -> str:
        """
        Removes opening ``[.*]``

        Args:
            input (str): string to clean

        Returns:
            str: input to remove square brackets and all in between
        """
        return pattern_sq_braket.sub('', input)

    @AcceptedTypes((dict, list), int, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def get_formated_dict_list_str(obj: Union[dict, list], indent=4) -> str:
        """
        Get a formated dictionary or list

        Args:
            obj (Union[dict, list]): Dict or list to get formats string for.
            indent (int, optional): The number of spaces to indent string.. Defaults to ``2``.

        Returns:
            str: string of formated dictionary properties and values
        """
        if not isinstance(obj, dict) and not isinstance(obj, list):
            return "{}"
        _indent = 4 if indent < 0 else indent
        formatted = json.dumps(obj, indent=_indent)
        return formatted

    @AcceptedTypes((list, tuple), int, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def get_string_list(lines: List[str], indent_amt: int = 0) -> str:
        """
        Converts a list into str.
        Similar to calling str(lines) but handles more edge cases.

        Args:
            lines (List[str]): list to convert
            indent_amt (int, optional): Amount to indent results. Defaults to 0.

        Returns:
            str: List as string.
        """
        _lines = Util._encode_list(lines)
        c_lines = Util._decode_list(str(_lines).split(','))
        s = ',\n'.join(c_lines)
        if indent_amt > 0:
            s = Util.indent(text=s, indent_amt=indent_amt)
        return s

    @AcceptedTypes(str, opt_all_args=True, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def get_last_part(input: str, sep='.') -> str:
        """
        Splits a string and returns the last part

        Args:
            input (str): string to get last part of.
            sep (str, optional): string used to split. Defaults to ``.``

        Returns:
            str: [description]
        """
        if not input:
            return ''
        _parts = input.rsplit(sep, 1)
        return _parts[0] if len(_parts) == 1 else _parts[1]

    @AcceptedTypes(str, int, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def indent(text: str, indent_amt: int = 4) -> str:
        """
        Indents a multi line string

        Args:
            text (str): text to apply indent
            indent_amt (int, optional): Amout of indent. Defaults to 4.

        Returns:
            str: indented text.
        """
        if indent_amt <= 0:
            return text
        indent = ' ' * indent_amt
        s = textwrap.indent(text, indent)
        return s

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def camel_to_snake(input: str) -> str:
        """
        Converts Camel case to snake clase

        Args:
            name (str): Camel name

        Returns:
            str: snake case
        """
        return RelInfo.camel_to_snake(input=input)

    @staticmethod
    def get_clean_imports(ns: str, imports: Iterable[str]) -> Set[str]:
        """
        Gets a set of unique imports.

        Args:
            ns (str): namespace to append if any item in imports is misssing ns part
            imports (Iterable[str]): Imports list, set, tuple, etc

        Returns:
            Set[str]: Set of imports. Each import is guaranteed to be full ns object.
        """
        sep = '.'
        results: Set[str] = set()
        for im in imports:
            if im.find(sep) < 0:
                s = ns + sep + im
            else:
                s = im
            results.add(s)
        return results

    @staticmethod
    def get_rel_import(i_str: str, ns: str, sep: str = '.') -> Tuple[str, str]:
        """
        Gets realitive import Tuple

        Args:
            i_str (str): Namespace and object such as ``com.sun.star.uno.Exception``
            ns (str): Namespace used to get realitive postion such as ``com.sun.star.awt``
            sep (str, optional): Namespace seperator. Defaults to ``.``

        Returns:
            Tuple[str, str]: realitive import info such as ``('..uno.exception', 'Exception')``
        """
        return RelInfo.get_rel_import(in_str=i_str, ns=ns, sep=sep)

    @staticmethod
    def get_rel_import_long(i_str: str, ns: str, sep: str = '.') -> Tuple[str, str, str]:
        """
        Gets realitive import Tuple

        Args:
            i_str (str): Namespace and object such as ``com.sun.star.uno.Exception``
            ns (str): Namespace used to get realitive postion such as ``com.sun.star.awt``
            sep (str, optional): Namespace seperator. Defaults to ``.``

        Returns:
            Tuple[str, str]: realitive import info such as ``('..uno.exception', 'Exception')``
        """
        return RelInfo.get_rel_import_long(in_str=i_str, ns=ns, sep=sep)

    def get_rel_import_long_name(i_str: str, ns: str, sep: str = '.') -> str:
        """
        Geta a long Name. Same as getting last part of ```get_rel_import_long()```

        Args:
            in_str (str): Namespace and object such as ``com.sun.star.uno.Exception``
            ns (str): Namespace used to get realitive postion such as ``com.sun.star.awt``
            sep (str, optional): Namespace seperator. Defaults to ``.``

        Returns:
            str: Long name such as ``uno_exception``
        """
        return RelInfo.get_rel_import_long_name(
            in_str=i_str,
            ns=ns,
            sep=sep
        )

    @AcceptedTypes(str, opt_all_args=True, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def encode_char(input: str, replace: str, en: str = '\xff') -> str:
        """
        Encodes all matching chars in a string with the value of ``en``.
        Chars ``\\xff`` and ``\\xfe`` are BOM

        Args:
            input (str): text to search and replace
            replace (str): char to replace all instances of
            en (str, optional): Value to replace. Defaults to ``\\xff``.

        Returns:
            str: input with chars replace with ``en`` value
        """
        return input.replace(replace, en)

    @AcceptedTypes(str, opt_all_args=True, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def decode_char(input: str, restore: str, de: str = '\xff') -> str:
        """
        Decodes allmathing chars in a string with the value of ``restore``.
        Chars ``\\xff`` and ``\\xfe`` are BOM

        Args:
            input (str): text to search and restore
            restore (str): char to restore
            de (str, optional): value to decode. Defaults to ``\\xff``.

        Returns:
            str: [description]
        """
        return input.replace(de, restore)

    @deprecated(version='0.1.4', reason='Deprecated, use get_python_type() instead')
    @AcceptedTypes(str, opt_args_filter=DecArgEnum.NAMED_ARGS, ftype=DecFuncEnum.METHOD_STATIC)
    @TypeCheckKw(arg_info={"typings": 0, "quote": 0}, types=[bool], ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def get_py_type(uno_type: str, **kwargs) -> str:
        """
        Gets python type from uno type.

        Converts values such as ``sequence< ::com::sun::star::uno::XInterface>`` =>
        ``List[XInterface]``. Also simple conversion such as ``long`` => ``int``

        Args:
            uno_type (str): Uno type such as ``long``

        Keyword Args:
            typings (bool, optional): If ``True`` typings is added in front of wrapped
                so ``List[int]`` => ``typing.List[int]. Default ``True``
            cb (callable, optional): callback function. eg: ``cb(data)``
            quote (bool, optional): If ``True`` return value will be wrapped in quotes
                for non python types such as ``'XInterface'``. Default ``True``

        Returns:
            str: ``uno_type`` converted to python type.

        Notes:
            Conversion can be complex operation. For this reason a callback function
            can be passed in.

            Callback function signature is ``cb(data)``
            Callback ``data`` is a dictionary of information about the conversion.
            If ``uno_type`` is a sequence (list) then ``data['wdata']`` contains info
            on the sequence.

            ``data``: {
                "uno_type":     "(str): original uno_type value passed in",
                "is_py_type":   "(bool): Will be True if uno_type is converted to a python type
                                    such as long => int. Will also be True for sequences that match
                                    such as sequence<long> => list[int].",
                "is_wrapper":   "(bool): if conversoin results in sequence<long> => List[int]",
                "is_typing":    "(bool): True if is wrapped and typings arg is True; Otherwise, False",
                "long_type":    "(str): ns and type such as com.sun.star.awt.AdjustmentType
                                    When sequence is found this will still be the long name of the inner wrapped.
                "wdata": {
                    "is_py_type":    "(bool): True if wrapper type is a python type such as List; Otherwise, False",
                    "py_type_inner": "(bool): True if wrapped is a python type such as int; Otherwise, False",
                    "prefix":        "(str): prefixe will not be added if typings arg is False",
                    "wrapper":       "(str): Wrapper such as typing.List or List",
                    "long_type":     "(str); ns and type such as com.sun.star.awt.AdjustmentType
                },
                "returns": "(object, optional): Default value is None. If a value is assigned
                            during callback then the value of returns will be returned from method.
            }
        """
        logger.warning(
            'Util.get_py_type is deprecated, use get_python_type() instead')

        if not uno_type:
            return ''

        def ex_type(in_parts: List[str]) -> Union[dict, None]:
            start = in_parts[0].rstrip()
            if not start in TYPE_MAP_EX:
                return None
            params: dict = TYPE_MAP_EX[start]
            _results = {
                "is_typing": params.get("is_typing", False),
                "is_py_type": params.get("is_py_type", True)
            }
            full = '<'.join(in_parts)
            _regx = params.get('regex', None)
            _replace: str = params['replace']
            if _regx:
                m = re.match(_regx, full)
                if m:
                    groups = m.groups()
                    replacements = []
                    for t in groups:
                        replacements.append(TYPE_MAP.get(t, 'object'))
                    _replace = _replace.format(*replacements)
            _results['type'] = _replace
            _results['long_type'] = params.get('long_type', _replace)
            return _results

        def do_cb(_cb: callable, data):
            if not _cb:
                return
            _cb(data)

        add_typings = bool(kwargs.get('typings', True))
        arg_quote = bool(kwargs.get('quote', True))
        cb = kwargs.get('cb', None)
        cb_data = {
            "uno_type": uno_type,
            "is_py_type": False,
            "is_wrapper": False,
            "is_typing": False,
            "returns": None,
            "wdata": {
                "is_wrapper": False,
                "is_py_type": False,
                "wdata": {
                    "prefix": "",
                    "wrapper": "",
                    "py_type_inner": False
                }
            }
        }
        _u_type = uno_type.strip().lstrip().replace("::", ".").lstrip('.')
        # check for # sequence< string >
        parts = _u_type.split(sep='<', maxsplit=1)
        if len(parts) > 1:
            ex_info = ex_type(parts)
            if ex_info:
                cb_data['is_wrapper'] = ex_info.get('is_wrapper', False)
                cb_data['is_typing'] = ex_info.get('is_typing', False)
                cb_data['long_type'] = ex_info['long_type']
                cb_data['is_py_type'] = ex_info['is_py_type']
                do_cb(cb, cb_data)
                return ex_info['type']
            is_pytype = True
            cb_data['is_wrapper'] = True
            clean_wrapper = Util.get_last_part(Util.get_clean_name(parts[0]))
            wrapper = TYPE_MAP.get(clean_wrapper, None)
            if wrapper:
                cb_data['wdata']['is_py_type'] = True
            else:
                is_pytype = False
                cb_data['wdata']['is_py_type'] = False
            type_pre = "typing." if add_typings else ''
            cb_data['is_typing'] = add_typings
            cb_data['wdata']['prefix'] = type_pre
            if wrapper:
                # got a match from TYPE_MAP
                # title case the word and add typings
                wrapper = type_pre + wrapper.title()
            else:
                wrapper = type_pre + 'List'
            cb_data['wdata']['wrapper'] = wrapper
            _type = Util.get_clean_ns(input=parts[1], ltrim=True)
            cb_data['long_type'] = _type
            _type = Util.get_last_part(_type)
            map_type = TYPE_MAP.get(_type, None)
            is_inner_py_type = True
            if not map_type:
                is_inner_py_type = False
                is_pytype = False
                map_type = _type
            cb_data['wdata']['py_type_inner'] = is_inner_py_type

            cb_data['is_py_type'] = is_pytype
            cb_data['type'] = map_type

            do_cb(cb, cb_data)
            if cb_data['returns']:
                return cb_data['returns']
            if is_inner_py_type is False and arg_quote is True:
                return f"'{wrapper}[{map_type}]'"
            return f"{wrapper}[{map_type}]"
        cb_data['long_type'] = Util.get_clean_ns(_u_type)
        _u_type_clean = Util.get_clean_name(Util.get_last_part(_u_type))
        result = TYPE_MAP.get(_u_type_clean, None)
        if result:
            if _u_type_clean == "type":
                # edge case of type of type
                # type is mapped to object in TYPE_MAP
                cb_data['is_typing'] = True
                result = f"typing.Type"
            cb_data['is_py_type'] = True
            cb_data['type'] = result
            do_cb(cb, cb_data)
            return result
        cb_data['type'] = _u_type_clean
        do_cb(cb, cb_data)
        if cb_data['returns']:
            return cb_data['returns']
        if arg_quote:
            return f"'{_u_type_clean}'"
        return _u_type_clean

    @staticmethod
    @TypeCheckKw(arg_info={"in_type": 0, "ns": 1}, types=[str, (str, type(None))], ftype=DecFuncEnum.METHOD_STATIC)
    def get_python_type(in_type: str, name_info: NameInfo, ns: str, long_names: bool = False) -> ModType.PythonType:
        """
        Gets Python Type info including an required imports.

        Args:
            in_type (str): uno type

        Returns:
            PythonType: class that contains type, requires typing and imporst info.
        """
        if Util.TYPE_RULES is None:
            Util.TYPE_RULES = ModType.TypeRules()

        logger.debug("Util.get_python_type() in_type: '%s'", in_type)

        def is_self_import(s: str, class_name: str) -> bool:
            try:
                p_type = Util.TYPE_RULES.get_python_type(in_type=s)
                if not p_type.imports:
                    return False
                if p_type.imports == class_name:
                    return True
                full_name = ns + '.' + class_name
                return p_type.imports == full_name
            except Exception as e:
                logger.error(e, exc_info=True)
                raise e

        Util.TYPE_RULES.namespace = ns
        Util.TYPE_RULES.long_names = long_names
        self_import = is_self_import(in_type, name_info.name)
        if self_import:
            Util.TYPE_RULES.long_names = False

        try:
            py_type = Util.TYPE_RULES.get_python_type(in_type)
            if self_import:
                py_type.imports = None
            return py_type
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e

    @staticmethod
    @AcceptedTypes((str, Path), ftype=DecFuncEnum.METHOD_STATIC)
    def mkdirp(dest_dir: Union[str, Path]):
        """
        Creates directory and all child directories if needed

        Args:
            dest_dir (Union[str, Path]): path to create directories for.
                Must be dir path only. No checking is done for file names.
        """
        # Python ≥ 3.5
        if isinstance(dest_dir, Path):
            dest_dir.mkdir(parents=True, exist_ok=True)
        else:
            Path(dest_dir).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _encode_list(lst: List[str]) -> List[str]:
        results = []
        for el in lst:
            s = Util.encode_char(el, ',')
            results.append(s)
        return results

    @staticmethod
    def _decode_list(lst: List[str]) -> List[str]:
        results = []
        for el in lst:
            s = Util.decode_char(el, ',')
            results.append(s)
        return results

# endregion util

from pathlib import Path
import uno
from ..utilities import util

class ModelsBase:
    def get_safe_word(self, in_str: object) -> object:
        """
        Get safe word. If a word is a reserved python word then _ is appended.

        Args:
            in_str (object): input

        Returns:
            object: if ``in_str`` is not str then it is returned verbatium. Otheriwse returns str.
        """
        if not isinstance(in_str, str):
            return in_str
        if in_str in util.RESERVER_WORDS:
            return in_str + '_'
        return in_str

    def get_attrib_default(self, name: str, returns: str, uno_none: bool = False) -> str:
        """
        Get defatul attribute value from uno

        Args:
            name (str): Name of property to get attrib for.
            returns (str): property returns type
            uno_none (bool, optional): If ``True`` replaces ``None`` with ``UNO_NONE`` where needed; Otherwise uses ``None``. Defaults to False.

        Returns:
            str: attribute default value as string.

        Note:
            If current exception/struct is not in the installled uno version then
            all unknow value are either ``None`` or ``UNO_NONE``
            
            For instance ReadOnlyOpenRequest: https://tinyurl.com/ycu8u8wu
            is a 7.2 version
        """
        if self.uno_instance is None:
            if uno_none is True:
                return 'UNO_NONE'
            return 'None'
        result = getattr(self.uno_instance, name, None)
        if isinstance(result, str):
            return result
        elif isinstance(result, uno.Enum):
            return f"{returns}.{result.value}"
        elif isinstance(result, uno.Char):
            char = ''.join(r'\u{:04X}'.format(ord(chr))
                           for chr in result.value)
            return char
        elif isinstance(result, uno.ByteSequence):
            if uno_none is True:
                return 'UNO_NONE'
            return 'None'
        elif hasattr(result, '__pyunostruct__'):
            if uno_none is True:
                return 'UNO_NONE'
            if returns == 'object':
                return 'None'
            return f"{returns}()"
        return str(result)


    def _get_json_path(self, json_file) -> Path:
        p = Path(json_file)
        if p.is_absolute():
            return p
        return Path(util.get_root(), p)

    def _get_path_from_ns(self, ns: str) -> Path:
        parts = ns.removeprefix('com.sun.star.').split('.')
        file_name = parts.pop() + ".json"
        p = Path(util.get_root(), self._config.uno_base_dir, *parts, file_name)
        return p
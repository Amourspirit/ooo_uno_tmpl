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

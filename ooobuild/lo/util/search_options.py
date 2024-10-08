# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.util
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing
from ..lang.locale import Locale as Locale_70d308fa
from .search_algorithms import SearchAlgorithms as SearchAlgorithms_e2c00d36


class SearchOptions(object):
    """
    Struct Class


    See Also:
        `API SearchOptions <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1SearchOptions.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.SearchOptions'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.util.SearchOptions'
    """Literal Constant ``com.sun.star.util.SearchOptions``"""

    def __init__(self, algorithmType: typing.Optional[SearchAlgorithms_e2c00d36] = SearchAlgorithms_e2c00d36.ABSOLUTE, searchFlag: typing.Optional[int] = 0, searchString: typing.Optional[str] = '', replaceString: typing.Optional[str] = '', Locale: typing.Optional[Locale_70d308fa] = UNO_NONE, changedChars: typing.Optional[int] = 0, deletedChars: typing.Optional[int] = 0, insertedChars: typing.Optional[int] = 0, transliterateFlags: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            algorithmType (SearchAlgorithms, optional): algorithmType value.
            searchFlag (int, optional): searchFlag value.
            searchString (str, optional): searchString value.
            replaceString (str, optional): replaceString value.
            Locale (Locale, optional): Locale value.
            changedChars (int, optional): changedChars value.
            deletedChars (int, optional): deletedChars value.
            insertedChars (int, optional): insertedChars value.
            transliterateFlags (int, optional): transliterateFlags value.
        """
        super().__init__()

        if isinstance(algorithmType, SearchOptions):
            oth: SearchOptions = algorithmType
            self.algorithmType = oth.algorithmType
            self.searchFlag = oth.searchFlag
            self.searchString = oth.searchString
            self.replaceString = oth.replaceString
            self.Locale = oth.Locale
            self.changedChars = oth.changedChars
            self.deletedChars = oth.deletedChars
            self.insertedChars = oth.insertedChars
            self.transliterateFlags = oth.transliterateFlags
            return

        kargs = {
            "algorithmType": algorithmType,
            "searchFlag": searchFlag,
            "searchString": searchString,
            "replaceString": replaceString,
            "Locale": Locale,
            "changedChars": changedChars,
            "deletedChars": deletedChars,
            "insertedChars": insertedChars,
            "transliterateFlags": transliterateFlags,
        }
        if kargs["Locale"] is UNO_NONE:
            kargs["Locale"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._algorithm_type = kwargs["algorithmType"]
        self._search_flag = kwargs["searchFlag"]
        self._search_string = kwargs["searchString"]
        self._replace_string = kwargs["replaceString"]
        self._locale = kwargs["Locale"]
        self._changed_chars = kwargs["changedChars"]
        self._deleted_chars = kwargs["deletedChars"]
        self._inserted_chars = kwargs["insertedChars"]
        self._transliterate_flags = kwargs["transliterateFlags"]


    @property
    def algorithmType(self) -> SearchAlgorithms_e2c00d36:
        """
        search type
        """
        return self._algorithm_type

    @algorithmType.setter
    def algorithmType(self, value: SearchAlgorithms_e2c00d36) -> None:
        self._algorithm_type = value

    @property
    def searchFlag(self) -> int:
        """
        some flags - can be mixed
        """
        return self._search_flag

    @searchFlag.setter
    def searchFlag(self, value: int) -> None:
        self._search_flag = value

    @property
    def searchString(self) -> str:
        """
        The text or pattern to be searched.
        """
        return self._search_string

    @searchString.setter
    def searchString(self, value: str) -> None:
        self._search_string = value

    @property
    def replaceString(self) -> str:
        """
        The replacement text (is for optional replacing - SearchOption is only the data container for it)
        """
        return self._replace_string

    @replaceString.setter
    def replaceString(self, value: str) -> None:
        self._replace_string = value

    @property
    def Locale(self) -> Locale_70d308fa:
        """
        The locale for case insensitive search.
        """
        return self._locale

    @Locale.setter
    def Locale(self, value: Locale_70d308fa) -> None:
        self._locale = value

    @property
    def changedChars(self) -> int:
        """
        This many characters can be different (as a replacement) between the found word and the search pattern in a \"Weighted LevenshteinDistance\" search.
        """
        return self._changed_chars

    @changedChars.setter
    def changedChars(self, value: int) -> None:
        self._changed_chars = value

    @property
    def deletedChars(self) -> int:
        """
        This many characters can be missing in the found word in a \"Weighted Levenshtein Distance\" search.
        """
        return self._deleted_chars

    @deletedChars.setter
    def deletedChars(self, value: int) -> None:
        self._deleted_chars = value

    @property
    def insertedChars(self) -> int:
        """
        This many characters can be additional in the found word in a \"Weighted Levenshtein Distance\" search.
        """
        return self._inserted_chars

    @insertedChars.setter
    def insertedChars(self, value: int) -> None:
        self._inserted_chars = value

    @property
    def transliterateFlags(self) -> int:
        """
        Flags for the transliteration.
        
        Same meaning as the enum of com.sun.star.i18n.TransliterationModules
        """
        return self._transliterate_flags

    @transliterateFlags.setter
    def transliterateFlags(self, value: int) -> None:
        self._transliterate_flags = value


__all__ = ['SearchOptions']

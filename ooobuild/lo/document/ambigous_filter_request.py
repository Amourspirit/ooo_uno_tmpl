# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.document
# Libre Office Version: 7.2
from ooo.oenv.env_const import UNO_NONE
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class AmbigousFilterRequest(Exception_85530a09):
    """
    Exception Class

    should be used for interaction to handle states of ambiguous filter detection
    
    This exception indicates, that generic filter detection can't decide which of two filters is the right one. In this case an interaction will be made. Given URL can be used to decide between given two filters. Decision can be made e.g. by a dialog, on which the user must select one of these filters. A possible continuation of type XInteractionFilterSelect transport this decision back to source of started interaction.

    See Also:
        `API AmbigousFilterRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1document_1_1AmbigousFilterRequest.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.AmbigousFilterRequest'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.document.AmbigousFilterRequest'
    __pyunostruct__: str = 'com.sun.star.document.AmbigousFilterRequest'

    typeName: str = 'com.sun.star.document.AmbigousFilterRequest'
    """Literal Constant ``com.sun.star.document.AmbigousFilterRequest``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, URL: typing.Optional[str] = '', SelectedFilter: typing.Optional[str] = '', DetectedFilter: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            URL (str, optional): URL value.
            SelectedFilter (str, optional): SelectedFilter value.
            DetectedFilter (str, optional): DetectedFilter value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "URL": URL,
            "SelectedFilter": SelectedFilter,
            "DetectedFilter": DetectedFilter,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._url = kwargs["URL"]
        self._selected_filter = kwargs["SelectedFilter"]
        self._detected_filter = kwargs["DetectedFilter"]
        inst_keys = ('URL', 'SelectedFilter', 'DetectedFilter')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def URL(self) -> str:
        """
        transport URL which couldn't be detected right
        """
        return self._url
    
    @URL.setter
    def URL(self, value: str) -> None:
        self._url = value

    @property
    def SelectedFilter(self) -> str:
        """
        transport the preselected filter
        """
        return self._selected_filter
    
    @SelectedFilter.setter
    def SelectedFilter(self, value: str) -> None:
        self._selected_filter = value

    @property
    def DetectedFilter(self) -> str:
        """
        transport the real detected filter, which stands in conflict to the pre selected one
        """
        return self._detected_filter
    
    @DetectedFilter.setter
    def DetectedFilter(self, value: str) -> None:
        self._detected_filter = value


__all__ = ['AmbigousFilterRequest']


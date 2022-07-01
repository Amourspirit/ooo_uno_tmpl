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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.form
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class DatabaseDeleteEvent(EventObject_a3d70b03):
    """
    Struct Class

    is fired if a database record is going to be deleted.
    
    Please do not use anymore, this struct is deprecated.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API DatabaseDeleteEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1form_1_1DatabaseDeleteEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form'
    __ooo_full_ns__: str = 'com.sun.star.form.DatabaseDeleteEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.form.DatabaseDeleteEvent'
    """Literal Constant ``com.sun.star.form.DatabaseDeleteEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Bookmarks: typing.Optional[typing.Tuple[object, ...]] = ()) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Bookmarks (typing.Tuple[object, ...], optional): Bookmarks value.
        """

        if isinstance(Source, DatabaseDeleteEvent):
            oth: DatabaseDeleteEvent = Source
            self.Source = oth.Source
            self.Bookmarks = oth.Bookmarks
            return

        kargs = {
            "Source": Source,
            "Bookmarks": Bookmarks,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._bookmarks = kwargs["Bookmarks"]
        inst_keys = ('Bookmarks',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Bookmarks(self) -> typing.Tuple[object, ...]:
        return self._bookmarks
    
    @Bookmarks.setter
    def Bookmarks(self, value: typing.Tuple[object, ...]) -> None:
        self._bookmarks = value


__all__ = ['DatabaseDeleteEvent']

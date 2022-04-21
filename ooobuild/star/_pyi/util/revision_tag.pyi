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
# Namespace: com.sun.star.util
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing
from .date_time import DateTime as DateTime_84de09d3


class RevisionTag(object):
    """
    Struct Class

    represents the information that describes a revision of something.

    See Also:
        `API RevisionTag <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1RevisionTag.html>`_
    """
    typeName: Literal['com.sun.star.util.RevisionTag']

    def __init__(self, TimeStamp: typing.Optional[DateTime_84de09d3] = ..., Author: typing.Optional[str] = ..., Comment: typing.Optional[str] = ..., Identifier: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            TimeStamp (DateTime, optional): TimeStamp value.
            Author (str, optional): Author value.
            Comment (str, optional): Comment value.
            Identifier (str, optional): Identifier value.
        """


    @property
    def TimeStamp(self) -> DateTime_84de09d3:
        """
        contains the time when the revision was created ( can be invalid )
        """


    @property
    def Author(self) -> str:
        """
        contains an identifier for the author that created the revision( can be empty )
        """


    @property
    def Comment(self) -> str:
        """
        contains a comment that the author has left for this revision ( can be empty )
        """


    @property
    def Identifier(self) -> str:
        """
        contains a unique identifier for the revision and must not be empty
        
        This identifier can have any form. It can be something like \"1.2.3\" or \"Version 1\" etc. It depends on the revision control system how it names the revisions.
        """



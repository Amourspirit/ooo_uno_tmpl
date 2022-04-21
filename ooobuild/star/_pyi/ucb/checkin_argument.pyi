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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class CheckinArgument(object):
    """
    Struct Class

    contains information needed to checkin a document.
    
    The checkin command is always called on the target private working copy document.

    See Also:
        `API CheckinArgument <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1CheckinArgument.html>`_
    """
    typeName: Literal['com.sun.star.ucb.CheckinArgument']

    def __init__(self, MajorVersion: typing.Optional[bool] = ..., VersionComment: typing.Optional[str] = ..., SourceURL: typing.Optional[str] = ..., TargetURL: typing.Optional[str] = ..., NewTitle: typing.Optional[str] = ..., MimeType: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            MajorVersion (bool, optional): MajorVersion value.
            VersionComment (str, optional): VersionComment value.
            SourceURL (str, optional): SourceURL value.
            TargetURL (str, optional): TargetURL value.
            NewTitle (str, optional): NewTitle value.
            MimeType (str, optional): MimeType value.
        """


    @property
    def MajorVersion(self) -> bool:
        """
        Tells whether to create a new major or minor version during the checkin.
        """


    @property
    def VersionComment(self) -> str:
        """
        Contains the version comment to set during the checkin.
        """


    @property
    def SourceURL(self) -> str:
        """
        contains the URL of the source of the action (e.g.
        
        the URL of the temporary file to checkin).
        """


    @property
    def TargetURL(self) -> str:
        """
        contains the URL of the private working copy to checkin.
        """


    @property
    def NewTitle(self) -> str:
        """
        contains the title of the transferred object, if it is different from the original one.
        
        If this field is filled, for example, a file will be renamed while it is being checked in.
        """


    @property
    def MimeType(self) -> str:
        """
        contains the Mime-Type of the content to check-in as it may be different from the original one.
        """



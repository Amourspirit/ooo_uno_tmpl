# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.text
# Libre Office Version: 7.4
import typing


class SectionFileLink(object):
    """
    Struct Class

    describes the link for a text section.
    
    If the URL is an empty string, then the section is not linked.
    
    The bookmark of the URL (after the \"#\") is the name of a bookmark or a section name in the linked document. If a bookmark or section with this name exists in the document, then only this part is linked into the given text section.
    
    SectionFileLink.FilterName is the internal name of the document filter. To use this struct, it is not necessary to set SectionFileLink.FilterName. It will be automatically assigned.

    See Also:
        `API SectionFileLink <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1text_1_1SectionFileLink.html>`_
    """
    typeName: str = 'com.sun.star.text.SectionFileLink'

    def __init__(self, FileURL: typing.Optional[str] = ..., FilterName: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            FileURL (str, optional): FileURL value.
            FilterName (str, optional): FilterName value.
        """
        ...

    @property
    def FileURL(self) -> str:
        """
        contains the URL of the linked file.
        """
        ...
    @FileURL.setter
    def FileURL(self, value: str) -> None:
        ...
    @property
    def FilterName(self) -> str:
        """
        contains the name of the file filter that is used to load the linked file.
        """
        ...
    @FilterName.setter
    def FilterName(self, value: str) -> None:
        ...

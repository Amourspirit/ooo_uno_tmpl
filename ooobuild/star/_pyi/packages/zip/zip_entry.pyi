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
# Namespace: com.sun.star.packages.zip
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class ZipEntry(object):
    """
    Struct Class

    used to represent a ZIP file entry
    
    This interface is an IDL version of the Java interface java.util.zip.ZipFile with some minor adaptations.

    See Also:
        `API ZipEntry <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1packages_1_1zip_1_1ZipEntry.html>`_
    """
    typeName: Literal['com.sun.star.packages.zip.ZipEntry']

    def __init__(self, extra: typing.Optional[typing.Tuple[int, ...]] = ..., nVersion: typing.Optional[int] = ..., nFlag: typing.Optional[int] = ..., nMethod: typing.Optional[int] = ..., nTime: typing.Optional[int] = ..., nCrc: typing.Optional[int] = ..., nCompressedSize: typing.Optional[int] = ..., nSize: typing.Optional[int] = ..., nOffset: typing.Optional[int] = ..., nDiskNumber: typing.Optional[int] = ..., sName: typing.Optional[str] = ..., sComment: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            extra (typing.Tuple[int, ...], optional): extra value.
            nVersion (int, optional): nVersion value.
            nFlag (int, optional): nFlag value.
            nMethod (int, optional): nMethod value.
            nTime (int, optional): nTime value.
            nCrc (int, optional): nCrc value.
            nCompressedSize (int, optional): nCompressedSize value.
            nSize (int, optional): nSize value.
            nOffset (int, optional): nOffset value.
            nDiskNumber (int, optional): nDiskNumber value.
            sName (str, optional): sName value.
            sComment (str, optional): sComment value.
        """


    @property
    def extra(self) -> typing.Tuple[int, ...]:
        """
        optional extra field data for entry
        """


    @property
    def nVersion(self) -> int:
        """
        version needed to extract
        """


    @property
    def nFlag(self) -> int:
        """
        bit flags
        """


    @property
    def nMethod(self) -> int:
        """
        compression method
        """


    @property
    def nTime(self) -> int:
        """
        modification time
        """


    @property
    def nCrc(self) -> int:
        """
        CRC-32 of entry data.
        """


    @property
    def nCompressedSize(self) -> int:
        """
        uncompressed size of entry data
        """


    @property
    def nSize(self) -> int:
        """
        uncompressed size of entry data
        """


    @property
    def nOffset(self) -> int:
        """
        offset of LOC header
        """


    @property
    def nDiskNumber(self) -> int:
        """
        The number of the disk this entry is saved on.
        """


    @property
    def sName(self) -> str:
        """
        the entry name
        """


    @property
    def sComment(self) -> str:
        """
        optional comment
        """



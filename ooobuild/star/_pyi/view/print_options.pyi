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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.view
from abc import ABC

class PrintOptions(ABC):
    """
    Service Class

    describes the options for print jobs.
    
    These options are only valid for a single print job. They do not change layout or formatting of the document.

    See Also:
        `API PrintOptions <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1view_1_1PrintOptions.html>`_
    """
    @property
    def Collate(self) -> bool:
        """
        advises the printer to collate the pages of the copies.
        """
        ...

    @Collate.setter
    def Collate(self, value: bool) -> None:
        ...
    @property
    def CopyCount(self) -> int:
        """
        specifies the number of copies to print.
        """
        ...

    @CopyCount.setter
    def CopyCount(self, value: int) -> None:
        ...
    @property
    def DuplexMode(self) -> int:
        """
        determines the duplex mode for the print job.
        """
        ...

    @DuplexMode.setter
    def DuplexMode(self, value: int) -> None:
        ...
    @property
    def FileName(self) -> str:
        """
        if set, specifies the name of a file to print to.
        """
        ...

    @FileName.setter
    def FileName(self, value: str) -> None:
        ...
    @property
    def Pages(self) -> str:
        """
        specifies which pages to print.
        
        This range is given as at the user interface. For example: \"1-4;10\" to print the pages 1 to 4 and 10.
        """
        ...

    @Pages.setter
    def Pages(self, value: str) -> None:
        ...
    @property
    def PrinterName(self) -> str:
        """
        if set, specifies name of the printer to use.
        """
        ...

    @PrinterName.setter
    def PrinterName(self, value: str) -> None:
        ...
    @property
    def SinglePrintJobs(self) -> bool:
        """
        advises the printer to create a single print job for each copy.
        """
        ...

    @SinglePrintJobs.setter
    def SinglePrintJobs(self, value: bool) -> None:
        ...
    @property
    def Sort(self) -> bool:
        """
        advises the printer to sort the pages of the copies.
        """
        ...

    @Sort.setter
    def Sort(self, value: bool) -> None:
        ...
    @property
    def Wait(self) -> bool:
        """
        if set to TRUE, the corresponding XPrintable.print() request will be executed synchronous.
        """
        ...

    @Wait.setter
    def Wait(self, value: bool) -> None:
        ...


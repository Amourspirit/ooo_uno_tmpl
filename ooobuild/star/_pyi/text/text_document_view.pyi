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
# Namespace: com.sun.star.text
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_text_view_cursor_supplier import XTextViewCursorSupplier as XTextViewCursorSupplier_4c931037
from ..view.office_document_view import OfficeDocumentView as OfficeDocumentView_fd320de9

class TextDocumentView(OfficeDocumentView_fd320de9, XPropertySet_bc180bfa, XTextViewCursorSupplier_4c931037):
    """
    Service Class

    specifies the view of a TextDocument.
    
    **since**
    
        OOo 2.0

    See Also:
        `API TextDocumentView <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TextDocumentView.html>`_
    """
    @property
    def IsConstantSpellcheck(self) -> bool:
        """
        specifies if spell checking should be done while typing.
        
        **since**
        
            OOo 2.0
        """
        ...

    @IsConstantSpellcheck.setter
    def IsConstantSpellcheck(self, value: bool) -> None:
        ...
    @property
    def IsHideSpellMarks(self) -> bool:
        """
        specifies if the marks for misspelled text should be displayed.
        
        **since**
        
            OOo 2.0
        """
        ...

    @IsHideSpellMarks.setter
    def IsHideSpellMarks(self, value: bool) -> None:
        ...
    @property
    def LineCount(self) -> int:
        """
        returns the number of lines in the document
        
        Since the document needs to be formatted to get the result obtaining this value may take some time.
        
        Empty paragraphs are not counted.
        
        **since**
        
            OOo 2.0
        """
        ...

    @LineCount.setter
    def LineCount(self, value: int) -> None:
        ...
    @property
    def PageCount(self) -> int:
        """
        returns the number of pages in the document
        
        Since the document needs to be formatted to get the result obtaining this value may take some time.
        
        **since**
        
            OOo 2.0
        """
        ...

    @PageCount.setter
    def PageCount(self, value: int) -> None:
        ...


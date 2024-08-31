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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
if typing.TYPE_CHECKING:
    from ..awt.x_device import XDevice as XDevice_70ba08fc
    from ..i18n.x_forbidden_characters import XForbiddenCharacters as XForbiddenCharacters_df60e2d
    from ..lang.locale import Locale as Locale_70d308fa
    from ..util.date import Date as Date_60040844

class SpreadsheetDocumentSettings(XPropertySet_bc180bfa):
    """
    Service Class

    contributes properties to control the configuration which is global for all views of a spreadsheet document.
    
    **since**
    
        OOo 3.0
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API SpreadsheetDocumentSettings <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1SpreadsheetDocumentSettings.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.SpreadsheetDocumentSettings'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def CalcAsShown(self) -> bool:
        """
        specifies whether calculations are performed with the rounded values displayed in cells (set to TRUE) instead of the internal values (set to FALSE).
        """
        ...

    @abstractproperty
    def CharLocale(self) -> Locale_70d308fa:
        """
        contains the standard document language for Western text.
        """
        ...

    @abstractproperty
    def CharLocaleAsian(self) -> Locale_70d308fa:
        """
        contains the standard document language for Asian text.
        """
        ...

    @abstractproperty
    def CharLocaleComplex(self) -> Locale_70d308fa:
        """
        contains the standard document language for Complex text.
        """
        ...

    @abstractproperty
    def DefaultTabStop(self) -> int:
        """
        specifies the width of default tabulators.
        """
        ...

    @abstractproperty
    def ForbiddenCharacters(self) -> XForbiddenCharacters_df60e2d:
        """
        contains the interface XForbiddenCharacters.
        """
        ...

    @abstractproperty
    def HasDrawPages(self) -> bool:
        """
        If this property is set the document has DrawPages.
        
        Use this property to find out, whether the document has DrawPages or not, because the getDrawPage method on the XDrawPageSupplier and the getDrawPages method on the XDrawPagesSupplier always creates the DrawPages if there are none; and this is very slow and needs more memory.
        """
        ...

    @abstractproperty
    def IgnoreCase(self) -> bool:
        """
        specifies whether upper and lower cases are treated as equal when comparing cells.
        """
        ...

    @abstractproperty
    def IsAdjustHeightEnabled(self) -> bool:
        """
        specifies whether the automatic adjustment of the row height is enabled.
        
        This boolean is actually a counter internally, of the number of times something has locked the height, so setting it to false will only perform one unlock operation, and might leave it still locked
        
        **since**
        
            OOo 3.0
        """
        ...

    @abstractproperty
    def IsExecuteLinkEnabled(self) -> bool:
        """
        specifies whether the automatic execution of links is enabled.
        
        **since**
        
            OOo 3.0
        """
        ...

    @abstractproperty
    def IsIterationEnabled(self) -> bool:
        """
        enables iterated calculation of circular references.
        """
        ...

    @abstractproperty
    def IsLoaded(self) -> bool:
        """
        specifies whether the document data are already loaded.
        
        **since**
        
            OOo 3.0
        """
        ...

    @abstractproperty
    def IsRecordChangesProtected(self) -> bool:
        """
        specifies whether changes record is protected.
        
        **since**
        
            LibreOffice 5.0
        """
        ...

    @abstractproperty
    def IsUndoEnabled(self) -> bool:
        """
        specifies whether the undo command is enabled.
        
        **since**
        
            OOo 3.0
        """
        ...

    @abstractproperty
    def IterationCount(self) -> int:
        """
        specifies how many iterations are carried out.
        
        This setting is only used, if iteration is enabled using SpreadsheetDocumentSettings.IsIterationEnabled.
        """
        ...

    @abstractproperty
    def IterationEpsilon(self) -> float:
        """
        specifies the point at which a change in results will stop the iteration.
        
        More exactly it specifies a difference in the change of the result between two iterations. If the result difference is less than or equal to this epsilon-value, the iteration is stopped.
        
        This setting is only used, if iteration is enabled using SpreadsheetDocumentSettings.IsIterationEnabled.
        """
        ...

    @abstractproperty
    def LookUpLabels(self) -> bool:
        """
        specifies whether column or row labels are looked up from anywhere on the sheet.
        
        Explicitly defined label ranges are used even if this property is set to FALSE.
        """
        ...

    @abstractproperty
    def MatchWholeCell(self) -> bool:
        """
        specifies whether filter criteria must match entire cell contents.
        """
        ...

    @abstractproperty
    def NullDate(self) -> Date_60040844:
        """
        specifies the date that is represented by the value zero.
        """
        ...

    @abstractproperty
    def RecordChanges(self) -> bool:
        """
        specifies whether changes record is enabled.
        
        No modification applied if the record changes protection is activated information given by SpreadsheetDocumentSettings.IsRecordChangesProtected
        
        **since**
        
            LibreOffice 5.0
        """
        ...

    @abstractproperty
    def ReferenceDevice(self) -> XDevice_70ba08fc:
        """
        contains the reference device used for formatting the document.
        
        **since**
        
            OOo 3.0
        """
        ...

    @abstractproperty
    def RegularExpressions(self) -> bool:
        """
        specifies whether regular expressions in formulas are enabled, e.g., for functions which look up spreadsheet contents.
        
        RegularExpressions and Wildcards are mutually exclusive, only one can have the value TRUE. If both are set to TRUE via API calls then the last one set takes precedence.
        """
        ...

    @abstractproperty
    def SpellOnline(self) -> bool:
        """
        enables online spell checking.
        """
        ...

    @abstractproperty
    def StandardDecimals(self) -> int:
        """
        specifies the number of decimals in the default number format.
        """
        ...

    @abstractproperty
    def Wildcards(self) -> bool:
        """
        specifies whether wildcards in formulas are enabled, e.g., for functions which look up spreadsheet contents.
        
        Wildcards and RegularExpressions are mutually exclusive, only one can have the value TRUE. If both are set to TRUE via API calls then the last one set takes precedence.
        
        **since**
        
            LibreOffice 5.2
        """
        ...


__all__ = ['SpreadsheetDocumentSettings']


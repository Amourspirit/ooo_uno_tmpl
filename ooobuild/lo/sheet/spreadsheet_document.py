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
# Namespace: com.sun.star.sheet
import typing
from abc import abstractproperty
from ..document.office_document import OfficeDocument as OfficeDocument_fecd0df2
from ..document.x_action_lockable import XActionLockable as XActionLockable_cb30e3a
from ..document.x_link_target_supplier import XLinkTargetSupplier as XLinkTargetSupplier_4ac21008
from ..drawing.x_draw_pages_supplier import XDrawPagesSupplier as XDrawPagesSupplier_29650f1e
from ..frame.x_model import XModel as XModel_7a6e095c
from ..lang.x_multi_service_factory import XMultiServiceFactory as XMultiServiceFactory_191e0eb6
from .spreadsheet_document_settings import SpreadsheetDocumentSettings as SpreadsheetDocumentSettings_a1641229
from .x_calculatable import XCalculatable as XCalculatable_c7b30c36
from .x_consolidatable import XConsolidatable as XConsolidatable_e2930d1d
from .x_document_auditing import XDocumentAuditing as XDocumentAuditing_fd650ded
from .x_goal_seek import XGoalSeek as XGoalSeek_99130a84
from .x_spreadsheet_document import XSpreadsheetDocument as XSpreadsheetDocument_2a1f0f30
from ..style.x_style_families_supplier import XStyleFamiliesSupplier as XStyleFamiliesSupplier_4c5a1020
from ..util.x_number_formats_supplier import XNumberFormatsSupplier as XNumberFormatsSupplier_3afb0fb7
from ..util.x_protectable import XProtectable as XProtectable_b17f0b93
if typing.TYPE_CHECKING:
    from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6
    from .x_area_links import XAreaLinks as XAreaLinks_a3ce0af3
    from .x_database_ranges import XDatabaseRanges as XDatabaseRanges_e0690cee
    from .x_label_ranges import XLabelRanges as XLabelRanges_bac20bb9
    from .x_named_ranges import XNamedRanges as XNamedRanges_bb030bbe

class SpreadsheetDocument(OfficeDocument_fecd0df2, SpreadsheetDocumentSettings_a1641229, XActionLockable_cb30e3a, XLinkTargetSupplier_4ac21008, XDrawPagesSupplier_29650f1e, XModel_7a6e095c, XMultiServiceFactory_191e0eb6, XCalculatable_c7b30c36, XConsolidatable_e2930d1d, XDocumentAuditing_fd650ded, XGoalSeek_99130a84, XSpreadsheetDocument_2a1f0f30, XStyleFamiliesSupplier_4c5a1020, XNumberFormatsSupplier_3afb0fb7, XProtectable_b17f0b93):
    """
    Service Class

    represents a model component which consists of some settings and one or more spreadsheets.

    See Also:
        `API SpreadsheetDocument <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1SpreadsheetDocument.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.SpreadsheetDocument'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def AreaLinks(self) -> 'XAreaLinks_a3ce0af3':
        """
        contains the collection of area links in the document.
        """

    @abstractproperty
    def ColumnLabelRanges(self) -> 'XLabelRanges_bac20bb9':
        """
        contains the collection of column label ranges in the document.
        """

    @abstractproperty
    def DDELinks(self) -> 'XNameAccess_e2ab0cf6':
        """
        contains the collection of DDE links in the document.
        """

    @abstractproperty
    def DatabaseRanges(self) -> 'XDatabaseRanges_e0690cee':
        """
        contains the collection of database ranges in the document.
        """

    @abstractproperty
    def NamedRanges(self) -> 'XNamedRanges_bb030bbe':
        """
        contains the collection of named ranges in the document.
        """

    @abstractproperty
    def RowLabelRanges(self) -> 'XLabelRanges_bac20bb9':
        """
        contains the collection of row label ranges in the document.
        """

    @abstractproperty
    def SheetLinks(self) -> 'XNameAccess_e2ab0cf6':
        """
        contains the collection of sheet links in the document.
        """



__all__ = ['SpreadsheetDocument']

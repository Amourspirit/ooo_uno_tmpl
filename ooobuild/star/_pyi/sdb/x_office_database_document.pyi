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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sdb
from typing_extensions import Literal
import typing
from ..document.x_document_sub_storage_supplier import XDocumentSubStorageSupplier as XDocumentSubStorageSupplier_da021351
from .x_form_documents_supplier import XFormDocumentsSupplier as XFormDocumentsSupplier_27dc0f33
from .x_report_documents_supplier import XReportDocumentsSupplier as XReportDocumentsSupplier_490a101b
if typing.TYPE_CHECKING:
    from ..sdbc.x_data_source import XDataSource as XDataSource_a2990ae7

class XOfficeDatabaseDocument(XDocumentSubStorageSupplier_da021351, XFormDocumentsSupplier_27dc0f33, XReportDocumentsSupplier_490a101b):
    """
    simplifies the accessing of data sources, and it's corresponding database document and forms, and reports.

    See Also:
        `API XOfficeDatabaseDocument <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1XOfficeDatabaseDocument.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sdb.XOfficeDatabaseDocument']

    @property
    def DataSource(self) -> 'XDataSource_a2990ae7':
        """
        provides access to the one and only DataSource associated with this document
        """



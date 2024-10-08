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
import warnings
warnings.filterwarnings('module')
warnings.warn('The csslo namespace is deprecated. Use lo instead.', DeprecationWarning, stacklevel=2)
from ....lo.sdb.application.copy_table_continuation import CopyTableContinuation as CopyTableContinuation
from ....lo.sdb.application.copy_table_operation import CopyTableOperation as CopyTableOperation
from ....lo.sdb.application.copy_table_row_event import CopyTableRowEvent as CopyTableRowEvent
from ....lo.sdb.application.copy_table_wizard import CopyTableWizard as CopyTableWizard
from ....lo.sdb.application.database_object import DatabaseObject as DatabaseObject
from ....lo.sdb.application.database_object_container import DatabaseObjectContainer as DatabaseObjectContainer
from ....lo.sdb.application.default_view_controller import DefaultViewController as DefaultViewController
from ....lo.sdb.application.named_database_object import NamedDatabaseObject as NamedDatabaseObject
from ....lo.sdb.application.x_copy_table_listener import XCopyTableListener as XCopyTableListener
from ....lo.sdb.application.x_copy_table_wizard import XCopyTableWizard as XCopyTableWizard
from ....lo.sdb.application.x_database_document_ui import XDatabaseDocumentUI as XDatabaseDocumentUI
from ....lo.sdb.application.x_table_ui_provider import XTableUIProvider as XTableUIProvider

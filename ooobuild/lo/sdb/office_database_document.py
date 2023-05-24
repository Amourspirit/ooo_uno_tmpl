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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdb
from __future__ import annotations
from ..document.office_document import OfficeDocument as OfficeDocument_fecd0df2
from ..frame.x_loadable import XLoadable as XLoadable_989a0a7f
from ..script.provider.x_script_provider_supplier import XScriptProviderSupplier as XScriptProviderSupplier_194514a2
from .x_office_database_document import XOfficeDatabaseDocument as XOfficeDatabaseDocument_327f0f39
from ..util.x_closeable import XCloseable as XCloseable_99ee0aa8

class OfficeDatabaseDocument(OfficeDocument_fecd0df2, XLoadable_989a0a7f, XScriptProviderSupplier_194514a2, XOfficeDatabaseDocument_327f0f39, XCloseable_99ee0aa8):
    """
    Service Class

    specifies an office database document which is a storable document.
    
    These documents contain information about forms, and reports, and the properties of a data source.
    
    The database document contains no data per default. The following is stored inside the document:
    
    **since**
    
        OOo 2.0

    See Also:
        `API OfficeDatabaseDocument <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1OfficeDatabaseDocument.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.OfficeDatabaseDocument'
    __ooo_type_name__: str = 'service'


__all__ = ['OfficeDatabaseDocument']


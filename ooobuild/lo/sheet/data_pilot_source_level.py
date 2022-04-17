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
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..container.x_named import XNamed as XNamed_a6520b08
from .x_data_pilot_member_results import XDataPilotMemberResults as XDataPilotMemberResults_56421045
from .x_members_supplier import XMembersSupplier as XMembersSupplier_efd10d98
if typing.TYPE_CHECKING:
    from .general_function import GeneralFunction as GeneralFunction_e2280d25

class DataPilotSourceLevel(XPropertySet_bc180bfa, XNamed_a6520b08, XDataPilotMemberResults_56421045, XMembersSupplier_efd10d98):
    """
    Service Class

    represents a level in a data pilot source hierarchy.
    
    **since**
    
        LibreOffice 5.3

    See Also:
        `API DataPilotSourceLevel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1DataPilotSourceLevel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DataPilotSourceLevel'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def SubTotals(self) -> 'typing.Tuple[GeneralFunction_e2280d25, ...]':
        """
        specifies the subtotals that are inserted for the level.
        
        The subtotals are calculated with the members of this level.
        """

    @abstractproperty
    def SubTotals2(self) -> 'typing.Tuple[int, ...]':
        """
        specifies the subtotals that are inserted for the level.
        
        The subtotals are calculated with the members of this level.
        
        **since**
        
            LibreOffice 5.3
        """

    @abstractproperty
    def ShowEmpty(self) -> bool:
        """
        specifies whether empty members are shown.
        """



__all__ = ['DataPilotSourceLevel']


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
# Namespace: com.sun.star.scanner
from typing_extensions import Literal
import typing
from .x_scanner_manager import XScannerManager as XScannerManager_fd640dcf
if typing.TYPE_CHECKING:
    from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a

class XScannerManager2(XScannerManager_fd640dcf):
    """
    Extension of XScannerManager.
    
    **since**
    
        LibreOffice 3.5

    See Also:
        `API XScannerManager2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1scanner_1_1XScannerManager2.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.scanner.XScannerManager2']

    def configureScannerAndScan(self, scannerContext: object, listener: 'XEventListener_c7230c4a') -> bool:
        """
        produce some kind of User Interface to let the user have a preview, configure the scan area, etc., it, and scan it returns FALSE if user cancelled this process

        Raises:
            com.sun.star.scanner.ScannerException: ``ScannerException``
        """


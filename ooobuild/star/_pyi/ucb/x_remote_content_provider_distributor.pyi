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
# Namespace: com.sun.star.ucb
from typing_extensions import Literal
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XRemoteContentProviderDistributor(XInterface_8f010a43):
    """
    Distribute a content broker to various XRemoteContentProviderAcceptors.

    See Also:
        `API XRemoteContentProviderDistributor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XRemoteContentProviderDistributor.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.ucb.XRemoteContentProviderDistributor']

    def connectToRemoteAcceptor(self, Url: str, Identifier: str) -> bool:
        """
        Offer the local content broker to a remote content provider acceptor.
        
        The Uno Url is handed to the com.sun.star.bridge.UnoUrlResolver service, which is responsible for raising any of the advertised exceptions.

        Raises:
            com.sun.star.connection.NoConnectException: ``NoConnectException``
            com.sun.star.connection.ConnectionSetupException: ``ConnectionSetupException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def disconnectFromAll(self) -> None:
        """
        Undo the offering of the local content broker to all remote content provider acceptors.
        """
    def disconnectFromRemoteAcceptor(self, Url: str) -> bool:
        """
        Undo the offering of the local content broker to a specific remote content provider acceptor.
        """


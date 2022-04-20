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
# Namespace: com.sun.star.io
from typing_extensions import Literal
from abc import ABC

class XAsyncOutputMonitor(ABC):
    """
    An optional companion interface to com.sun.star.io.XOutputStream that supports scenarios where com.sun.star.io.XOutputStream.writeBytes() operates asynchronously and does not necessarily report any errors.
    
    A typical scenario where this interface is useful is when an com.sun.star.io.XOutputStream is used to write to a file via NFS. Normally, any calls to com.sun.star.io.XOutputStream.writeBytes() will execute asynchronously then, in that any potential errors might only be reported by later calls to com.sun.star.io.XOutputStream.writeBytes() or com.sun.star.io.XOutputStream.closeOutput(). If such an output stream shall not be closed immediately after one or more calls to com.sun.star.io.XOutputStream.writeBytes(), but the client wants to know as soon as possible whether writing was successful, then com.sun.star.io.XAsyncOutputMonitor.waitForCompletion() should be called after the series of calls to com.sun.star.io.XOutputStream.writeBytes().
    
    **since**
    
        OOo 2.0

    See Also:
        `API XAsyncOutputMonitor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XAsyncOutputMonitor.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.io.XAsyncOutputMonitor']

    def waitForCompletion(self) -> None:
        """
        waits for the completion of any previous calls to com.sun.star.io.XOutputStream.writeBytes(), and reports potentially pending errors.
        
        Calling this method is potentially expensive (even if the associated com.sun.star.io.XOutputStream represents a local file not accessed via NFS, for example). This method has a similar description to com.sun.star.io.XOutputStream.flush(). However, where the semantics of flush are rather vague, waitForCompletion has very specific semantics—it just blocks long enough so that any errors encountered during previous calls to com.sun.star.io.XOutputStream.writeBytes() can reliably be reported. It specifically does not guarantee that any data have safely been stored on a stable physical medium, like a hard disk (and it is completely unspecified whether flush should give this guarantee).

        Raises:
            IOException: ``IOException``
        """


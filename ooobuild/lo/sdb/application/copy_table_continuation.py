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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.sdb.application


class CopyTableContinuation(object):
    """
    Const Class

    specifies the possible continuations when copying a table row via a CopyTableWizard failed.

    See Also:
        `API CopyTableContinuation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sdb_1_1application_1_1CopyTableContinuation.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb.application'
    __ooo_full_ns__: str = 'com.sun.star.sdb.application.CopyTableContinuation'
    __ooo_type_name__: str = 'const'

    Proceed = 0
    """
    indicates the error should be ignored, and copying should be continued.
    """
    CallNextHandler = 1
    """
    is used to indicate the next registered XCopyTableListener should be called.
    """
    Cancel = 2
    """
    cancels the whole copying process
    """
    AskUser = 3
    """
    asks the user how the handle the error.
    
    The user can choose between ignoring the error and canceling the copy operation.
    """

__all__ = ['CopyTableContinuation']

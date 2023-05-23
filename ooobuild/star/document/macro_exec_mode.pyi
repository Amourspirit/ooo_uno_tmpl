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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.document
import typing


class MacroExecMode:
    """
    Const

    Specify whether a macro can be executed.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API MacroExecMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1document_1_1MacroExecMode.html>`_
    """
    NEVER_EXECUTE: int = ...
    """
    A macro should not be executed at all.
    """
    FROM_LIST: int = ...
    """
    Execute macros from secure list quietly.
    
    If a macro is not in the list a confirmation for it executing will appear.
    """
    ALWAYS_EXECUTE: int = ...
    """
    Execute any macro, macros signed with trusted certificates and macros from secure list are executed quietly.
    
    If the macro is neither in secure list nor signed a conformation will be requested.
    """
    USE_CONFIG: int = ...
    """
    Use configuration to retrieve macro settings.
    
    In case a user confirmation is required a dialog is output.
    """
    ALWAYS_EXECUTE_NO_WARN: int = ...
    """
    A macro should be executed always no conformation should be provided.
    """
    USE_CONFIG_REJECT_CONFIRMATION: int = ...
    """
    Use configuration to retrieve macro settings.
    
    Treat cases when user confirmation required as rejected.
    """
    USE_CONFIG_APPROVE_CONFIRMATION: int = ...
    """
    Use configuration to retrieve macro settings.
    
    Treat cases when user confirmation required as approved.
    """
    FROM_LIST_NO_WARN: int = ...
    """
    Execute only macros from secure list.
    
    Macros that are not from the list are not executed.
    """
    FROM_LIST_AND_SIGNED_WARN: int = ...
    """
    Execute only macros from secure list or macros that are signed by trusted certificates.
    
    If the macro is neither in secure list nor signed it will not be executed.
    
    If the macro is signed with unknown certificate a warning will appear. The macro either will not be executed or if the warning allows conformation, it will be executed after user agrees.
    """
    FROM_LIST_AND_SIGNED_NO_WARN: int = ...
    """
    Execute only macros from secure list or macros that are signed by trusted certificates.
    
    No warning/conformation should be shown.
    """

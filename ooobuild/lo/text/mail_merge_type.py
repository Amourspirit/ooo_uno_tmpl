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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.text


class MailMergeType(object):
    """
    Const Class

    Defines the possible output types/devices for mail merge.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API MailMergeType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1MailMergeType.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.MailMergeType'
    __ooo_type_name__: str = 'const'

    PRINTER = 1
    """
    The output device is a printer.
    """
    FILE = 2
    """
    The output device is a file.
    """
    MAIL = 3
    """
    The output is sent as e-Mail.
    """
    SHELL = 4
    """
    The output is a document shell.
    
    The successful mail merge returns a XTextDocument based component.
    
    **since**
    
        LibreOffice 4.4
    """

__all__ = ['MailMergeType']

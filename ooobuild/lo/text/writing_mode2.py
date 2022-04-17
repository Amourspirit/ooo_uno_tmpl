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
# Libre Office Version: 7.3
# Namespace: com.sun.star.text


class WritingMode2(object):
    """
    Const Class

    this set of constants describes different writing directions
    
    In addition to numerous explicit writing directions, it allows to specify to take the writing direction from the object's context.
    
    **since**
    
        LibreOffice 6.3

    See Also:
        `API WritingMode2 <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1WritingMode2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.WritingMode2'
    __ooo_type_name__: str = 'const'

    LR_TB = 0
    """
    text within lines is written left-to-right.
    
    Lines and blocks are placed top-to-bottom.
    
    Typically, this is the writing mode for normal \"alphabetic\" text.
    """
    RL_TB = 1
    """
    text within a line are written right-to-left.
    
    Lines and blocks are placed top-to-bottom.
    
    Typically, this writing mode is used in Arabic and Hebrew text.
    """
    TB_RL = 2
    """
    text within a line is written top-to-bottom.
    
    Lines and blocks are placed right-to-left.
    
    Typically, this writing mode is used in Chinese and Japanese text.
    """
    TB_LR = 3
    """
    text within a line is written top-to-bottom.
    
    Lines and blocks are placed left-to-right.
    
    Typically, this writing mode is used in Mongolian text.
    """
    PAGE = 4
    """
    obtain writing mode from the current page.
    
    May not be used in page styles.
    """
    CONTEXT = 4
    """
    obtain actual writing mode from the context of the object.
    """
    BT_LR = 5
    """
    text within a line is written bottom-to-top.
    
    Lines and blocks are placed left-to-right.
    
    **since**
    
        LibreOffice 6.3
    """

__all__ = ['WritingMode2']

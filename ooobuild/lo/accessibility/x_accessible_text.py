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
# Libre Office Version: 7.3
# Namespace: com.sun.star.accessibility
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .accessible_scroll_type import AccessibleScrollType as AccessibleScrollType_b426126f
    from .text_segment import TextSegment as TextSegment_1e5b0ee8
    from ..awt.point import Point as Point_5fb2085e
    from ..awt.rectangle import Rectangle as Rectangle_84b109e9
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73

class XAccessibleText(XInterface_8f010a43):
    """
    Implement this interface to give read-only access to a text.
    
    The XAccessibleText interface should be implemented by all UNO components that present textual information on the display like buttons, text entry fields, or text portions of the document window. The interface provides access to the text's content, attributes, and spatial location. However, text can not be modified with this interface. That is the task of the XAccessibleEditableText interface.
    
    The text length, i.e. the number of characters in the text, is returned by XAccessibleText.getCharacterCount(). All methods that operate on particular characters (e.g. XAccessibleText.getCharacterAt()) use character indices from 0 to length-1. All methods that operate on character positions (e.g. XAccessibleText.getTextRange()) use indices from 0 to length.
    
    Please note that accessible text does not necessarily support selection. In this case it should behave as if there where no selection. An empty selection is used for example to express the current cursor position.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XAccessibleText <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1accessibility_1_1XAccessibleText.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.accessibility'
    __ooo_full_ns__: str = 'com.sun.star.accessibility.XAccessibleText'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.accessibility.XAccessibleText'

    @abstractmethod
    def copyText(self, nStartIndex: int, nEndIndex: int) -> bool:
        """
        Copy the specified text into the clipboard.
        
        Copy the specified text into the clipboard. The text that is copied is the same text that would have been selected by the XAccessibleText.getTextRange() method.
        
        The other clipboard related methods XAccessibleEditableText.cutText() and XAccessibleEditableText.deleteText() can be found in the XAccessibleEditableText because of their destructive nature.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def getCaretPosition(self) -> int:
        """
        Return the position of the caret.
        
        Returns the offset of the caret. The caret is often called text cursor. The caret is actually the position between two characters. Its position/offset is that of the character to the right of it.
        """
    @abstractmethod
    def getCharacter(self, nIndex: int) -> str:
        """
        Return the character at the specified position.
        
        Returns the character at the given index.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def getCharacterAttributes(self, nIndex: int, aRequestedAttributes: 'typing.Tuple[str, ...]') -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        Get the attribute set for the specified position.
        
        Returns a set of attributes that are associated for the character at the given index. To prevent the method from returning possibly large sets of attributes that the caller is not interested in the caller has to provide a list of attributes that he wants to be returned.
        
        An empty sequence signals the callers interest in all the attributes. This is useful in two cases: a) Simply as a way to avoid passing a potentially large array to the called object or b) when the caller does not know what attributes the called objects supports but is interested in all of them nevertheless.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
        """
    @abstractmethod
    def getCharacterBounds(self, nIndex: int) -> 'Rectangle_84b109e9':
        """
        Return the bounding box of the specified position.
        
        Returns the bounding box of the indexed character.
        
        The virtual character after the last character of the represented text, i.e. the one at position length is a special case. It represents the current input position and will therefore typically be queried by AT more often than other positions. Because it does not represent an existing character its bounding box is defined in relation to preceding characters. It should be roughly equivalent to the bounding box of some character when inserted at the end of the text. Its height typically being the maximal height of all the characters in the text or the height of the preceding character, its width being at least one pixel so that the bounding box is not degenerate.Note that the index \"length\" is not always valid. Whether it is or not is implementation dependent. It typically is when text is editable or otherwise when on the screen the caret can be placed behind the text. You can be sure that the index is valid after you have received an AccessibleEventId.CARET event for this index.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def getCharacterCount(self) -> int:
        """
        Return the number of characters in the represented text.
        
        Returns the number of characters in the text represented by this object or, in other words, the text length.
        """
    @abstractmethod
    def getIndexAtPoint(self, aPoint: 'Point_5fb2085e') -> int:
        """
        Return the text position for the specified screen position.
        
        Given a point in local coordinates, i.e. relative to the coordinate system of the object, return the zero-based index of the character under that point. The same functionality could be achieved by using the bounding boxes for each character as returned by XAccessibleText.getCharacterBounds(). The method XAccessibleText.getIndexAtPoint(), however, can be implemented in a more efficient way.
        """
    @abstractmethod
    def getSelectedText(self) -> str:
        """
        Return the selected text.
        
        Returns the portion of the text that is selected.
        """
    @abstractmethod
    def getSelectionEnd(self) -> int:
        """
        Return the position of the end of the selection.
        
        Returns the index of the end of the selected text.
        """
    @abstractmethod
    def getSelectionStart(self) -> int:
        """
        Return the position of the start of the selection.
        
        Returns the index of the start of the selected text.
        """
    @abstractmethod
    def getText(self) -> str:
        """
        Return the whole text.
        
        Returns the complete text. This is equivalent to a call to XAccessibleText.getTextRange() with the arguments zero and getCharacterCount()-1.
        """
    @abstractmethod
    def getTextAtIndex(self, nIndex: int, nTextType: int) -> 'TextSegment_1e5b0ee8':
        """
        Get a text portion around the given position.
        
        Returns the substring of the specified text type that contains the character at the given index, if any. For example, given the text type AccessibleTextType.WORD, the word which contains the character at position nIndex is returned, or an empty string if no word is found at the that position.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractmethod
    def getTextBeforeIndex(self, nIndex: int, nTextType: int) -> 'TextSegment_1e5b0ee8':
        """
        Get a text portion before the given position.
        
        Returns the substring of the specified text type that is located before the given character and does not include it. The result of this method should be same as a result for XAccessibleText.getTextAtIndex() with a suitably decreased index value.
        
        For example, if text type is AccessibleTextType.WORD, then the complete word that is closest to and located before nIndex is returned.
        
        If the index is valid, but no suitable word (or other text type) is found, an empty text segment is returned.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractmethod
    def getTextBehindIndex(self, nIndex: int, nTextType: int) -> 'TextSegment_1e5b0ee8':
        """
        Get a text portion behind the given position.
        
        Returns the substring of the specified text type that is located after the given character and does not include it. The result of this method should be same as a result for XAccessibleText.getTextAtIndex() with a suitably increased index value.
        
        For example, if text type is AccessibleTextType.WORD, then the complete word that is closest to and located behind nIndex is returned.
        
        If the index is valid, but no suitable word (or other text type) is found, an empty string is returned.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractmethod
    def getTextRange(self, nStartIndex: int, nEndIndex: int) -> str:
        """
        Return the specified text range.
        
        Returns the substring between the two given indices.
        
        The substring starts with the character at nStartIndex (inclusive) and up to the character at nEndIndex (exclusive), if nStartIndex is less or equal nEndIndex. If nEndIndex is lower than nStartIndex, the result is the same as a call with the two arguments being exchanged.
        
        The whole text can be requested by passing the indices zero and getCharacterCount(). If both indices have the same value, an empty string is returned.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def scrollSubstringTo(self, nStartIndex: int, nEndIndex: int, aScrollType: 'AccessibleScrollType_b426126f') -> bool:
        """
        Scroll the specified text to make it visible on screen.
        
        **since**
        
            LibreOffice 7.0

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def setCaretPosition(self, nIndex: int) -> bool:
        """
        Set the position of the caret.
        
        The caret is often called text cursor. The caret is actually the position between two characters. Its position/offset is that of the character to the right of it.
        
        Setting the caret position may or may not alter the current selection. A change of the selection is notified to the accessibility event listeners with an AccessibleEventId.ACCESSIBLE_SELECTION_EVENT.
        
        When the new caret position differs from the old one (which, of course, is the standard case) this is notified to the accessibility event listeners with an AccessibleEventId.ACCESSIBLE_CARET_EVENT.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @abstractmethod
    def setSelection(self, nStartIndex: int, nEndIndex: int) -> bool:
        """
        Set a new selection.
        
        Sets the selected text portion according to the given indices. The old selection is replaced by the new selection.
        
        The selection encompasses the same string of text that XAccessibleText.getTextRange() would have selected. See there for details.
        
        Setting the selection may or may not change the caret position. Typically the caret is moved to the position after the second argument. When the caret is moved this is notified to the accessibility event listeners with an AccessibleEventId.ACCESSIBLE_CARET_EVENT.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """

__all__ = ['XAccessibleText']


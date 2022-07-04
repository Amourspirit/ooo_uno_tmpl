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
# Namespace: com.sun.star.document
from typing_extensions import Literal
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from ..beans.named_value import NamedValue as NamedValue_a37a0af3
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..beans.x_property_container import XPropertyContainer as XPropertyContainer_c600e71
    from ..embed.x_storage import XStorage as XStorage_8e460a32
    from ..lang.locale import Locale as Locale_70d308fa
    from ..util.date_time import DateTime as DateTime_84de09d3

class XDocumentProperties(ABC):
    """
    provides document-specific information such as the author, creation date, and user-defined fields.
    
    This interface manages access to document meta-data properties. Such properties may be set from the outside via the setter methods (e.g. when importing arbitrary document formats that support document properties), or imported from an ODF package via the methods loadFromStorage() and loadFromMedium(). The properties may also be stored via the methods storeToStorage() and storeToMedium().
    
    **since**
    
        OOo 3.0

    See Also:
        `API XDocumentProperties <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XDocumentProperties.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.document.XDocumentProperties']

    def getUserDefinedProperties(self) -> 'XPropertyContainer_c600e71':
        """
        provides access to a container for user-defined properties.
        
        The returned object also implements the interface com.sun.star.beans.XPropertySet.
        """
        ...
    def loadFromMedium(self, URL: str, Medium: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        loads document properties from an ODF package or an OLE container.
        
        The URL could be part of the Medium parameter, but because often no other parameters except the URL are needed, providing it separately was added for convenience.

        Raises:
            com.sun.star.io.WrongFormatException: ``WrongFormatException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    def loadFromStorage(self, Storage: 'XStorage_8e460a32', Medium: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        loads document properties from an ODF package.
        
        This method is used for accessing an ODF package that is owned by someone else, e.g., a document.
        
        This is unfortunately necessary in order to properly resolve relative URLs in the meta-data.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.io.WrongFormatException: ``WrongFormatException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    def resetUserData(self, Author: str) -> None:
        """
        resets all attributes that could identify the user.
        
        Clears the document properties, such that it appears the document has just been created. This is a convenience method which resets several attributes at once, as follows:
        """
        ...
    def storeToMedium(self, URL: str, Medium: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        stores document properties to an ODF package or an OLE container.
        
        The URL could be part of the Medium parameter, but because often no other parameters except the URL are needed, providing it separately was added for convenience.

        Raises:
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    def storeToStorage(self, Storage: 'XStorage_8e460a32', Medium: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        stores document properties to an ODF package.
        
        This method is used for accessing an ODF package that is owned by someone else, e.g., a document. Note that the implementation may choose to store the meta-data in either OOo or ODF format, depending on the MediaType property of the given Storage argument.
        
        This is unfortunately necessary in order to properly resolve relative URLs in the meta-data.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
            com.sun.star.io.IOException: ``IOException``
        """
        ...

    @property
    def DocumentStatistics(self) -> 'typing.Tuple[NamedValue_a37a0af3, ...]':
        """
        contains some statistics about the document.
        
        The contained statistics may be specific to the type of the document.
        """
        ...

    @property
    def Keywords(self) -> 'typing.Tuple[str, ...]':
        """
        contains a list of keywords for the document.
        """
        ...

    @property
    def Author(self) -> str:
        """
        contains the initial author of the document.
        """
        ...

    @property
    def AutoloadSecs(self) -> int:
        """
        contains the number of seconds after which a specified URL is to be loaded after the document is loaded into a desktop frame.
        
        A value of 0 is valid and describes a redirection. A value of 0 together with an empty string as AutoloadURL describes a case where no autoload is specified.
        """
        ...

    @property
    def AutoloadURL(self) -> str:
        """
        contains the URL to load automatically at a specified time after the document is loaded into a desktop frame.
        
        An empty URL is valid and describes a case where the document shall be reloaded from its original location after some time described by the attribute AutoloadSecs. An empty string together with an AutoloadSecs value of 0 describes a case where no autoload is specified.
        """
        ...

    @property
    def CreationDate(self) -> 'DateTime_84de09d3':
        """
        contains the date and time when the document was created.
        """
        ...

    @property
    def DefaultTarget(self) -> str:
        """
        contains the name of the default frame into which links should be loaded if no target is specified.
        
        This applies to the autoload feature too, but to others as well.
        """
        ...

    @property
    def Description(self) -> str:
        """
        contains a multi-line comment describing the document.
        
        Line delimiters can be UNIX, Macintosh or DOS style.
        """
        ...

    @property
    def EditingCycles(self) -> int:
        """
        describes how often the document was edited and saved.
        """
        ...

    @property
    def EditingDuration(self) -> int:
        """
        contains the net time of editing the document (in seconds).
        """
        ...

    @property
    def Generator(self) -> str:
        """
        identifies which application was used to create or last modify the document.
        
        The generating application will set this attribute when it creates a new document or it saves a document. When a document is loaded that itself contains such an attribute it will be preserved until the document is saved again.
        """
        ...

    @property
    def Language(self) -> 'Locale_70d308fa':
        """
        contains the default language of the document.
        """
        ...

    @property
    def ModificationDate(self) -> 'DateTime_84de09d3':
        """
        contains the date and time of the last time the document was stored.
        
        If the document has never been stored, contains a default value.
        """
        ...

    @property
    def ModifiedBy(self) -> str:
        """
        contains the name of the person who most recently stored the document.
        """
        ...

    @property
    def PrintDate(self) -> 'DateTime_84de09d3':
        """
        contains the date and time when the document was last printed.
        
        If the document has never been printed, contains a default value.
        """
        ...

    @property
    def PrintedBy(self) -> str:
        """
        contains the name of the person who most recently printed the document.
        """
        ...

    @property
    def Subject(self) -> str:
        """
        contains the subject of the document.
        """
        ...

    @property
    def TemplateDate(self) -> 'DateTime_84de09d3':
        """
        contains the date and time of when the document was created or updated from the template.
        """
        ...

    @property
    def TemplateName(self) -> str:
        """
        contains the name of the template from which the document was created.
        
        The value is an empty string if the document was not created from a template or if it was detached from the template.
        """
        ...

    @property
    def TemplateURL(self) -> str:
        """
        contains the URL of the template from which the document was created.
        
        The value is an empty string if the document was not created from a template or if it was detached from the template.
        """
        ...

    @property
    def Title(self) -> str:
        """
        contains the title of the document.
        """
        ...



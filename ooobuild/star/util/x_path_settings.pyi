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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.util
from __future__ import annotations
import typing

from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa


class XPathSettings(XPropertySet_bc180bfa):
    """
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API XPathSettings <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XPathSettings.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.util.XPathSettings'

    @property
    def Addin(self) -> str:
        """
        Specifies the directory that contains spreadsheet add-ins which use the old add-in API.
        """
        ...
    @Addin.setter
    def Addin(self, value: str) -> None:
        ...
    @property
    def AutoCorrect(self) -> str:
        """
        The settings of the AutoCorrect dialog.
        
        The value can be more than one path separated by a semicolon.
        """
        ...
    @AutoCorrect.setter
    def AutoCorrect(self, value: str) -> None:
        ...
    @property
    def AutoText(self) -> str:
        """
        The directory which contains the AutoText modules.
        
        The value can be more than one path separated by a semicolon.
        """
        ...
    @AutoText.setter
    def AutoText(self, value: str) -> None:
        ...
    @property
    def Backup(self) -> str:
        """
        Automatic backup copies of documents are stored here.
        """
        ...
    @Backup.setter
    def Backup(self, value: str) -> None:
        ...
    @property
    def BasePathShareLayer(self) -> str:
        """
        """
        ...
    @BasePathShareLayer.setter
    def BasePathShareLayer(self, value: str) -> None:
        ...
    @property
    def BasePathUserLayer(self) -> str:
        """
        """
        ...
    @BasePathUserLayer.setter
    def BasePathUserLayer(self, value: str) -> None:
        ...
    @property
    def Basic(self) -> str:
        """
        The Basic files, used by the AutoPilots, can be found here.
        
        The value can be more than one path separated by a semicolon.
        """
        ...
    @Basic.setter
    def Basic(self, value: str) -> None:
        ...
    @property
    def Bitmap(self) -> str:
        """
        This directory contains the icons for the toolbars.
        """
        ...
    @Bitmap.setter
    def Bitmap(self, value: str) -> None:
        ...
    @property
    def Config(self) -> str:
        """
        The configuration files are located here.
        
        This entry cannot be changed by the user in Office user interface.
        """
        ...
    @Config.setter
    def Config(self, value: str) -> None:
        ...
    @property
    def Dictionary(self) -> str:
        """
        The provided dictionaries are stored here.
        """
        ...
    @Dictionary.setter
    def Dictionary(self, value: str) -> None:
        ...
    @property
    def Favorite(self) -> str:
        """
        Path to save folder bookmarks.
        """
        ...
    @Favorite.setter
    def Favorite(self, value: str) -> None:
        ...
    @property
    def Filter(self) -> str:
        """
        Specifies the directory where all the filters are stored.
        """
        ...
    @Filter.setter
    def Filter(self, value: str) -> None:
        ...
    @property
    def Gallery(self) -> str:
        """
        Specifies the directories which contains the Gallery database and multimedia files.
        
        The value can be more than one path separated by a semicolon.
        """
        ...
    @Gallery.setter
    def Gallery(self, value: str) -> None:
        ...
    @property
    def Graphic(self) -> str:
        """
        This directory is displayed when the dialog for opening a graphic or for saving a new graphic is called.
        """
        ...
    @Graphic.setter
    def Graphic(self, value: str) -> None:
        ...
    @property
    def Help(self) -> str:
        """
        The path to the Office help files.
        """
        ...
    @Help.setter
    def Help(self, value: str) -> None:
        ...
    @property
    def Linguistic(self) -> str:
        """
        The files that are necessary for the spell check are saved here.
        """
        ...
    @Linguistic.setter
    def Linguistic(self, value: str) -> None:
        ...
    @property
    def Module(self) -> str:
        """
        This is the path for the modules.
        """
        ...
    @Module.setter
    def Module(self, value: str) -> None:
        ...
    @property
    def Palette(self) -> str:
        """
        This is the path to the palette files *.SOB to *.SOF containing user-defined colors and patterns.
        
        The value can be more than one path separated by a semicolon.
        """
        ...
    @Palette.setter
    def Palette(self, value: str) -> None:
        ...
    @property
    def Plugin(self) -> str:
        """
        Plugins are saved in these directories.
        
        The value can be more than one path separated by a semicolon.
        """
        ...
    @Plugin.setter
    def Plugin(self, value: str) -> None:
        ...
    @property
    def Storage(self) -> str:
        """
        Mail, News files and other information (for example, about FTP Server) are stored here.
        """
        ...
    @Storage.setter
    def Storage(self, value: str) -> None:
        ...
    @property
    def Temp(self) -> str:
        """
        The base url to the office temp-files.
        """
        ...
    @Temp.setter
    def Temp(self, value: str) -> None:
        ...
    @property
    def Template(self) -> str:
        """
        The templates originate from these folders and sub-folders.
        
        The value can be more than one path separated by a semicolon.
        """
        ...
    @Template.setter
    def Template(self, value: str) -> None:
        ...
    @property
    def UIConfig(self) -> str:
        """
        Global directories to look for user interface configuration files.
        
        The user interface configuration will be merged with user settings stored in the directory specified by UserConfig. The value can be more than one path separated by a semicolon.
        """
        ...
    @UIConfig.setter
    def UIConfig(self, value: str) -> None:
        ...
    @property
    def UserConfig(self) -> str:
        """
        Specifies the folder with the user settings.
        """
        ...
    @UserConfig.setter
    def UserConfig(self, value: str) -> None:
        ...
    @property
    def UserDictionary(self) -> str:
        """
        The custom dictionaries are contained here.
        """
        ...
    @UserDictionary.setter
    def UserDictionary(self, value: str) -> None:
        ...
    @property
    def Work(self) -> str:
        """
        The path of the work folder can be modified according to the user's needs.
        
        The path specified here can be seen in the Open or Save dialog.
        """
        ...
    @Work.setter
    def Work(self, value: str) -> None:
        ...


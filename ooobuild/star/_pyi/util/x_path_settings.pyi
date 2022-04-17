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
# Namespace: com.sun.star.util
from typing_extensions import Literal
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class XPathSettings(XPropertySet_bc180bfa):
    """
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API XPathSettings <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XPathSettings.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.util.XPathSettings']

    @property
    def Addin(self) -> str:
        """
        Specifies the directory that contains spreadsheet add-ins which use the old add-in API.
        """

    @property
    def AutoCorrect(self) -> str:
        """
        The settings of the AutoCorrect dialog.
        
        The value can be more than one path separated by a semicolon.
        """

    @property
    def AutoText(self) -> str:
        """
        The directory which contains the AutoText modules.
        
        The value can be more than one path separated by a semicolon.
        """

    @property
    def Backup(self) -> str:
        """
        Automatic backup copies of documents are stored here.
        """

    @property
    def BasePathShareLayer(self) -> str:
        """
        """

    @property
    def BasePathUserLayer(self) -> str:
        """
        """

    @property
    def Basic(self) -> str:
        """
        The Basic files, used by the AutoPilots, can be found here.
        
        The value can be more than one path separated by a semicolon.
        """

    @property
    def Bitmap(self) -> str:
        """
        This directory contains the icons for the toolbars.
        """

    @property
    def Config(self) -> str:
        """
        The configuration files are located here.
        
        This entry cannot be changed by the user in Office user interface.
        """

    @property
    def Dictionary(self) -> str:
        """
        The provided dictionaries are stored here.
        """

    @property
    def Favorite(self) -> str:
        """
        Path to save folder bookmarks.
        """

    @property
    def Filter(self) -> str:
        """
        Specifies the directory where all the filters are stored.
        """

    @property
    def Gallery(self) -> str:
        """
        Specifies the directories which contains the Gallery database and multimedia files.
        
        The value can be more than one path separated by a semicolon.
        """

    @property
    def Graphic(self) -> str:
        """
        This directory is displayed when the dialog for opening a graphic or for saving a new graphic is called.
        """

    @property
    def Help(self) -> str:
        """
        The path to the Office help files.
        """

    @property
    def Linguistic(self) -> str:
        """
        The files that are necessary for the spell check are saved here.
        """

    @property
    def Module(self) -> str:
        """
        This is the path for the modules.
        """

    @property
    def Palette(self) -> str:
        """
        This is the path to the palette files *.SOB to *.SOF containing user-defined colors and patterns.
        
        The value can be more than one path separated by a semicolon.
        """

    @property
    def Plugin(self) -> str:
        """
        Plugins are saved in these directories.
        
        The value can be more than one path separated by a semicolon.
        """

    @property
    def Storage(self) -> str:
        """
        Mail, News files and other information (for example, about FTP Server) are stored here.
        """

    @property
    def Temp(self) -> str:
        """
        The base url to the office temp-files.
        """

    @property
    def Template(self) -> str:
        """
        The templates originate from these folders and sub-folders.
        
        The value can be more than one path separated by a semicolon.
        """

    @property
    def UIConfig(self) -> str:
        """
        Global directories to look for user interface configuration files.
        
        The user interface configuration will be merged with user settings stored in the directory specified by UserConfig. The value can be more than one path separated by a semicolon.
        """

    @property
    def UserConfig(self) -> str:
        """
        Specifies the folder with the user settings.
        """

    @property
    def UserDictionary(self) -> str:
        """
        The custom dictionaries are contained here.
        """

    @property
    def Work(self) -> str:
        """
        The path of the work folder can be modified according to the user's needs.
        
        The path specified here can be seen in the Open or Save dialog.
        """



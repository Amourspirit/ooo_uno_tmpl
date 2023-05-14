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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.text
from ..document.settings import Settings as Settings_b2bc0bb8
from .print_settings import PrintSettings as PrintSettings_bea20c2b

class DocumentSettings(Settings_b2bc0bb8, PrintSettings_bea20c2b):
    """
    Service Class

    describes properties that apply to the whole text document.
    
    **since**
    
        OOo 2.0

    See Also:
        `API DocumentSettings <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1DocumentSettings.html>`_
    """
    @property
    def AddParaSpacingToTableCells(self) -> bool:
        """
        specifies if paragraph and table spacing is added at the bottom of table cells
        
        This property controls, if the spacing of the last paragraph respectively table of a table cell is added at the bottom of this table cells If TRUE (default for documents since OpenOffice.org 2.0), the spacing of the last paragraph respectively table of a table cell is added at the bottom of this table cell. If FALSE (typically for documents till OpenOffice.org 1.1), the spacing of the last paragraph respectively table of a table cell isn't added at the bottom of this table cell.
        
        **since**
        
            OOo 2.0
        """
        ...
    @AddParaSpacingToTableCells.setter
    def AddParaSpacingToTableCells(self, value: bool) -> None:
        ...
    @property
    def AddParaTableSpacing(self) -> bool:
        """
        specifies if spacing between paragraphs and tables is to be added.
        
        If between two paragraphs, two tables, or a paragraph and a table, you have defined spacing above and below each object, usually only the larger one of the two spaces is used. If the spacing between the objects are to be added this property has to be TRUE.
        """
        ...
    @AddParaTableSpacing.setter
    def AddParaTableSpacing(self, value: bool) -> None:
        ...
    @property
    def AddParaTableSpacingAtStart(self) -> bool:
        """
        specifies if top paragraph spacing is applied to paragraphs on the first page of text documents.
        
        If TRUE, the paragraph or table spacing to the top will also be effective at the beginning of a page or column if the paragraph or table is positioned on the first page of the document. The same applies for a page break.
        """
        ...
    @AddParaTableSpacingAtStart.setter
    def AddParaTableSpacingAtStart(self, value: bool) -> None:
        ...
    @property
    def AlignTabStopPosition(self) -> bool:
        """
        specifies the alignment of tab stops in text documents.
        
        If TRUE centered and right-aligned paragraphs containing tabs are formatted as a whole in the center or aligned to the right. If FALSE, only the text to the right of the last tab, for example, is aligned to the right, while the text to the left remains where it is.
        """
        ...
    @AlignTabStopPosition.setter
    def AlignTabStopPosition(self, value: bool) -> None:
        ...
    @property
    def ChartAutoUpdate(self) -> bool:
        """
        specifies if charts in text documents are updated automatically.
        
        This has no effect if \"FieldAutoUpdate\" is FALSE.
        """
        ...
    @ChartAutoUpdate.setter
    def ChartAutoUpdate(self, value: bool) -> None:
        ...
    @property
    def ConsiderTextWrapOnObjPos(self) -> bool:
        """
        specifies if the text wrap of floating screen objects are considered in a specified way in the positioning algorithm.
        
        This property controls how floating screen objects (Writer fly frames and drawing objects) are positioned. If TRUE, the object positioning algorithm will consider the text wrap style, set at the floating screen object. The attribute BaseFrameProperties.WrapInfluenceOnPosition specifies how the text wrap is considered. If FALSE (default value), the former object positioning algorithm (known from OpenOffice.org 1.1) is applied.
        
        **since**
        
            OOo 2.0
        """
        ...
    @ConsiderTextWrapOnObjPos.setter
    def ConsiderTextWrapOnObjPos(self, value: bool) -> None:
        ...
    @property
    def IsLabelDocument(self) -> bool:
        """
        specifies if the document has been created as a label document.
        
        This property indicates that the document contains multiple text frames and that the content of one frame is duplicated into the other frames by internally linked text sections.
        """
        ...
    @IsLabelDocument.setter
    def IsLabelDocument(self, value: bool) -> None:
        ...
    @property
    def MathBaselineAlignment(self) -> bool:
        """
        specifies if Math objects should automatically vertically aligned to match the baseline of the surrounding text.
        
        If activated formula object that are anchored 'As Character' will be vertically aligned to have their baseline match with the one from the text.
        
        **since**
        
            OOo 3.4
        """
        ...
    @MathBaselineAlignment.setter
    def MathBaselineAlignment(self, value: bool) -> None:
        ...
    @property
    def SaveGlobalDocumentLinks(self) -> bool:
        """
        specifies if the contents of links in the global document are saved or not.
        
        This property applies only for master documents.
        
        Note: This name is a bit misleading, it should be something like SaveLinkedDocumentContent.
        """
        ...
    @SaveGlobalDocumentLinks.setter
    def SaveGlobalDocumentLinks(self, value: bool) -> None:
        ...
    @property
    def UseFormerLineSpacing(self) -> bool:
        """
        specifies if the former (till OpenOffice.org 1.1) or the new line spacing formatting is applied.
        
        This property controls how a set line spacing at a paragraph influences the formatting of the text lines and the spacing between paragraphs. If TRUE, the formatting till OpenOffice.org 1.1 is applied. This means, that a proportional line spacing is applied above and below a text line and that the maximum of the line spacing value between two paragraphs is added respectively reckoned up with the paragraph spacing (adding or reckoning up is controlled by document option AddParaTableSpacing). If FALSE (default for documents since OpenOffice.org 2.0), a proportional line spacing is only applied below a text line and it's always added to the paragraph spacing between two paragraphs.
        
        **since**
        
            OOo 2.0
        """
        ...
    @UseFormerLineSpacing.setter
    def UseFormerLineSpacing(self, value: bool) -> None:
        ...
    @property
    def UseFormerObjectPositioning(self) -> bool:
        """
        specifies if the former (till OpenOffice.org 1.1) or the new object positioning is applied.
        
        This property controls how floating screen objects (Writer fly frames and drawing objects are positioned. If TRUE, the object positioning till OpenOffice.org 1.1 is applied. This means, that the top of a paragraph, at which a floating screen object orients its vertical position, includes the lower spacing and the line spacing of the previous paragraph. If FALSE (default for documents since OpenOffice.org 2.0), the top of a paragraph, at which a floating screen object orients its vertical position, doesn't include the lower spacing and the line spacing of the previous paragraph.
        
        **since**
        
            OOo 2.0
        """
        ...
    @UseFormerObjectPositioning.setter
    def UseFormerObjectPositioning(self, value: bool) -> None:
        ...


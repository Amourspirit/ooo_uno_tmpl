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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.accessibility
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class AccessibleRole(metaclass=UnoConstMeta, type_name="com.sun.star.accessibility.AccessibleRole", name_space="com.sun.star.accessibility"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.accessibility.AccessibleRole``"""
        pass

    class AccessibleRoleEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.accessibility.AccessibleRole", name_space="com.sun.star.accessibility"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.accessibility.AccessibleRole`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.accessibility import AccessibleRole as AccessibleRole
    else:
        # keep document generators happy
        from ...lo.accessibility.accessible_role import AccessibleRole as AccessibleRole

    class AccessibleRoleEnum(IntEnum):
        """
        Enum of Const Class AccessibleRole

        Collection of roles.
        
        This collection of constants defines the set of possible roles of classes implementing the XAccessible interface according to the Java class javax.accessibility.AccessibleRole. The role of an object describes its generic function like \"button\", \"menu\", or \"text\". You can obtain an object's role by calling the getAccessibleRole() method of the XAccessibleContext interface.
        
        We are using constants instead of a more typesafe enum. The reason for this is that IDL enums may not be extended. Therefore, in order to include future extensions to the set of roles we have to use constants here.
        
        For some roles there exist two labels with the same value. Please use the one with the underscores. The other ones are somewhat deprecated and will be removed in the future.
        
        **since**
        
            OOo 1.1.2
        """
        UNKNOWN = AccessibleRole.UNKNOWN
        """
        Unknown role.
        
        The object contains some Accessible information, but its role is not known.
        """
        ALERT = AccessibleRole.ALERT
        """
        Object is used to alert the user about something.
        """
        COLUMN_HEADER = AccessibleRole.COLUMN_HEADER
        """
        The header for a column of data.
        """
        CANVAS = AccessibleRole.CANVAS
        """
        Object that can be drawn into and is used to trap events.
        
        See also FRAME, GLASS_PANE, and LAYERED_PANE.
        """
        CHECK_BOX = AccessibleRole.CHECK_BOX
        """
        Check box role.
        
        A choice that can be checked or unchecked and provides a separate indicator for the current state.
        
        See also PUSH_BUTTON, TOGGLE_BUTTON, and RADIO_BUTTON.
        """
        CHECK_MENU_ITEM = AccessibleRole.CHECK_MENU_ITEM
        """
        This role is used for check buttons that are menu items.
        """
        COLOR_CHOOSER = AccessibleRole.COLOR_CHOOSER
        """
        A specialized dialog that lets the user choose a color.
        """
        COMBO_BOX = AccessibleRole.COMBO_BOX
        """
        Combo box role.
        
        A list of choices the user can select from. Also optionally allows the user to enter a choice of their own.
        """
        DATE_EDITOR = AccessibleRole.DATE_EDITOR
        """
        Date editor role.
        
        A DATE_EDITOR is a component that allows users to edit date and time.
        """
        DESKTOP_ICON = AccessibleRole.DESKTOP_ICON
        """
        An iconified internal frame in a DESKTOP_PANE.
        
        See also DESKTOP_PANE and INTERNAL_FRAME.
        """
        DESKTOP_PANE = AccessibleRole.DESKTOP_PANE
        """
        Desktop pane role.
        
        A pane that supports internal frames and iconified versions of those internal frames.
        """
        DIRECTORY_PANE = AccessibleRole.DIRECTORY_PANE
        """
        Directory pane role.
        
        A pane that allows the user to navigate through and select the contents of a directory. May be used by a file chooser.
        
        See also FILE_CHOOSER.
        """
        DIALOG = AccessibleRole.DIALOG
        """
        Dialog box role.
        
        A top level window with title bar and a border. A dialog is similar to a frame, but it has fewer properties and is often used as a secondary window for an application.
        
        See also FRAME and WINDOW.
        """
        DOCUMENT = AccessibleRole.DOCUMENT
        """
        View of a document.
        
        The view of an actual document. Its content depends on the document type.
        """
        EMBEDDED_OBJECT = AccessibleRole.EMBEDDED_OBJECT
        """
        Embedded (OLE) object.
        """
        END_NOTE = AccessibleRole.END_NOTE
        """
        Text that is used as an endnote (footnote at the end of a chapter or section.
        """
        FILE_CHOOSER = AccessibleRole.FILE_CHOOSER
        """
        File chooser role.
        
        A specialized dialog that displays the files in the directory and lets the user select a file, browse a different directory, or specify a filename. May use the directory pane to show the contents of a directory.
        
        See also DIRECTORY_PANE.
        """
        FILLER = AccessibleRole.FILLER
        """
        Filler role.
        
        An object that fills up space in a user interface. It is often used in interfaces to tweak the spacing between components, but serves no other purpose.
        """
        FONT_CHOOSER = AccessibleRole.FONT_CHOOSER
        """
        Font chooser role.
        
        A FONT_CHOOSER is a component that lets the user pick various attributes for fonts.
        """
        FOOTER = AccessibleRole.FOOTER
        """
        Footer of a document page.
        """
        FOOTNOTE = AccessibleRole.FOOTNOTE
        """
        Text that is used as a footnote.
        """
        FRAME = AccessibleRole.FRAME
        """
        Frame role.
        
        A top level window with a title bar, border, menu bar, etc. It is often used as the primary window for an application.
        
        See also DIALOG, CANVAS, and WINDOW.
        """
        GLASS_PANE = AccessibleRole.GLASS_PANE
        """
        Glass pane role.
        
        A pane that is guaranteed to be painted on top of all panes beneath it.
        
        See also ROOT_PANE and CANVAS.
        """
        GRAPHIC = AccessibleRole.GRAPHIC
        """
        Graphical object.
        """
        GROUP_BOX = AccessibleRole.GROUP_BOX
        """
        Group box role.
        
        A GROUP_BOX is a simple container that contains a border around it and contains components inside it.
        """
        HEADER = AccessibleRole.HEADER
        """
        Header of a document page.
        """
        HEADING = AccessibleRole.HEADING
        """
        Chapter or section heading.
        """
        HYPER_LINK = AccessibleRole.HYPER_LINK
        """
        A hypertext anchor.
        """
        ICON = AccessibleRole.ICON
        """
        A small fixed size picture, typically used to decorate components.
        """
        INTERNAL_FRAME = AccessibleRole.INTERNAL_FRAME
        """
        Internal frame role.
        
        A frame-like object that is clipped by a desktop pane. The desktop pane, internal frame, and desktop icon objects are often used to create multiple document interfaces within an application.
        
        See also DESKTOP_ICON, DESKTOP_PANE, and FRAME.
        """
        LABEL = AccessibleRole.LABEL
        """
        An object used to present an icon or short string in an interface.
        
        See also TEXT and STATIC.
        """
        LAYERED_PANE = AccessibleRole.LAYERED_PANE
        """
        layered pane role.
        
        A specialized pane that allows its children to be drawn in layers, providing a form of stacking order. This is usually the pane that holds the menu bar as well as the pane that contains most of the visual components in a window.
        
        See also GLASS_PANE and ROOT_PANE.
        """
        LIST = AccessibleRole.LIST
        """
        List role.
        
        An object that presents a list of objects to the user and allows the user to select one or more of them. A list is usually contained within a scroll pane.
        
        See also SCROLL_PANE and LIST_ITEM.
        """
        LIST_ITEM = AccessibleRole.LIST_ITEM
        """
        List item role.
        
        An object that presents an element in a list. A list is usually contained within a scroll pane.
        
        See also SCROLL_PANE and LIST.
        """
        MENU = AccessibleRole.MENU
        """
        Menu role.
        
        An object usually found inside a menu bar that contains a list of actions the user can choose from. A menu can have any object as its children, but most often they are menu items, other menus, or rudimentary objects such as radio buttons, check boxes, or separators. For example, an application may have an \"Edit\" menu that contains menu items for \"Cut\" and \"Paste.\"
        
        See also MENU_BAR, MENU_ITEM, SEPARATOR, RADIO_BUTTON, CHECK_BOX, and POPUP_MENU.
        """
        MENU_BAR = AccessibleRole.MENU_BAR
        """
        Menu bar role.
        
        An object usually drawn at the top of the primary dialog box of an application that contains a list of menus the user can choose from. For example, a menu bar might contain menus for \"File,\" \"Edit,\" and \"Help.\"
        
        See also MENU, POPUP_MENU, and LAYERED_PANE.
        """
        MENU_ITEM = AccessibleRole.MENU_ITEM
        """
        Menu item role.
        
        An object usually contained in a menu that presents an action the user can choose. For example, the \"Cut\" menu item in an \"Edit\" menu would be an action the user can select to cut the selected area of text in a document.
        
        See also MENUBAR, SEPARATOR, and POPUP_MENU.
        """
        OPTION_PANE = AccessibleRole.OPTION_PANE
        """
        A specialized pane whose primary use is inside a DIALOG.
        
        See also DIALOG.
        """
        PAGE_TAB = AccessibleRole.PAGE_TAB
        """
        Page tab role.
        
        An object that is a child of a page tab list. Its sole child is the panel that is to be presented to the user when the user selects the page tab from the list of tabs in the page tab list.
        
        See also PAGE_TAB_LIST.
        """
        PAGE_TAB_LIST = AccessibleRole.PAGE_TAB_LIST
        """
        Page tab list role.
        
        An object that presents a series of panels (or page tabs), one at a time, through some mechanism provided by the object. The most common mechanism is a list of tabs at the top of the panel. The children of a page tab list are all page tabs.
        
        See also PAGE_TAB.
        """
        PANEL = AccessibleRole.PANEL
        """
        A generic container that is often used to group objects.
        """
        PARAGRAPH = AccessibleRole.PARAGRAPH
        """
        Paragraph of text.
        """
        PASSWORD_TEXT = AccessibleRole.PASSWORD_TEXT
        """
        Password text role.
        
        A text object used for passwords, or other places where the text contents is not shown visibly to the user.
        """
        POPUP_MENU = AccessibleRole.POPUP_MENU
        """
        Pop-up menu role.
        
        A temporary window that is usually used to offer the user a list of choices, and then hides when the user selects one of those choices.
        
        See also MENU and MENU_ITEM.
        """
        PUSH_BUTTON = AccessibleRole.PUSH_BUTTON
        """
        Push button role.
        
        An object the user can manipulate to tell the application to do something.
        
        See also CHECK_BOX, TOGGLE_BUTTON, RADIO_BUTTON, BUTTON_MENU and BUTTON_DROPDOWN.
        """
        PROGRESS_BAR = AccessibleRole.PROGRESS_BAR
        """
        An object used to indicate how much of a task has been completed.
        """
        RADIO_BUTTON = AccessibleRole.RADIO_BUTTON
        """
        Radio button role.
        
        A specialized check box that will cause other radio buttons in the same group to become unchecked when this one is checked.
        
        See also PUSH_BUTTON, TOGGLE_BUTTON, and CHECK_BOX.
        """
        RADIO_MENU_ITEM = AccessibleRole.RADIO_MENU_ITEM
        """
        This role is used for radio buttons that are menu items.
        """
        ROW_HEADER = AccessibleRole.ROW_HEADER
        """
        The header for a row of data.
        """
        ROOT_PANE = AccessibleRole.ROOT_PANE
        """
        Root pane role.
        
        A specialized pane that has a glass pane and a layered pane as its children.
        
        See also GLASS_PANE and LAYERED_PANE.
        """
        SCROLL_BAR = AccessibleRole.SCROLL_BAR
        """
        Scroll bar role.
        
        An object usually used to allow a user to incrementally view a large amount of data. Usually used only by a scroll pane.
        
        See also SCROLL_PANE.
        """
        SCROLL_PANE = AccessibleRole.SCROLL_PANE
        """
        Scroll pane role.
        
        An object that allows a user to incrementally view a large amount of information. Its children can include scroll bars and a viewport.
        
        See also SCROLL_BAR and VIEW_PORT.
        """
        SHAPE = AccessibleRole.SHAPE
        """
        Object with graphical representation used to represent content on draw pages.
        """
        SEPARATOR = AccessibleRole.SEPARATOR
        """
        Separator role.
        
        An object usually contained in a menu to provide a visual and logical separation of the contents in a menu. For example, the \"File\" menu of an application might contain menu items for \"Open,\" \"Close,\" and \"Exit,\" and will place a separator between \"Close\" and \"Exit\" menu items.
        
        See also MENU and MENU_ITEM.
        """
        SLIDER = AccessibleRole.SLIDER
        """
        Slider role.
        
        An object that allows the user to select from a bounded range. For example, a slider might be used to select a number between 0 and 100.
        """
        SPIN_BOX = AccessibleRole.SPIN_BOX
        """
        Spin box role.
        
        A SPIN_BOX is a simple spinner component and its main use is for simple numbers.
        """
        SPLIT_PANE = AccessibleRole.SPLIT_PANE
        """
        Split pane role.
        
        A specialized panel that presents two other panels at the same time. Between the two panels is a divider the user can manipulate to make one panel larger and the other panel smaller.
        """
        STATUS_BAR = AccessibleRole.STATUS_BAR
        """
        Status bar role.
        
        A STATUS_BAR is an simple component that can contain multiple labels of status information to the user.
        """
        TABLE = AccessibleRole.TABLE
        """
        Table component.
        
        An object used to present information in terms of rows and columns. An example might include a spreadsheet application.
        """
        TABLE_CELL = AccessibleRole.TABLE_CELL
        """
        Single cell in a table.
        """
        TEXT = AccessibleRole.TEXT
        """
        Text role.
        
        An object that presents text to the user. The text is usually editable by the user as opposed to a label or static text.
        
        See also LABEL and STATIC.
        """
        TEXT_FRAME = AccessibleRole.TEXT_FRAME
        """
        Collection of objects that constitute a logical text entity.
        """
        TOGGLE_BUTTON = AccessibleRole.TOGGLE_BUTTON
        """
        Toggle button role.
        
        A specialized push button that can be checked or unchecked, but does not provide a separate indicator for the current state.
        
        See also PUSH_BUTTON, CHECK_BOX and RADIO_BUTTON.
        """
        TOOL_BAR = AccessibleRole.TOOL_BAR
        """
        Tool bar role.
        
        A bar or palette usually composed of push buttons or toggle buttons. It is often used to provide the most frequently used functions for an application.
        """
        TOOL_TIP = AccessibleRole.TOOL_TIP
        """
        Tool tip role.
        
        An object that provides information about another object. The accessible Description property of the tool tip is often displayed to the user in a small \"help bubble\" when the user causes the mouse to hover over the object associated with the tool tip.
        """
        TREE = AccessibleRole.TREE
        """
        Tree role.
        
        An object used to present hierarchical information to the user. The individual nodes in the tree can be collapsed and expanded to provide selective disclosure of the tree's contents.
        """
        VIEW_PORT = AccessibleRole.VIEW_PORT
        """
        Viewport role.
        
        An object usually used in a scroll pane. It represents the portion of the entire data that the user can see. As the user manipulates the scroll bars, the contents of the viewport can change.
        
        See also SCROLL_PANE.
        """
        WINDOW = AccessibleRole.WINDOW
        """
        A top level window with no title or border.
        
        See also FRAME and DIALOG.
        """
        BUTTON_DROPDOWN = AccessibleRole.BUTTON_DROPDOWN
        """
        Button dropdown role.
        
        The object represents a button that drops down a list of items.
        
        See also PUSH_BUTTON and BUTTON_MENU.
        
        **since**
        
            OOo 3.0
        """
        BUTTON_MENU = AccessibleRole.BUTTON_MENU
        """
        Button menu role.
        
        The object represents a button that drops down a menu.
        
        See also PUSH_BUTTON and BUTTON_DROPDOWN.
        
        **since**
        
            OOo 3.0
        """
        CAPTION = AccessibleRole.CAPTION
        """
        Caption role.
        
        The object contains descriptive information, usually textual, about another user interface element such as a table, chart, or image.
        
        .
        
        **since**
        
            OOo 3.0
        """
        CHART = AccessibleRole.CHART
        """
        Chart role.
        
        The object is a graphical depiction of quantitative data. It may contain multiple subelements whose attributes and/or description may be queried to obtain both the quantitative data and information about how the data is being presented.
        
        **since**
        
            OOo 3.0
        """
        EDIT_BAR = AccessibleRole.EDIT_BAR
        """
        Edit bar role.
        
        A role indicating the object acts as a formula for calculating a value.
        
        **since**
        
            OOo 3.0
        """
        FORM = AccessibleRole.FORM
        """
        Form role.
        
        The object is a container for form controls, for instance as part of a web form or user-input form within a document.
        
        **since**
        
            OOo 3.0
        """
        IMAGE_MAP = AccessibleRole.IMAGE_MAP
        """
        Image map role.
        
        Usually a graphic with multiple hotspots, where each hotspot can be activated resulting in the loading of another document or section of a document.
        
        **since**
        
            OOo 3.0
        """
        NOTE = AccessibleRole.NOTE
        """
        Note role.
        
        An embedded note which is not visible until activated.
        
        **since**
        
            OOo 3.0
        """
        PAGE = AccessibleRole.PAGE
        """
        Page role.
        
        An object representing a page of document content. It is used in documents which are accessed by the user on a page by page basis.
        
        **since**
        
            OOo 3.0
        """
        RULER = AccessibleRole.RULER
        """
        Ruler role.
        
        An object which describes margins and tab stops, etc. for text objects which it controls.
        
        **since**
        
            OOo 3.0
        """
        SECTION = AccessibleRole.SECTION
        """
        Section role.
        
        The object is a containing instance of document content which constitutes a particular \"logical\" section of the document.
        
        **since**
        
            OOo 3.0
        """
        TREE_ITEM = AccessibleRole.TREE_ITEM
        """
        Tree item role.
        
        An object that presents an element in a tree
        
        See also TREE and TREE_TABLE.
        
        **since**
        
            OOo 3.0
        """
        TREE_TABLE = AccessibleRole.TREE_TABLE
        """
        Tree table role.
        
        An object which represents both hierarchical and tabular information.
        
        **since**
        
            OOo 3.0
        """
        COMMENT = AccessibleRole.COMMENT
        """
        Comment role.
        
        An object which represents a comment.
        
        A comment is anchored at a certain content position in the document and annotates this document content position or a certain text range of the document content. In the OpenDocument file format a comment is known as an annotation.
        
        See also COMMENT_END.
        
        **since**
        
            OOo 3.2
        """
        COMMENT_END = AccessibleRole.COMMENT_END
        """
        Comment end role.
        
        An invisible object which represents the end position of a text range which is annotated by a comment - see COMMENT.
        
        This object and the corresponding object representing the comment shall be in relation of type MEMBER_OF.
        
        **since**
        
            OOo 3.2
        """
        DOCUMENT_PRESENTATION = AccessibleRole.DOCUMENT_PRESENTATION
        """
        View of a presentation document.
        
        It's an specific variation of DOCUMENT for presentations.
        
        **since**
        
            LibreOffice 4.3
        """
        DOCUMENT_SPREADSHEET = AccessibleRole.DOCUMENT_SPREADSHEET
        """
        View of an spreadsheet document.
        
        It's an specific variation of DOCUMENT for spreadsheets.
        
        **since**
        
            LibreOffice 4.3
        """
        DOCUMENT_TEXT = AccessibleRole.DOCUMENT_TEXT
        """
        View of a text document.
        
        It's an specific variation of DOCUMENT for text.
        
        **since**
        
            LibreOffice 4.3
        """
        STATIC = AccessibleRole.STATIC
        """
        Static text role.
        
        An object that presents a brief amount of information to the user. The text is not editable by the user as opposed to a text, and not meant to have a relation with another object as opposed to a label.
        
        See also LABEL and TEXT.
        """

__all__ = ['AccessibleRole', 'AccessibleRoleEnum']

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
# Namespace: com.sun.star.form.runtime
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class FormFeature(metaclass=UnoConstMeta, type_name="com.sun.star.form.runtime.FormFeature", name_space="com.sun.star.form.runtime"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.form.runtime.FormFeature``"""
        pass

    class FormFeatureEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.form.runtime.FormFeature", name_space="com.sun.star.form.runtime"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.form.runtime.FormFeature`` as Enum values"""
        pass

else:
    from ....lo.form.runtime.form_feature import FormFeature as FormFeature

    class FormFeatureEnum(IntEnum):
        """
        Enum of Const Class FormFeature

        specifies the operations on a user interface form, as supported by the XFormOperations interface.
        
        **since**
        
            OOo 2.2
        """
        MoveAbsolute = FormFeature.MoveAbsolute
        """
        moves the form to a record given by absolute position.
        
        This operation cannot be executed without arguments. When executing it (i.e. when calling com.sun.star.form.runtime.XFormOperations.executeWithArguments()), you need to specify a parameter named Position of type long, which denotes the position to move the form to.
        """
        TotalRecords = FormFeature.TotalRecords
        """
        determines the number of total records in the form, including the potentially active insertion row.
        
        This is not strictly an operation you can do on a form, but rather a state you can retrieve (and display to the user) using the XFormOperations's respective methods.
        
        The state obtained here is a string, not a number. This is because in an UI form, the fact that the current record count is not yet known (since not all records have been visited, yet) is indicated by an asterisk (*) besides the record count.
        """
        MoveToFirst = FormFeature.MoveToFirst
        """
        moves the form to the first record
        """
        MoveToPrevious = FormFeature.MoveToPrevious
        """
        moves the form to the record before the current record, if there is any
        """
        MoveToNext = FormFeature.MoveToNext
        """
        moves the form to the record after the current record, if there is any
        """
        MoveToLast = FormFeature.MoveToLast
        """
        moves the form to the last record
        """
        MoveToInsertRow = FormFeature.MoveToInsertRow
        """
        moves the form to the insertion row, if privileges allow
        """
        SaveRecordChanges = FormFeature.SaveRecordChanges
        """
        saves all changes in the form's current record, including changes in the current control which had not yet been committed to the form
        """
        UndoRecordChanges = FormFeature.UndoRecordChanges
        """
        reverts all changes in the form's current record, including changes in the current control which had not yet been committed to the form
        """
        DeleteRecord = FormFeature.DeleteRecord
        """
        deletes the current record, while honoring any registered com.sun.star.form.XConfirmDeleteListeners
        """
        ReloadForm = FormFeature.ReloadForm
        """
        reloads the form content
        """
        SortAscending = FormFeature.SortAscending
        """
        sorts the form ascending by the field which the active form control is bound to.
        """
        SortDescending = FormFeature.SortDescending
        """
        sorts the form descending by the field which the active form control is bound to.
        """
        InteractiveSort = FormFeature.InteractiveSort
        """
        opens a dialog which allows the user to interactively specify a form sorting order
        """
        AutoFilter = FormFeature.AutoFilter
        """
        adds a filter to the form, which is defined by the active form control and its current value
        
        For instance, if the currently active form control is bound to a table field named Price, and currently has a value of 100, then invoking the AutoFilter operation will put an additional filter Price = 100 on the form.
        """
        InteractiveFilter = FormFeature.InteractiveFilter
        """
        opens a dialog which allows the user to interactively specify a form filter
        """
        ToggleApplyFilter = FormFeature.ToggleApplyFilter
        """
        toggles the com.sun.star.sdb.RowSet.ApplyFilter property of the form.
        """
        RemoveFilterAndSort = FormFeature.RemoveFilterAndSort
        """
        removes all filter and sort criteria put on the form.
        
        Note that this does not apply to criteria which are part of the form's data source. That is, if you bind the form to the SQL command SELECT * FROM Articles WHERE Price > 100, then the Price > 100 filter will not be removed.
        
        Effectively, this operation resets the com.sun.star.sdb.RowSet.Filter and com.sun.star.sdb.RowSet.Order properties of the form.
        """
        RefreshCurrentControl = FormFeature.RefreshCurrentControl
        """
        refreshes the current control
        
        Basically, this means calling XRefreshable.refresh on the current control, if it supports this interface.
        
        **since**
        
            OOo 3.1
        """

__all__ = ['FormFeature', 'FormFeatureEnum']

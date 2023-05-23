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
# Namespace: com.sun.star.form.binding
from ..data_aware_control_model import DataAwareControlModel as DataAwareControlModel_27110ef8
from .bindable_control_model import BindableControlModel as BindableControlModel_9a1111a8

class BindableDataAwareControlModel(DataAwareControlModel_27110ef8, BindableControlModel_9a1111a8):
    """
    Service Class

    is a specialization of the com.sun.star.form.DataAwareControlModel which additionally supports binding to external value suppliers.
    
    Control models usually have some kind of value property, which reflects the very current content of the controls associated with this model. For instance, for an com.sun.star.form.component.TextField, this would be the com.sun.star.awt.UnoControlEditModel.Text property of the base service. Similarly, a com.sun.star.form.component.CheckBox has a property com.sun.star.awt.UnoControlCheckBoxModel.State, which reflects the current check state.
    
    Usual com.sun.star.form.DataAwareControlModels can be bound to a column of a com.sun.star.form.component.DataForm, and exchange their content with such a column.In particular, when the com.sun.star.form.component.DataForm is moved to a different record, then the bound control model is updated with the value of it's column in this particular row.On the other hand, when any change in the control model (e.g. resulting from a user entering data in a control associated with the control model) is committed (com.sun.star.form.XBoundComponent.commit()), then the actual data of the control model is written into the associated com.sun.star.form.component.DataForm column.
    
    BindableDataAwareControlModel's additionally support an alternative value binding, which forces them to exchange their value with another foreign instance. In some sense, they are an abstraction of the data aware control models, which only support a specialized, hard-coded value binding (namely the binding to a com.sun.star.form.component.DataForm column).
    
    For this, they provide the XBindableValue interface which allows to set an external component to exchange the value with.
    
    The following rules apply when a data aware control model is bound to an external value binding:
    
    When a BindableDataAwareControlModel is being bound to an external value, using XBindableValue.setValueBinding(), then the control model (its value property, respectively) and the external value are initially synchronized by setting the external value (XValueBinding.getValue()) at the control model.

    See Also:
        `API BindableDataAwareControlModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1binding_1_1BindableDataAwareControlModel.html>`_
    """
    ...

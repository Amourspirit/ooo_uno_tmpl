# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
import warnings
warnings.filterwarnings('module')
warnings.warn('The csslo namespace is deprecated. Use lo instead.', DeprecationWarning, stacklevel=2)
from ....lo.form.inspection.button_navigation_handler import ButtonNavigationHandler as ButtonNavigationHandler
from ....lo.form.inspection.cell_binding_property_handler import CellBindingPropertyHandler as CellBindingPropertyHandler
from ....lo.form.inspection.default_form_component_inspector_model import DefaultFormComponentInspectorModel as DefaultFormComponentInspectorModel
from ....lo.form.inspection.edit_property_handler import EditPropertyHandler as EditPropertyHandler
from ....lo.form.inspection.event_handler import EventHandler as EventHandler
from ....lo.form.inspection.form_component_property_handler import FormComponentPropertyHandler as FormComponentPropertyHandler
from ....lo.form.inspection.submission_property_handler import SubmissionPropertyHandler as SubmissionPropertyHandler
from ....lo.form.inspection.xml_forms_property_handler import XMLFormsPropertyHandler as XMLFormsPropertyHandler
from ....lo.form.inspection.xsd_validation_property_handler import XSDValidationPropertyHandler as XSDValidationPropertyHandler

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
# Namespace: com.sun.star.form.submission
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_submission_veto_listener import XSubmissionVetoListener as XSubmissionVetoListener_18e1149e
    from ...task.x_interaction_handler import XInteractionHandler as XInteractionHandler_bf80e51

class XSubmission(XInterface_8f010a43):
    """
    is implemented by components which support submitting data.

    See Also:
        `API XSubmission <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1submission_1_1XSubmission.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.submission'
    __ooo_full_ns__: str = 'com.sun.star.form.submission.XSubmission'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.form.submission.XSubmission'

    @abstractmethod
    def addSubmissionVetoListener(self, listener: 'XSubmissionVetoListener_18e1149e') -> None:
        """
        registers the given listener to be notified when a submission occurs

        Raises:
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
        ...
    @abstractmethod
    def removeSubmissionVetoListener(self, listener: 'XSubmissionVetoListener_18e1149e') -> None:
        """
        revokes a listener which has previously been registered to be notified when a submission occurs

        Raises:
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
        ...
    @abstractmethod
    def submit(self) -> None:
        """
        tells the component to submit data

        Raises:
            com.sun.star.util.VetoException: ``VetoException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def submitWithInteraction(self, aHandler: 'XInteractionHandler_bf80e51') -> None:
        """
        tells the component to submit data

        Raises:
            com.sun.star.util.VetoException: ``VetoException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...

__all__ = ['XSubmission']


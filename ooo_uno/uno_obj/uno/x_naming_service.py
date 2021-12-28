# coding: utf-8
# this is a auto generated file generated by Cheetah
from abc import abstractmethod
from .x_interface import XInterface


class XNamingService(XInterface):
    """
    allows to insert, remove and access named objects.

    See Also:
        `API XNamingService <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1uno_1_1XNamingService.html>`_
    """

    @abstractmethod
    def getRegisteredObject(self, Name: str) -> 'XInterface':
        """
        provides a previous registered object.

        Raises:
            Exception: ``Exception``
        """
    @abstractmethod
    def registerObject(self, Name: str, Object: 'XInterface') -> None:
        """
        registers one object under the specified name.
        
        If any object is registered before, then this object is revoked automatically.

        Raises:
            Exception: ``Exception``
        """
    @abstractmethod
    def revokeObject(self, Name: str) -> None:
        """
        revokes the registration of an object.
        
        If the object was not previously registered, then this call does nothing.

        Raises:
            Exception: ``Exception``
        """

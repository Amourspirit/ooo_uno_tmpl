# coding: utf-8
from typing import Any
import uno


# coding: utf-8

def uno_enum_class_new(cls, value):
    """
    New (__new__) method for dynamically created uno.enum classes

    Args:
        value (object): Can be Uno.Enum, uno.Enum.value, str

    Raises:
        ValueError: if unable to match enum instance

    Returns:
        [uno.Enum]: Enum Instance

    Example:
        ..code-block:: python

            >>> e = HorizontalAlignment("RIGHT")
            >>> print(e.value)
            RIGHT
            >>> e = HorizontalAlignment(HorizontalAlignment.LEFT)
            >>> print(e.value)
            LEFT
            >>> e = HorizontalAlignment(HorizontalAlignment.CENTER.value)
            >>> print(e.value)
            CENTER
    """
    if isinstance(value, str):
        if hasattr(cls, value):
            return getattr(cls, value)
    _type = type(value)
    if _type is uno.Enum:
        return value
    if _type is cls:
        return value
    raise ValueError("%r is not a valid %s" % (value, cls.__name__))


def uno_enum_class_ne(self, other):
    return not self.__eq__(other)


class UnoEnumMeta(type):
    """
    Get access to Uno Enum values without having to directly import them.

    This is a meta class.

    Example:

        .. code-block:: python

            class FillMode(metaclass=UnoEnumMeta, type_name="com.sun.star.sheet.FillMode", name_space="com.sun.star.sheet"):
                pass

    Note:
        Uno enums can not be imported directly in python.

        ``from com.sun.star.sheet import FillMode`` is not a valid import
        and results in an import error.

        ``from com.sun.star.sheet.FillMode import LINEAR, SIMPLE, GROWTH`` is valid import but cumbersome.

        This metaclass use a just in time approach. If the enum is not yet an attribute it is automatiacally added dynamically.
        All subsequent calls automatically use the dynamically added attribute.
    """
    _initialized = False  # This class var is important. It is always False.
    # The instances will override this with their own,
    # set to True.
    typeName = None
    __ooo_type_name__ = "enum"
    __ooo_full_ns__ = None
    __ooo_ns__ = None

    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        return super().__prepare__(name, bases, **kwargs)

    def __new__(metacls, name, bases, namespace, **kwargs):
        return super().__new__(metacls, name, bases, namespace)

    def __init__(cls, name, bases, namespace, type_name, name_space, **kwargs):
        super().__init__(name, bases, namespace)
        cls.typeName = type_name
        cls.__ooo_full_ns__ = type_name
        cls.__ooo_ns__ = name_space
        cls._initialized = True

    def __call__(cls, value) -> uno.Enum:
        """
        New (__new__) method for dynamically created uno.enum classes

        Args:
            value (object): Can be Uno.Enum, uno.Enum.value, str

        Raises:
            TypeError: if unable to match enum instance

        Returns:
            [uno.Enum]: Enum Instance

        Example:
            ..code-block:: python

                >>> e = HorizontalAlignment("RIGHT")
                >>> print(e.value)
                RIGHT
                >>> e = HorizontalAlignment(HorizontalAlignment.LEFT)
                >>> print(e.value)
                LEFT
                >>> e = HorizontalAlignment(HorizontalAlignment.CENTER.value)
                >>> print(e.value)
                CENTER
        """
        if isinstance(value, str):
            if hasattr(cls, value):
                return getattr(cls, value)
        _type = type(value)
        if _type is uno.Enum:
            return value
        if _type is cls:
            return value
        raise TypeError("%r is not a valid %s" % (value, cls.__name__))

    def __getattr__(self, __name: str) -> uno.Enum | Any:
        if self._initialized:
            # Provide the caller attributes in whatever ways interest you.
            try:
                key = __name
                e = uno.Enum(self.typeName, __name)
                # metaclass __dict__ is a mappingproxy
                # the only way to set attribue is to call super
                super().__setattr__(key, e)
                return self.__dict__[key]
            except Exception:
                raise AttributeError(
                    f"Enum {self.typeName} has no attribute {__name}")
        else:
            try:
                # Transparent access to instance vars.
                return self.__dict__[__name]
            except KeyError:
                raise AttributeError(__name)

    def __setattr__(self, key, value):
        if self._initialized:
            pass
        else:
            # metaclass __dict__ is a mappingproxy
            # the only way to set attribue is to call super
            super().__setattr__(key, value)  # Transparent access.

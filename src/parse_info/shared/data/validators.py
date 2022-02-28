# coding: utf-8

def str_null_empty(value:str) -> str:
    """
    Test if a string is null or empty

    Args:
        value (str): string to test

    Raises:
        TypeError: if ``value`` is not a string.
        ValueError: if ``value`` is null or empty.

    Returns:
        str: ``value``
    """
    if not isinstance(value, str):
        raise TypeError("value is required to be a string instance.")
    s = value.strip()
    if len(s) > 0:
        return value
    raise ValueError("must not be null or empty string")


def namespace(value: str) -> str:
    """
    Test if ``value`` starts with ``com.sun.star.``

    Args:
        value (str): namespace string for testing.

    Raises:
        TypeError: if ``value`` is not a string.
        ValueError: If string is null or does not start with ``com.sun.star.``

    Returns:
        str: ``value``
    """
    s = str_null_empty(value=value)
    if value.startswith('com.sun.star.'):
        return value
    raise ValueError(
        f"must start with 'com.sun.star.'. Current value: {value}")

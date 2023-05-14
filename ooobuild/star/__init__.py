# coding: utf-8
import os
from typing import TYPE_CHECKING

__version_tmpl__ = "0.2.10"

_IGNORE_IMPORT_ERROR = os.environ.get("ooouno_ignore_import_error", None) in ("True", "true", "yes")

if TYPE_CHECKING is False and _IGNORE_IMPORT_ERROR is False:
    raise ImportError

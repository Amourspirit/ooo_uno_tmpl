=============
Release Notes
=============

Version 0.2.0
=============
Older version fo LO API are supported via the previous version.

Dropped try blocks for import in the dyn import namespace.
Previously each import in the dyn namespace was wrapped in a try block.
This was for backwards compatibality versions of LibreOffice pre ``7.2``.
This option is set by the ``dyn_ns_import_check`` in config.json.

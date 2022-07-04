=============
Release Notes
=============

Version 0.2.10
==============
Add type rules to detect uno.ByteSequence

Version 0.2.1
=============

Older version fo LO API are supported via the previous version.

Dropped ``try`` blocks for import in the dyn import namespace.
Previously each import in the dyn namespace was wrapped in a try block.
This was for backwards compatibality versions of LibreOffice pre ``7.2``.
This option is set by the ``dyn_ns_import_check`` in config.json.

Include ``ooobuild`` and ``ooodata`` directories.
Even though the data in these folders are automitaclly generated ( this is also true for ``lo`` dir) from
LO API webpages. When the LO API updates to a new version this data cannot be generated again.
For this reason they are being included in src.

Removed ``--clean-scratch`` as an option from ``make`` command line options. Option is no longer applicable.

Version 0.2.0
=============

Add generation of ``*.pyi`` files.
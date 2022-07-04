from pathlib import Path
from ..utilities import util
from .. import __version__


def write_star_error() -> None:
    """
    Writes __init__.py with raise ImportError into star namesapce.

    When com.sun.star namesapce is pure typings then
    any import form the namesapce will be imported by python a namesapce.

    This means python would see ``import com.sun.star.uno``
    as a valid import. The issue is when uno.py imports it expects an import
    error for imports such as ``from com.sun.star.uno import Exception as UnoException``.

    Becuase ``import com.sun.star.uno`` imports as a namesapce the import error is not
    triggered and uno import method would return a namesapce and then an ImportError
    would be raised as ``com.sun.star.uno`` is valid but ``import as Exception``
    raises an ImportError Exception.

    The solution is to raise an ImportError at the namespace level. This is caught by
    uno and then a real uno object is imported and returned.

    In some cases it may be desireable to not raise import error.
    For this reason a check in done for a global key that is set in
    config.json as ``gloabal_ignore_import_error`` with a default value of ``ooouno_ignore_import_error``.
    if global var is set to ``"True"`` or ``"true"`` or ``"yes"`` then ImportError is NOT raised.
    """
    config = util.get_app_cfg()
    root_dir = Path(util.get_root())
    p = Path(config.builld_dir, *config.com_sun_star_pyi)
    if not p.is_absolute():
        p = root_dir.joinpath(p)
    util.mkdirp(p)
    p = p.joinpath('__init__.py')
    # https://www.sitekickr.com/tools/line-break-remover/
    contents = f'# coding: utf-8\nimport os\nfrom typing import TYPE_CHECKING\n\n__version_tmpl__ = "{__version__}"\n\n_IGNORE_IMPORT_ERROR = os.environ.get("{config.gloabal_ignore_import_error}", None) in ("True", "true", "yes")\n\nif TYPE_CHECKING == False and _IGNORE_IMPORT_ERROR == False:\n    raise ImportError\n'
    with open(p, 'w') as file:
        file.write(contents)

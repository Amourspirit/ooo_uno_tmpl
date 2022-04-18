from pathlib import Path
from ..utilities import util

def write_star_error() -> None:
    """
    Writes __init__.py with raise ImportError into star namesapce.

    When com.sun.star namesapce is pure typings then
    any import form the namesapce will be imported by python a namesapce.
    
    This means python would see ``import com.sun.star.uno``
    as a valid import. The issue is when uno.py imports it expects an import
    error for imports such as ``from com.sun.star.uno import Exception as UnoException``.
    
    Becuase `import com.sun.star.uno`` import as a namesapce the import error is not
    triggered and uno import method would return a namesapce and then an ImportError
    would be raised as ``com.sun.star.uno`` is valid but ``import as Exception``
    raises an ImportError Exception.
    
    The solution is to raise an ImportError at the namespace level. This is caught by
    uno and then a real uno object is imported and returned.
    """
    config = util.get_app_cfg()
    root_dir = Path(util.get_root())
    p = Path(config.builld_dir, *config.com_sun_star_pyi)
    if not p.is_absolute():
        p = root_dir.joinpath(p)
    util.mkdirp(p)
    p = p.joinpath('__init__.py')
    contents = "from typing import TYPE_CHECKING\n\nif not TYPE_CHECKING:\n    raise ImportError\n"
    with open(p, 'w') as file:
        file.write(contents)

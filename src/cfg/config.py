# coding: utf-8
import json
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class AppConfig:
    libre_office_ver: str
    """Version of Libre Office that is being built such as 7.2"""
    min_module_links_ver: str
    """Min version that can be parsed for module_links.json files"""
    module_links_file: str
    """Json file name for module links such as module_links.json"""
    min_json_data_ver: str
    """Min version that can be parsed for .json files of Module Components"""
    uno_base_dir: str
    """Base Directory for Uno such as lo"""
    cache_dir: str
    """The cache directory to use. This is generally used in creating a cache directory is system temp dir."""
    base_dir: str
    """
    Base dir for project such as ooo
    
    This the root dir for helper modules
    """
    uno_obj_dir: str
    """Uno obj dir such as uno. This is the directory that templates and json data file are written to."""
    build_dir: str
    """Output build dir such as build"""
    data_dir: str
    """Output data dir such as data"""
    dyn_dir: str
    """
    Dynamic output directory such as ``dyn``.
    
    This will usually be a subdirectory of ``build_dir``
    """
    pyi_dir: List[str]
    """
    Pyi output directory such as ``['star', '_pyi']``.
    
    This will usually be a subdirectory of ``build_dir``
    """
    pyi_write_imports_in_init: bool
    """
    Write imports in ``__init__.py`` files in pyi_dir.
    
    If True then each import directory will have an ``__init__.py`` file with imports of all it modules in that directory.
    
    If True then ``pyi_write_star_dir_old_style`` Should be False and ``pyi_dir`` set to ['star'].
    """
    pyi_write_star_dir_old_style: bool
    """
    Specifies if make runs a special method to write all star modules into a star subdirectories and imports from the value
    of ``pyi_dir``.
    
    This property is mainly for backwards compatibility with older versions of make.
    """
    scratch_dir: str
    """Output scratch dir such as scratch"""
    resource_dir: str
    """App Resources dir such as resources"""
    db_mod_info: str
    """Name of Module Info database in ``resource_dir`` such as ``mod_info.sqlite``"""
    cache_duration: float
    """
    The amount of time in seconds to keep files in cache.

    Note:
        Files cached in system tmp folder will be cleared upon reboot.
    """
    pixel_inherit: int
    """
    Index color of component map images for inherits.
    """
    pixel_noinherit: int
    """
    Index color of component map images for NON-inherits.
    """
    pixel_map_no_link: int
    """
    Image maps have indexed colors. All shapes that have a link have one border color.
    Shape that has no link has another border color. This is the no link border color.
    Used for finding shape within an image.
    """
    pixel_map_min_shape_width: int
    """
    Min number of pixels to match for a shape in an image.
    See Also: ``pixel_map_no_link``
    """
    base_const: str
    """
    module path to const such as ``ooo_uno.base.const``
    """
    base_const_int: str
    """
    Base class for constants of int type such as ``ConstIntBase``
    """
    base_const_int_flags: str
    """
    Base class for constants of int flags type such as ``ConstIntFlagsBase``
    """
    helper_ns: str
    """helper namespace such as ooo.helper"""
    helper_mod: str
    """helper module name such as uno_helper"""
    enum_mod: str
    """enum helper mod name such as enum_helper"""
    env: str
    """
    module path to oenv such as ``ooo_uno.oenv``
    """
    remove_parent_inherited: bool
    """
    Determines if parsers remove classes from inheritance if an inherited class
    is already inherited by a parent class.
    """
    use_long_import_names: bool
    """
    Determines if Long Import Name are used.
    
    If ``True`` then by default import will be in a format similar to :
        ``from ..accessibility.x_accessible_action import XAccessibleAction as accessibility_x_accessible_action_i``
    
    If ``False`` then by default import will be in a format similar to :
        ``from ..accessibility.x_accessible_action import XAccessibleAction``
    
    """
    template_struct_ext: str
    """Extension for struct files such as .tmpl"""
    template_const_ext: str
    """Extension for const files such as .tmpl"""
    template_interface_ext: str
    """Extension for interface files such as .tmpl"""
    template_singleton_ext: str
    """Extension for singleton files such as .tmpl"""
    template_enum_ext: str
    """Extension for enum files such as .tmpl"""
    template_exception_ext: str
    """Extension for exception files such as .tppi"""
    template_typedef_ext: str
    """Extension for typedef files such as .tppi"""
    template_service_ext: str
    """Extension for service files such as .tppi"""
    template_dyn_ext: str
    """Extension for dynamic templates such as .dyn"""
    template_dyn_py_ext: str
    """Extension for dynamic templates py ext such as .dynpy"""
    template_pyi_ext: str
    """Extension for pyi templates such as .tpyi"""
    template_pyi_py_ext: str
    """Extension for pyi templates py ext such as .pyipy"""
    component_types: List[str]
    com_sun_star_lo: List[str]
    """
    Path Like structure that will be used for LO namespace imports in build dir such as ['csslo'].
    """
    com_sun_star_dyn: List[str]
    """
    Path Like structure that will be used for DYN namespace imports in build dir such as ['cssdyn'].
    """
    com_sun_star_pyi: List[str]
    """
    Path Like structure that will be used for PYI namespace imports in build dir such as ['star'].
    """
    inc_lic: str
    """Path to License Include File"""
    css_dyn_ns_import_check: bool
    """
    Determines if import checks are done for cssdyn namespace exports
    
    Some classes in the cssdyn namespace may not be available on older version of LO
    such as ``com.sun.star.util.XBinaryDataContainer`` which is a LO 7.2 interface.
    If an attempt to import this class in older ver then the entire process will fail
    Adding import check resolves this issue.
    
    Newer releases of this lin can probably turn this off and user can then use previous
    version for backward compatibility.
    """
    css_dyn_ns_import_exceptions: List[str]
    """
    if ``dyn_ns_import_check`` is ``True`` then this is the exceptions to ignore.
    Usually this is ``['ImportError', 'AttributeError']`` but can be other exceptions.
    
    Sometimes API classes are dropped and that would result in an ``ImportError``.
    Also certain classes such as ``ooobuild.dyn.drawing.canvas_feature.CanvasFeature``
    have attributes that can not be imported such as ``CanvasFeature.None``.
    """
    css_dyn_ns_import_excludes: List[str]
    """
    List of Full Namespaces to exclude from dyn import.
    
    Classes such as ``com.sun.star.beans.Ambiguous`` Should not be imported from dyn.
    """
    css_dyn_ns_import_warn: bool
    """
    Specifies if a Deprecation Warning should be raised for cssdyn imports.
    """
    css_lo_ns_import_warn: bool
    """
    Specifies if a Deprecation Warning should be raised for csslo imports.
    """
    global_ignore_import_error: str
    """
    This is the key used when creating com.sun.star.__init__.py for pyi.
    
    This global key is used in os.environ to check if import error should be
    raised when importing from com.sun.star (default is is error is raised if not TYPE_CHECKING).
    """


def read_config(config_file: str) -> AppConfig:
    """
    Gets config for given config file

    Args:
        config_file (str): Config file to load

    Returns:
        AppConfig: Configuration object
    """
    with open(config_file, 'r') as file:
        data = json.load(file)
        return AppConfig(**data)


def read_config_default() -> AppConfig:
    """
    Loads default configuration ``config.json``

    Returns:
        AppConfig: Configuration Object
    """
    root = Path(__file__).parent
    config_file = Path(root, 'config.json')
    return read_config(str(config_file))

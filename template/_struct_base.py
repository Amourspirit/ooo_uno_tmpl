#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
from Cheetah.compat import unicode
from _base_struct import BaseStruct

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.6.post2'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 2)
__CHEETAH_genTime__ = 1640689567.7542617
__CHEETAH_genTimestamp__ = 'Tue Dec 28 06:06:07 2021'
__CHEETAH_src__ = '_struct_base.tmpl'
__CHEETAH_srcLastModified__ = 'Tue Dec 28 06:05:51 2021'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class struct_base(BaseStruct):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(struct_base, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        _v = VFN(VFFSL(SL,"self",True),"init_data",False)() # '$self.init_data()' on line 4, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.init_data()')) # from line 4, col 1.
        #  str, list, tupple
        #  set is attribs is sorted
        _v = VFN(VFFSL(SL,"self",True),"load_data",False)() # '$self.load_data()' on line 18, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.load_data()')) # from line 18, col 1.
        #  Main Template
        namespace = ''
        sorted = VFN(VFFSL(SL,"self",True),"get_sorted_names",False)()
        str_inherits = "object"
        is_inherits = len(VFFSL(SL,"inherits",True)) > 0
        if VFFSL(SL,"is_inherits",True): # generated from line 24, col 1
            str_inherits = VFN(VFFSL(SL,"self",True),"lst_to_str",False)(VFFSL(SL,"inherits",True))
        write('''# coding: utf-8
# this is a auto generated file generated by Cheetah
''')
        if VFFSL(SL,"dynamic_struct",True): # generated from line 29, col 1
            write('''import os
from collections import namedtuple
''')
        for imp in VFFSL(SL,"imports",True): # generated from line 33, col 1
            write('''import ''')
            _v = VFFSL(SL,"imp",True) # '$imp' on line 34, col 8
            if _v is not None: write(_filter(_v, rawExpr='$imp')) # from line 34, col 8.
            write('''
''')
        for frm, imp in VFFSL(SL,"from_imports",True): # generated from line 36, col 1
            write('''from ''')
            _v = VFFSL(SL,"frm",True) # '$frm' on line 37, col 6
            if _v is not None: write(_filter(_v, rawExpr='$frm')) # from line 37, col 6.
            write(''' import ''')
            _v = VFFSL(SL,"imp",True) # '$imp' on line 37, col 18
            if _v is not None: write(_filter(_v, rawExpr='$imp')) # from line 37, col 18.
            write('''
''')
        if VFFSL(SL,"requires_typing",True) or VFFSL(SL,"dynamic_struct",True): # generated from line 39, col 1
            write('''import typing
''')
        if len(VFFSL(SL,"auto_imports",True)) > 0: # generated from line 42, col 1
            write('''if typing.TYPE_CHECKING:
''')
            for frm, imp in VFFSL(SL,"auto_imports",True): # generated from line 44, col 5
                write('''    from ''')
                _v = VFFSL(SL,"frm",True) # '$frm' on line 45, col 10
                if _v is not None: write(_filter(_v, rawExpr='$frm')) # from line 45, col 10.
                write(''' import ''')
                _v = VFFSL(SL,"imp",True) # '$imp' on line 45, col 22
                if _v is not None: write(_filter(_v, rawExpr='$imp')) # from line 45, col 22.
                write('''
''')
        write('''

class ''')
        _v = VFFSL(SL,"name",True) # '${name}' on line 50, col 7
        if _v is not None: write(_filter(_v, rawExpr='${name}')) # from line 50, col 7.
        write('''(''')
        _v = VFFSL(SL,"str_inherits",True) # '${str_inherits}' on line 50, col 15
        if _v is not None: write(_filter(_v, rawExpr='${str_inherits}')) # from line 50, col 15.
        write('''):
    """
''')
        if isinstance(VFFSL(SL,"desc",True), str): # generated from line 52, col 5
            write('''    ''')
            _v = VFFSL(SL,"desc",True) # '$desc' on line 53, col 5
            if _v is not None: write(_filter(_v, rawExpr='$desc')) # from line 53, col 5.
            write('''
''')
        else: # generated from line 54, col 5
            for line in VFFSL(SL,"desc",True): # generated from line 55, col 9
                write('''    ''')
                _v = VFFSL(SL,"line",True) # '$line' on line 56, col 5
                if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 56, col 5.
                write('''
''')
        if VFFSL(SL,"link",True): # generated from line 59, col 1
            write('''
    See Also:
        `API ''')
            _v = VFFSL(SL,"name",True) # '$name' on line 62, col 14
            if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 62, col 14.
            write(''' <''')
            _v = VFFSL(SL,"link",True) # '$link' on line 62, col 21
            if _v is not None: write(_filter(_v, rawExpr='$link')) # from line 62, col 21.
            write('''>`_
''')
        if VFFSL(SL,"dynamic_struct",True): # generated from line 64, col 1
            write('''
    Note:
        | At runtime this will be a `namedtuple <https://docs.python.org/3/library/collections.html#collections.namedtuple>`_ and not a class.
        | At design time a class is presumed. This allows for better typings.
        | Effectively functionallity is the same and namedtuple is more efficient than a class.
''')
        write('''    """
    def __init__(self, ''')
        _v = VFN(VFFSL(SL,"self",True),"get_constructor_str",False)() # '$self.get_constructor_str()' on line 72, col 24
        if _v is not None: write(_filter(_v, rawExpr='$self.get_constructor_str()')) # from line 72, col 24.
        write('''):
''')
        for i, tpl in enumerate(VFFSL(SL,"sorted",True)): # generated from line 73, col 1
            index = tpl[1]
            itm = VFFSL(SL,"attribs",True)[VFFSL(SL,"index",True)]
            write('''        self._''')
            _v = VFN(VFFSL(SL,"self",True),"camel_to_snake",False)(VFFSL(SL,"itm.name",True)) # '$self.camel_to_snake($itm.name)' on line 76, col 15
            if _v is not None: write(_filter(_v, rawExpr='$self.camel_to_snake($itm.name)')) # from line 76, col 15.
            write(''' = ''')
            _v = VFFSL(SL,"itm.name",True) # '$itm.name' on line 76, col 49
            if _v is not None: write(_filter(_v, rawExpr='$itm.name')) # from line 76, col 49.
            write('''
''')
        for i, tpl in enumerate(VFFSL(SL,"sorted",True)): # generated from line 78, col 1
            index = tpl[1]
            itm = VFN(VFFSL(SL,"self",True),"get_attrib_for_prop",False)(VFFSL(SL,"index",True))
            write('''
    @property
    def ''')
            _v = VFFSL(SL,"itm.name",True) # '${itm.name}' on line 83, col 9
            if _v is not None: write(_filter(_v, rawExpr='${itm.name}')) # from line 83, col 9.
            write('''(self) -> ''')
            _v = VFFSL(SL,"itm.type",True) # '$itm.type' on line 83, col 30
            if _v is not None: write(_filter(_v, rawExpr='$itm.type')) # from line 83, col 30.
            write(''':
''')
            if VFFSL(SL,"itm.lines",True): # generated from line 84, col 5
                write('''        """
''')
                if isinstance(VFFSL(SL,"itm.lines",True), str): # generated from line 86, col 9
                    write('''        ''')
                    _v = VFFSL(SL,"itm.lines",True) # '$itm.lines' on line 87, col 9
                    if _v is not None: write(_filter(_v, rawExpr='$itm.lines')) # from line 87, col 9.
                    write('''
''')
                else: # generated from line 88, col 9
                    for line in VFFSL(SL,"itm.lines",True): # generated from line 89, col 13
                        write('''        ''')
                        _v = VFFSL(SL,"line",True) # '$line' on line 90, col 9
                        if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 90, col 9.
                        write('''
''')
                if 'orig_type' in VFFSL(SL,"itm",True): # generated from line 93, col 9
                    write('''
        **Libre Office Type:** ``''')
                    _v = VFFSL(SL,"itm",True)['orig_type'] # "${itm['orig_type']}" on line 95, col 34
                    if _v is not None: write(_filter(_v, rawExpr="${itm['orig_type']}")) # from line 95, col 34.
                    write('''``
''')
                write('''        """
''')
            write('''        return self._''')
            _v = VFN(VFFSL(SL,"self",True),"camel_to_snake",False)(VFFSL(SL,"itm.name",True)) # '$self.camel_to_snake($itm.name)' on line 99, col 22
            if _v is not None: write(_filter(_v, rawExpr='$self.camel_to_snake($itm.name)')) # from line 99, col 22.
            write('''
''')
        if VFFSL(SL,"dynamic_struct",True): # generated from line 101, col 1
            write('''
def _dynamic_struct():
    # Dynamically create nametuple that is more efficient as stand in for struct

    global ''')
            _v = VFFSL(SL,"name",True) # '$name' on line 106, col 12
            if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 106, col 12.
            write("""
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    # if statment is to stop VS Code from reporting errors
    if not typing.TYPE_CHECKING:
        """)
            _v = VFFSL(SL,"name",True) # '${name}' on line 112, col 9
            if _v is not None: write(_filter(_v, rawExpr='${name}')) # from line 112, col 9.
            write(""" = namedtuple('""")
            _v = VFFSL(SL,"name",True) # '$name' on line 112, col 31
            if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 112, col 31.
            write("""', [""")
            _v = VFN(VFFSL(SL,"self",True),"get_nt_names_str",False)() # '$self.get_nt_names_str()' on line 112, col 40
            if _v is not None: write(_filter(_v, rawExpr='$self.get_nt_names_str()')) # from line 112, col 40.
            write('''])

if not typing.TYPE_CHECKING:
    _dynamic_struct()
''')
        write("""
__all__ = ['""")
        _v = VFFSL(SL,"name",True) # '$name' on line 118, col 13
        if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 118, col 13.
        write("""']""")
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    dynamic_struct = False

    name = ""

    desc = "" 

    quote = set()

    typings = set()

    sort = True 

    link = ""

    imports = []

    inherits = []

    from_imports = []

    auto_imports = []

    requires_typing = False

    attribs = []

    _mainCheetahMethod_for_struct_base = 'respond'

## END CLASS DEFINITION

if not hasattr(struct_base, '_initCheetahAttributes'):
    templateAPIClass = getattr(struct_base,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(struct_base)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=struct_base()).run()



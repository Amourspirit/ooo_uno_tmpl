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
import typing
from _interface_base import BaseInterface

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.6.post2'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 2)
__CHEETAH_genTime__ = 1638624682.9053159
__CHEETAH_genTimestamp__ = 'Sat Dec  4 08:31:22 2021'
__CHEETAH_src__ = '_x_base.tmpl'
__CHEETAH_srcLastModified__ = 'Sat Dec  4 08:30:51 2021'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class x_base(BaseInterface):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(x_base, self).__init__(*args, **KWs)
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
        
        #  see: https://cheetahtemplate.org/users_guide/inheritanceEtc.html#implements
        #  $from_imports is a tuple eg: $from_imports = [('.tab_align', 'TabAlign')]
        #  main Template
        is_method = 'methods' in VFFSL(SL,"attribs",True)
        abc_imports = ['abstractmethod'] if VFFSL(SL,"is_method",True) else []
        write('''# coding: utf-8
# this is a auto generated file generated by Cheetah
''')
        for imp in VFFSL(SL,"imports",True): # generated from line 19, col 1
            write('''import ''')
            _v = VFFSL(SL,"imp",True) # '$imp' on line 20, col 8
            if _v is not None: write(_filter(_v, rawExpr='$imp')) # from line 20, col 8.
            write('''
''')
        if len(VFFSL(SL,"abc_imports",True)) > 0: # generated from line 22, col 1
            write('''from abc import ''')
            _v = VFN(VFFSL(SL,"self",True),"lst_to_str",False)(VFFSL(SL,"abc_imports",True)) # '$self.lst_to_str($abc_imports)' on line 23, col 17
            if _v is not None: write(_filter(_v, rawExpr='$self.lst_to_str($abc_imports)')) # from line 23, col 17.
            write('''
''')
        for frm, imp in VFFSL(SL,"from_imports",True): # generated from line 25, col 1
            write('''from ''')
            _v = VFFSL(SL,"frm",True) # '$frm' on line 26, col 6
            if _v is not None: write(_filter(_v, rawExpr='$frm')) # from line 26, col 6.
            write(''' import ''')
            _v = VFFSL(SL,"imp",True) # '$imp' on line 26, col 18
            if _v is not None: write(_filter(_v, rawExpr='$imp')) # from line 26, col 18.
            write('''
''')
        write('''

class ''')
        _v = VFFSL(SL,"name",True) # '${name}' on line 30, col 7
        if _v is not None: write(_filter(_v, rawExpr='${name}')) # from line 30, col 7.
        write('''(''')
        _v = VFN(VFFSL(SL,"self",True),"lst_to_str",False)(VFFSL(SL,"inherits",True)) # '$self.lst_to_str($inherits)' on line 30, col 15
        if _v is not None: write(_filter(_v, rawExpr='$self.lst_to_str($inherits)')) # from line 30, col 15.
        write('''):
    """
''')
        for line in VFN(VFFSL(SL,"self",True),"line_gen",False)(VFFSL(SL,"desc",True)): # generated from line 32, col 5
            write('''    ''')
            _v = VFFSL(SL,"line",True) # '$line' on line 33, col 5
            if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 33, col 5.
            write('''
''')
        if VFFSL(SL,"link",True): # generated from line 35, col 1
            write('''
    See Also:
        `API ''')
            _v = VFFSL(SL,"name",True) # '$name' on line 38, col 14
            if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 38, col 14.
            write(''' <''')
            _v = VFFSL(SL,"link",True) # '$link' on line 38, col 21
            if _v is not None: write(_filter(_v, rawExpr='$link')) # from line 38, col 21.
            write('''>`_
''')
        write('''    """

''')
        if VFFSL(SL,"is_method",True): # generated from line 42, col 1
            methods = VFFSL(SL,"attribs",True)['methods']
            for method in VFFSL(SL,"methods",True): # generated from line 44, col 5
                m_desc = VFFSL(SL,"method",True)['desc']
                write('''    @abstractmethod
    ''')
                _v = VFN(VFFSL(SL,"self",True),"get_formated_meth",False)(VFFSL(SL,"method",True)) # '$self.get_formated_meth($method)' on line 47, col 5
                if _v is not None: write(_filter(_v, rawExpr='$self.get_formated_meth($method)')) # from line 47, col 5.
                write('''
        """
''')
                for line in VFN(VFFSL(SL,"self",True),"line_gen",False)(VFFSL(SL,"m_desc",True)): # generated from line 49, col 9
                    write('''        ''')
                    _v = VFFSL(SL,"line",True) # '$line' on line 50, col 9
                    if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 50, col 9.
                    write('''
''')
                write('''        """
''')
        
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

    name = "XFont"

    desc = []

    link = ""

    inherits = []

    imports = ['typing']

    from_imports = []

    attribs = {}

    _mainCheetahMethod_for_x_base = 'respond'

## END CLASS DEFINITION

if not hasattr(x_base, '_initCheetahAttributes'):
    templateAPIClass = getattr(x_base,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(x_base)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=x_base()).run()



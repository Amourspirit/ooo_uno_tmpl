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
from _struct_base import struct_base as s_base

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.6.post2'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 2)
__CHEETAH_genTime__ = 1638250828.7570243
__CHEETAH_genTimestamp__ = 'Tue Nov 30 00:40:28 2021'
__CHEETAH_src__ = '/home/paul/Documents/Projects/Python/Cheeta3/ooo_uno/uno_obj/style/TabStop.tmpl'
__CHEETAH_srcLastModified__ = 'Mon Nov 29 23:43:24 2021'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class TabStop(s_base):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(TabStop, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def writeBody(self, **KWS):



        ## CHEETAH: main method generated for this template
        trans = KWS.get("trans")
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
        
        #  set is attribs is sorted
        #  set is attribs is sorted
        
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

    sort = True 

    sort = True 

    name = "TabStop"

    desc = "This struct describes drop caps at a paragraph object."

    link = "https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1style_1_1TabStop.html"

    imports = []

    from_imports = [('.tab_align', 'TabAlign')]

    attribs = [    {        "name": "Position",        "type": 'int',        "orig_type": "long",        "lines": ('This field specifies the position of the tabulator in relation to the left border.',)    },    {        "name": "Alignment",        "type": 'TabAlign',        "orig_type": "com.sun.star.style.TabAlign",        "lines": ('This field specifies the alignment of the text range before the tabulator.',)    },    {        "name": "DecimalChar",        "type": 'str',        "orig_type": "char",        "lines": 'This field specifies which delimiter is used for the decimal.'    },    {        "name": "FillChar",        "type": 'str',        "orig_type": "char",        "lines": ('This field specifies the character that is used to fill up the',            'space between the text in the text range and the tabulators.',)    }]

    _mainCheetahMethod_for_TabStop = 'writeBody'

## END CLASS DEFINITION

if not hasattr(TabStop, '_initCheetahAttributes'):
    templateAPIClass = getattr(TabStop,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(TabStop)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=TabStop()).run()



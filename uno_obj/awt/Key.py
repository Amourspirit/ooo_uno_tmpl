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
from _const_base import const_base as c_base

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.6.post2'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 2)
__CHEETAH_genTime__ = 1638259852.3657563
__CHEETAH_genTimestamp__ = 'Tue Nov 30 03:10:52 2021'
__CHEETAH_src__ = '/home/paul/Documents/Projects/Python/Cheeta3/ooo_uno/uno_obj/awt/Key.tmpl'
__CHEETAH_srcLastModified__ = 'Tue Nov 30 03:10:48 2021'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class Key(c_base):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(Key, self).__init__(*args, **KWs)
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
        
        #  set is const_dict is sorted
        #  $from_imports is a tuple eg: $from_imports = [('.tab_align', 'TabAlign')]
        write('''
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

    hex = False

    sort = True 

    flags = False

    name = "Key"

    desc = 'These values are used to specify distinct physical keys, plus some special values used by the macOS implementation.'

    imports = []

    from_imports = []

    link = "https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1Key.html"

    const_dict = {    "NUM0": ('256',),    "NUM1": ('257',),    "NUM2": ('258',),    "NUM3": ('259',),    "NUM4": ('260',),    "NUM5": ('261',),    "NUM6": ('262',),    "NUM7": ('263',),    "NUM8": ('264',),    "NUM9": ('265',),    "A": ('512',),    "B": ('513',),    "C": ('514',),    "D": ('515',),    "E": ('516',),    "F": ('517',),    "G": ('518',),    "H": ('519',),    "I": ('520',),    "J": ('521',),    "K": ('522',),    "L": ('523',),    "M": ('524',),    "N": ('525',),    "O": ('526',),    "P": ('527',),    "Q": ('528',),    "R": ('529',),    "S": ('530',),    "T": ('531',),    "U": ('532',),    "V": ('533',),    "W": ('534',),    "X": ('535',),    "Y": ('536',),    "Z": ('537',),    "F1": ('768',),    "F2": ('769',),    "F3": ('770',),    "F4": ('771',),    "F5": ('772',),    "F6": ('773',),    "F7": ('774',),    "F8": ('775',),    "F9": ('776',),    "F10": ('777',),    "F11": ('778',),    "F12": ('779',),    "F13": ('780',),    "F14": ('781',),    "F15": ('782',),    "F16": ('783',),    "F17": ('784',),    "F18": ('785',),    "F19": ('786',),    "F20": ('787',),    "F21": ('788',),    "F22": ('789',),    "F23": ('790',),    "F24": ('791',),    "F25": ('792',),    "F26": ('793',),    "DOWN": ('1024',),    "UP": ('1025',),    "LEFT": ('1026',),    "RIGHT": ('1027',),    "HOME": ('1028',),    "END": ('1029',),    "PAGEUP": ('1030',),    "PAGEDOWN": ('1031',),    "RETURN": ('1280',),    "ESCAPE": ('1281',),    "TAB": ('1282',),    "BACKSPACE": ('1283',),    "SPACE": ('1284',),    "INSERT": ('1285',),    "DELETE": ('1286',),    "ADD": ('1287',),    "SUBTRACT": ('1288',),    "MULTIPLY": ('1289',),    "DIVIDE": ('1290',),    "POINT": ('1291',),    "COMMA": ('1292',),    "LESS": ('1293',),    "GREATER": ('1294',),    "EQUAL": ('1295',),    "OPEN": ('1296',),    "CUT": ('1297',),    "COPY": ('1298',),    "PASTE": ('1299',),    "UNDO": ('1300',),    "REPEAT": ('1301',),    "FIND": ('1302',),    "PROPERTIES": ('1303',),    "FRONT": ('1304',),    "CONTEXTMENU": ('1305',),    "HELP": ('1306',),    "MENU": ('1307',),    "HANGUL_HANJA": ('1308',),    "DECIMAL": ('1309',),    "TILDE": ('1310',),    "QUOTELEFT": ('1311',),    "CAPSLOCK": ('1312',),    "NUMLOCK": ('1313',),    "SCROLLLOCK": ('1314',),    "DELETE_TO_BEGIN_OF_LINE": ('1536',),    "DELETE_TO_END_OF_LINE": ('1537',),    "DELETE_TO_BEGIN_OF_PARAGRAPH": ('1538',),    "BRACKETLEFT": ('1315',),    "BRACKETRIGHT": ('1316',),    "SEMICOLON": ('1317',),    "QUOTERIGHT": ('1318',),    "DELETE_TO_END_OF_PARAGRAPH": ('1539',(        "The following values don't correspond to physical keys on any keyboard but are used in the macOS implementation of VCL.",        '',        'They correspond to some of the action messages of the NSResponder abstract class.'    )),    "DELETE_WORD_BACKWARD": ('1540',),    "DELETE_WORD_FORWARD": ('1541',),    "INSERT_LINEBREAK": ('1542',),    "INSERT_PARAGRAPH": ('1543',),    "MOVE_WORD_BACKWARD": ('1544',),    "MOVE_WORD_FORWARD": ('1545',),    "MOVE_TO_BEGIN_OF_LINE": ('1546',),    "MOVE_TO_END_OF_LINE": ('1547',),    "MOVE_TO_BEGIN_OF_PARAGRAPH": ('1548',),    "MOVE_TO_END_OF_PARAGRAPH": ('1549',),    "SELECT_BACKWARD": ('1550',),    "SELECT_FORWARD": ('1551',),    "SELECT_WORD_BACKWARD": ('1552',),    "SELECT_WORD_FORWARD": ('1553',),    "SELECT_WORD": ('1554',),    "SELECT_LINE": ('1555',),    "SELECT_PARAGRAPH": ('1556',),    "SELECT_ALL": ('1557',),    "SELECT_TO_BEGIN_OF_LINE": ('1558',),    "SELECT_TO_END_OF_LINE": ('1559',),    "MOVE_TO_BEGIN_OF_DOCUMENT": ('1560',),    "MOVE_TO_END_OF_DOCUMENT": ('1561',),    "SELECT_TO_BEGIN_OF_DOCUMENT": ('1562',),    "SELECT_TO_END_OF_DOCUMENT": ('1563',),    "SELECT_TO_BEGIN_OF_PARAGRAPH": ('1564',),    "SELECT_TO_END_OF_PARAGRAPH": ('1565',)}

    _mainCheetahMethod_for_Key = 'writeBody'

## END CLASS DEFINITION

if not hasattr(Key, '_initCheetahAttributes'):
    templateAPIClass = getattr(Key,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(Key)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=Key()).run()



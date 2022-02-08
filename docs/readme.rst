============
Readme Notes
============

General
=======

Files that start with _ are excluded from make.py

Due to the difficulties with cheetah import of templates that are not in the same
dir a realitive link is created from template folder to each template folder such as:
ln --relative --symbolic '/home/paul/Documents/Projects/Python/Cheeta3/ooo_uno_tmpl/template/_enum_base.py' '/home/paul/Documents/Projects/Python/Cheeta3/ooo_uno_tmpl/uno_obj/style/_enum_base.py'
Links are created automatically for files in the Template folder

template dir can rebuild templates by running make

generating templates is done with make.py.
Example:
python make.py --force-compile true --clean-scratch true

for help run:
python make.py --help

output is copied into build/lo folder with the same dir structure as lo


UNO
===

General info
------------

UNO objects only accept positional arguments. For this reason when calling uno function and methods
only positional args should be used.
The exceptions that allow both positional and keyword args in the ooo.dyn namespace are as follows:

Struct instances
++++++++++++++++

All Pair instnces below are functionally equal.

.. code::

    from ooo.dyn.beans.pair import Pair
    
    pair1 = Pair(First='Hello', Second='World')
    pair2 = Pair("Hello", "World")
    pair3 = Pair()
    pair3.First = 'Hello'
    pair3.Second = 'World'

Parser
======

Config
------

known_json.json
+++++++++++++++

This file contains mappings to full known json data files in the parser/known_json dir.

When a parser find a match it will use the json data found in parser/known_json instead of
generating json.

If a parser command inline includes ``--no-allow-known-json`` or parser parse method
``allow_known_json=False`` then know is ignored and json is built from parser.

In the output dir ``uno_obj`` the json is outputed respecting known by defalut.

In the output dir ``data`` the json is outputed ignoring known by default.
The ``data`` dir is used to generate database and therefore requires raw data
and thus it is preferred to ignore known json.

known_extends.json
++++++++++++++++++

This file contains mappings that are the extends for classes that match full namespace.
When a mapping ends with ._ it indicates that it is a python matching

The following example directs com.sun.star.uno.Exception import form python builtin Exception class.

.. code::

    {
      "com.sun.star.uno.Exception": [
        "Exception._"
      ]
    }

Example full imports. Directs **DatabaseTextField** to only import *TextField* and *DataAwareControlModel*.

.. code::

    {
      "com.sun.star.form.component.DatabaseTextField": [
      "com.sun.star.form.component.TextField",
      "com.sun.star.form.DataAwareControlModel"
      ]
    }

Conda
=====

Set up env
----------

$ conda env create -f  environment.yml

Set up new env
--------------

$ conda create --prefix ./env python=3.10

Write env to Yaml
-----------------

$ conda env export > environment.yml

active from command line
------------------------

$ conda activate $PWD/env

Links of intrest
================

Contains Typedefs

https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1beans.html

Interface:
    deprecated
    https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XVclContainerPeer.html

    Interface with Properties
    https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1animations_1_1XAnimate.html
    
    Interface that inherite more than one interface
    https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1animations_1_1XParallelTimeContainer.html

    Exported Interfaces can be inherited interfaces;
    see: https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1animations_1_1XParallelTimeContainer.html
    see: https://code.woboq.org/libreoffice/libreoffice/workdir/UnoApiHeadersTarget/offapi/normal/com/sun/star/animations/XParallelTimeContainer.hdl.html

===========================================================
LibreOffice python development environment setup guidelines
===========================================================

System Setup
============

At the time of this writting, Libre Office only provides python3 system packages, not pip packages.

Installing on Ubuntu

APT packages
------------

.. code::

    $ sudo apt-get install libreoffice python3 libreoffice-script-provider-python python3-uno uno-libs-private libuno-salhelpergcc3-3 libuno-sal3 libuno-purpenvhelpergcc3-3 libuno-cppuhelpergcc3-3 libuno-cppu3

Virtual Environment
===================

Virtual Environment for this project uses conda.

.. code::

    $ conda env create --prefix ./env -f environment.yml

UNO
===


No uno pip
----------

Uno is required to compile temlates of this project.

As stated there is no uno pip install. However uno is required for this project.

uno in env
----------

There are a couple of ways to setup uno for this project after uno has been install on system.

1. Copy uno file into env subfolder.

.. code::

    $ cp '/usr/lib/python3/dist-packages/uno.py' env/lib/python3.7/site-packages/uno.py

2. Link uno file into env subfolder.

.. code::

    $ ln -s '/usr/lib/python3/dist-packages/uno.py' env/lib/python3.7/site-packages/uno.py

Linking helps future proof incase of updates.
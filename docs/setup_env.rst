LibreOffice python development environment setup guidelines
===========================================================

Limitations
-----------

Currently this project will only work on linux.
However, the output from this project is cross platform.

System Setup
------------

At the time of this writting, Libre Office only provides python3 system packages, not pip packages.

Installing on Ubuntu

APT packages
------------

.. code::

    $ sudo apt-get install libreoffice python3 libreoffice-script-provider-python python3-uno uno-libs-private libuno-salhelpergcc3-3 libuno-sal3 libuno-purpenvhelpergcc3-3 libuno-cppuhelpergcc3-3 libuno-cppu3



Virtual Environment
-------------------

This project use a virtual environment for development purposes.

`Poetry <https://python-poetry.org/>`_ is required to install this project in a development environment.

Set up virtual environment if not existing.

Linux
^^^^^

.. code::

    $ python -m venv ./.venv

Activate virtual environment.

.. code::

    source ./.venv/bin/activate

Install requirements using Poetry.

.. code::

    (.venv) $ poetry install

In order to run test it is essential that ``uno.py`` and ``unohelper.py`` can be imported.
These files are part of the LibreOffice installation.
The location of these files vary depending on OS and other factors.


On Linux what is required to communicate with LibreOffice API it a copy of, or link to ``uno.py`` and ``unohelper.py`` in the virtual environment.
``uno.py`` sets up the necessary code that makes importing from LibreOffice API possible.

This project has a command to accomplish this in the virtual environment on Linux.

.. code::

    (.venv) $ python -m app cmd-link --add

After virtual environment is set up and **activated**, running the above command on Linux will search in known paths for ``uno.py`` and ``unohelper.py``
and create links to files in the current virtual environment.
That's it! Now should be ready for development.

For other options try:

    .. code::

        (.venv) $ python -m app cmd-link -h


Testing Virtual Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^

For a quick test of environment import ``uno`` If there is no import  error you should be good to go.

.. code::

    $ source ./.venv/bin/activate
    (.venv) user@cpu:~/Projects/Python/ooo_uno_tmpl
    $ python
    Python 3.10.5 (main, Jul 31 2022, 06:03:52) [GCC 11.2.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import uno
    >>> 

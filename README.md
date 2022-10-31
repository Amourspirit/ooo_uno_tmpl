# OOO UNO TEMPLATE

Coverts LibreOffice API into Typings and classes.

This is the template project for [ooouno](https://github.com/Amourspirit/python-ooouno) project and [LibreOffice API Typings](https://github.com/Amourspirit/python-types-unopy).

This project reads all [LibreOffice API](https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star.html) and converts into the API into `json` data.
Json data is then used to generate `python` classes and typings through the use of templates.

For help:

```bash
python -m app -h
```

For Extended Help see app.py built in help or see app [docstring](./app.py).

```bash
pydoc app
```

## Quickstart

* `python -m venv ./.venv`
* `source ./.venv/bin/activate`
* `poetry install`
* `python -m app cmd-link --add`

For details on setup see [Setup Environment](docs/setup_env.rst)

## Related Projects

* [OOO Development Tools](https://github.com/Amourspirit/python_ooo_dev_tools)
* [LibreOffice Python UNO Examples](https://github.com/Amourspirit/python-ooouno-ex)
* [ooouno](https://github.com/Amourspirit/python-ooouno)
* [LibreOffice API Typings](https://github.com/Amourspirit/python-types-unopy)
* [ScriptForge Typings](https://github.com/Amourspirit/python-types-scriptforge)
* [Access2base Typings](https://github.com/Amourspirit/python-types-access2base)
* [LibreOffice Python UNO Examples](https://github.com/Amourspirit/python-ooouno-ex)
* [LibreOffice Developer Search](https://github.com/Amourspirit/python_lo_dev_search)
* [LibreOffice UNO Typings](https://github.com/Amourspirit/python-types-uno-script)

# OOO UNO TEMPLATE

Coverts Libre Office Api into Typings and classes.

This is the template project for [ooouno](https://github.com/Amourspirit/python-ooouno) project.

This project reads all [Libre Office Api](https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star.html) and converts into python classes and typings.

For help:

```bash
python -m app -h
```

For Extended Help see app.py build in help.

```bash
$ pydoc app
```

## Quickstart

* Install [requirements](docs/setup_env.rst)
* Activte env: `$ conda activte ./env`
* run app make: `$ python -m make`
* create build/csslo namespace: `$ python -m app data star --css-lo`
* create build/cssdyn namespace: `$ python -m app data star --css-dyn`

**Note:**

Initial full build will take some time

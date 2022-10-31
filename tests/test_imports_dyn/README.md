# Dynamic Test Notes

These test need to be NOT run in debug mode.

There is a issue with debug mode in VS Code that `import uno` completely crashes and exits the test.
This can give the appearance that the test passed when it never got tested at all.

Running test in all available non-debug modes seems to work fine.

## test_imports

`test_imports.py` test all classes in the `ooobuild.lo` directory by import from `ooobuild.dyn` directory.

## test_runitme_imports

`test_runitme_imports.py` test the equivalent `uno` class by importing Dynamically from `ooobuild.dyn`.
Services and type def are not run in these tests as they are not valid `uno` imports.

`test_runitme_imports.py` is also a good test to run to discover missing import from other version of LO.

For instance in LO `7.3` the following are valid imports.

- `from com.sun.star.chart2 import InterpretedData`
- `from com.sun.star.chart2 import XChartTypeTemplate`
- `from com.sun.star.chart2 import XDataInterpreter`
- `from com.sun.star.chart2 import XTransformation`

However in Lo `7.4` these import fail.

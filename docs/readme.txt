Files that start with _ are excluded from make.py

Due to the difficulties with cheetah import of templates that are not in the same
dir a realitive link is created from template folder to each template folder such as:
ln --relative --symbolic '/home/paul/Documents/Projects/Python/Cheeta3/ooo_uno_tmpl/template/_enum_base.py' '/home/paul/Documents/Projects/Python/Cheeta3/ooo_uno_tmpl/uno_obj/style/_enum_base.py'
ln --relative --symbolic '/home/paul/Documents/Projects/Python/Cheeta3/ooo_uno_tmpl/template/_const_base.py' '/home/paul/Documents/Projects/Python/Cheeta3/ooo_uno_tmpl/uno_obj/style/_const_base.py'
ln --relative --symbolic '/home/paul/Documents/Projects/Python/Cheeta3/ooo_uno_tmpl/template/_const.py' '/home/paul/Documents/Projects/Python/Cheeta3/ooo_uno_tmpl/uno_obj/style/_const.py'
ln --relative --symbolic '/home/paul/Documents/Projects/Python/Cheeta3/ooo_uno_tmpl/template/_struct_base.py' '/home/paul/Documents/Projects/Python/Cheeta3/ooo_uno_tmpl/uno_obj/style/_struct_base.py'

template dir can rebuild templates by running make

generating templates is done with make.py.
Example:
python make.py --force-compile true --clean-scratch true

for help run:
python make.py --help

output is copied into scratch folder with the same dir structure as uno_obj

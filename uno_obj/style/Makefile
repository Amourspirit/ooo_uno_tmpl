.SUFFIXES: # Clear the suffix list
.SUFFIXES: .py .tmpl
# https://stackoverflow.com/questions/50963741/how-do-i-use-inheritance-in-cheetah-templates
%.py: %.tmpl
	cheetah compile --nobackup $<
#	python -m compile $@

templates = $(shell echo *.tmpl)
modules = $(patsubst %.tmpl,%.py,$(templates))

.PHONY: all
all: $(modules)
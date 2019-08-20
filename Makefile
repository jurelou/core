PROJECT_NAME=opulence
PYTHON=python3
DOCS_SRC=docs
DOCS_OUTPUT=docs/_build/html
CELERY_LOGLEVEL=--loglevel=info

all:
	cd opulence ; celery -A engine.run.app worker $(CELERY_LOGLEVEL)


test:
	$(PYTHON) -m unittest discover $(PROJECT_NAME)

doc:
	sphinx-build  $(DOCS_SRC) $(DOCS_OUTPUT)

autodoc:
	sphinx-autobuild $(DOCS_SRC) $(DOCS_OUTPUT)


.PHONY: test doc autodoc 

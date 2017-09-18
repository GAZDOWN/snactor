# Minimal makefile for Sphinx documentation
#
## default build operation:
all: clean html 

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = Leapp
SOURCEDIR     = source
BUILDDIR      = build


# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile all dynamic_clean

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean: dynamic_clean

dynamic_clean:
	rm -rf $(SOURCEDIR)/tmp
	rm -rf $(SOURCEDIR)/_dynamic
	find . -iname "__pycache__" -exec rm -rf {} \; || true
	find . -iname "*.pyc" -exec rm -rf {} \; || true

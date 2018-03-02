MAKE             = /usr/bin/make
RST2HTML         = ./bootstrap.py
# STYLESHEET       =

# Migrating to Bootstrap v4.
# Components
#     Dropped the Glyphicons icon font. If you need icons, some options are:
#         the upstream version of Glyphicons
#         Octicons
#         Font Awesome
#         See the Extend page for a list of alternatives. Have additional suggestions? Please open an issue or PR.
# https://getbootstrap.com/docs/4.0/migration/
# https://getbootstrap.com/docs/4.0/extend/icons/

STYLESHEET='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css'
# components.html: STYLESHEET='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'
components.html: STYLESHEET='bootstrap/css/bootstrap.min.css'
carousel.html: STYLESHEET='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css,\
			   bootstrap/css/carousel.css'
# getting-started.html: STYLESHEET='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'
getting-started.html: STYLESHEET='bootstrap/css/bootstrap.min.css'
TEMPLATE=page.tmpl
carousel.html: TEMPLATE=page-carousel.tmpl

RST2HTML_OPTIONS = --strip-comments		\
                   --report=3			\
                   --no-doc-title		\
                   --traceback			\
                   --compact-lists		\
                   --no-toc-backlinks		\
                   --syntax-highlight=short	\
                   --template=$(TEMPLATE)	\
                   --cloak-email-addresses	\
                   --stylesheet=$(STYLESHEET)	\
                   --link-stylesheet		\
		   --no-xml-declaration

SOURCES = $(wildcard doc/*.rst)
TMP = $(subst .rst,.html, $(SOURCES))
OBJECTS = $(subst doc/,, $(TMP))

all:$(OBJECTS)

%.html: doc/%.rst
	@echo "  - $@"
	@$(RST2HTML) $(RST2HTML_OPTIONS) $< $@

clean:
	@-rm -f $(OBJECTS)

distclean: clean
	@-rm -f `find . -name "*~"`

.PHONY: all clean distclean

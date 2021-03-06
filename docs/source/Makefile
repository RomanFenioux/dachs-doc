HTMLTARGET=vo.ari.uni-heidelberg.de:/var/www/docs/DaCHS
RST_SOURCES=data_checklist.rstx howDoI.rstx ref.rstx tutorial.rstx\
	booster.rstx install.rstx stc.rstx processors.rstx adql.rstx\
	votable.rstx commonproblems.rstx tapquery.rstx develNotes.rstx\
	opguide.rstx elemref.rstx templating.rstx
ALL_HTML=index.html $(subst .rstx,.html,$(RST_SOURCES))
HTML_FILES=$(ALL_HTML)
ALL_PDF=$(subst .rstx,.pdf,$(RST_SOURCES))
LATEXOPTS=--documentoptions=11pt,a4paper --stylesheet stylesheet.tex


%.html: %.rstx
	rst2html --template rst2html-template.txt --stylesheet ref.css\
		--link-stylesheet < $<  >$@

%.dvi: %.tex
	latex $<
	latex $<
	rm $*.log

%.ps: %.dvi
	dvips $<

%.pdf: %.tex
	pdflatex $<

%.tex: %.rstx
	rst2latex $(LATEXOPTS) $< > $@

.PHONY: ref.rstx elemref.rstx apidoc-stamp
ref.rstx:
	gavo --debug --traceback gendoc > ref.rstx

elemref.rstx:
	python makeElementIndex.py > $@
	
# Since building apidoc takes forever, you need to manually trigger it
# using make apidoc-stamp
apidoc-stamp:
	touch apidoc-stamp

apidoc: gavo-epydoc.conf apidoc-stamp
	rm -rf apidoc
	epydoc -v --config gavo-epydoc.conf

install: all
	rsync -av *.css gavodoc.js $(HTML_FILES) $(ALL_PDF) $(RST_SOURCES) apidoc $(HTMLTARGET) 

all: $(HTML_FILES) $(ALL_PDF)

clean:
	rm -f $(ALL_HTML)
	rm -f *.log *.aux *.out *.pdf
	rm -f apidoc-stamp

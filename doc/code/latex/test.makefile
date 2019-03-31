ALL_FIGURE_NAMES=$(shell cat test.figlist)
ALL_FIGURES=$(ALL_FIGURE_NAMES:%=%.pdf)

allimages: $(ALL_FIGURES)
	@echo All images exist now. Use make -B to re-generate them.

FORCEREMAKE:

include $(ALL_FIGURE_NAMES:%=%.dep)

%.dep:
	mkdir -p "$(dir $@)"
	touch "$@" # will be filled later.

test-figure0.pdf: 
	pdflatex -halt-on-error -interaction=batchmode -jobname "test-figure0" "\def\tikzexternalrealjob{test}\input{test}"; convert -density 300 -transparent white "test-figure0.pdf" "test-figure0.png"

test-figure0.pdf: test-figure0.md5
test-figure1.pdf: 
	pdflatex -halt-on-error -interaction=batchmode -jobname "test-figure1" "\def\tikzexternalrealjob{test}\input{test}"

test-figure1.pdf: test-figure1.md5

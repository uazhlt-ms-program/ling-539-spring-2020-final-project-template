TEX = pdflatex -interaction nonstopmode
BIB = biber
GS = gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite

PAPER = main
BIBFILE = main
BUNDLE = final-project-proposal.pdf

all: $(PAPER).pdf
	$(GS) -sOutputFile=$(BUNDLE) $(PAPER).pdf

$(PAPER).pdf: $(PAPER).bbl $(PAPER).tex
	$(TEX) $(PAPER)
	$(TEX) $(PAPER)

$(PAPER).bbl: $(PAPER).aux
	$(BIB) $(PAPER)

$(PAPER).aux: $(BIBFILE).bib
	$(TEX) $(PAPER).tex
	$(TEX) $(PAPER).tex

view: $(BUNDLE)
	open $(BUNDLE)

spell:
	ispell *.tex

clean:
	rm -fv *.aux *.log *.bbl *.blg *.toc *.out *.lot *.lof *.run.xml main-blx.bib $(PAPER).pdf $(BUNDLE)

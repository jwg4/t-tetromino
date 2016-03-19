all: every_square.pdf

clean:
	rm *.pdf *.aux *.log *.bbl *.blg *.dvi

every_square.aux: every_square.tex
	latex every_square.tex

every_square.blb: every_square.aux polyomino.bib
	bibtex every_square.tex

every_square.pdf: every_square.bib every_square.tex
	pdflatex every_square.tex

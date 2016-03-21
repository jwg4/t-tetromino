all: every_square.pdf

clean:
	rm -f *.pdf *.aux *.log *.bbl *.blg *.dvi

every_square.aux: every_square.tex lshaped_image.tex
	latex every_square.tex

every_square.blb: every_square.aux polyomino.bib
	bibtex every_square

every_square.pdf: every_square.blb every_square.tex lshaped_image.tex
	pdflatex every_square.tex

lshaped_image.tex: lshaped.py
	python lshaped.py > lshaped_image.tex

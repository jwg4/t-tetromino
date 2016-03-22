all: every_square.pdf

clean:
	rm -f *.pdf *.aux *.log *.bbl *.blg *.dvi

every_square.aux: every_square.tex $(IMAGES)
	latex every_square.tex

every_square.blb: every_square.aux polyomino.bib
	bibtex every_square

every_square.pdf: every_square.blb every_square.tex $(IMAGES)
	pdflatex every_square.tex

IMAGES = lshaped_image.tex cropped_image.tex five_image.tex

lshaped_image.tex: lshaped.py drawings.py
	python lshaped.py > lshaped_image.tex

cropped_image.tex: cropped.py drawings.py
	python cropped.py > cropped_image.tex

five_image.tex: five.py drawings.py
	python five.py > five_image.tex

all: every_square.pdf gap_number.pdf

clean:
	rm -f *.pdf *.aux *.log *.bbl *.blg *.dvi

IMAGES = lshaped_image.tex cropped_image.tex five_image.tex ones_image.tex threes_image.tex strips_image.tex extending_image.tex

every_square.aux: every_square.tex $(IMAGES)
	latex every_square.tex

every_square.blb: every_square.aux polyomino.bib
	bibtex every_square

every_square.pdf: every_square.blb every_square.tex $(IMAGES)
	pdflatex every_square.tex

gap_number.aux: gap_number.tex $(IMAGES)
	latex gap_number.tex

gap_number.blb: gap_number.aux polyomino.bib
	bibtex gap_number

gap_number.pdf: gap_number.blb gap_number.tex $(IMAGES)
	pdflatex gap_number.tex

lshaped_image.tex: lshaped.py drawings.py
	python lshaped.py > lshaped_image.tex

extending_image.tex: extending.py drawings.py
	python extending.py > extending_image.tex

cropped_image.tex: cropped.py drawings.py
	python cropped.py > cropped_image.tex

five_image.tex: five.py drawings.py
	python five.py > five_image.tex

ones_image.tex: ones.py drawings.py
	python ones.py > ones_image.tex

threes_image.tex: threes.py drawings.py
	python threes.py > threes_image.tex

strips_image.tex: strips.py drawings.py
	python strips.py > strips_image.tex

all: every_square.pdf gap_number.pdf

clean:
	rm -f *.pdf *.aux *.log *.bbl *.blg *.dvi

IMAGES = lshaped_image.tex cropped_image.tex five_image.tex ones_image.tex threes_image.tex strips_image.tex extending_image.tex

%.aux: %.tex $(IMAGES)
	latex $<

%.blb: %.aux polyomino.bib
	bibtex $<

%.pdf: %.blb %.tex $(IMAGES)
	pdflatex $<

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

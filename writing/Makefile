all: every_square.pdf gap_number.pdf

clean:
	rm -f *.pdf *.aux *.log *.bbl *.blg *.dvi

IMAGES = lshaped_image.tex cropped_image.tex five_image.tex ones_image.tex threes_image.tex strips_image.tex extending_image.tex

%.aux: %.tex $(IMAGES)
	latex $<

%.bbl: %.aux polyomino.bib
	bibtex $<

%.pdf: %.tex %.bbl $(IMAGES)
	pdflatex $<

%_image.tex: %.py drawings.py
	python $< > $@

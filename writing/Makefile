all: every_square.pdf gap_number.pdf

clean:
	rm -f *.pdf *.aux *.log *.bbl *.blg *.dvi
	rm -rf arxiv/*

IMAGES = lshaped_image.tex cropped_image.tex five_image.tex ones_image.tex threes_image.tex strips_image.tex extending_image.tex six_image.tex
ES_IMAGES = cropped_image.tex five_image.tex ones_image.tex threes_image.tex six_image.tex

every_square.aux: every_square.tex $(ES_IMAGES)
	latex $<

gap_number.aux: gap_number.tex $(IMAGES) rectangle_table.tex
	latex $<

%.bbl: %.aux polyomino.bib
	bibtex $<

every_square.pdf: every_square.tex every_square.bbl $(ES_IMAGES)
	latex $<
	pdflatex $<

gap_number.pdf: gap_number.tex gap_number.bbl $(IMAGES) rectangle_table.tex
	latex $<
	pdflatex $<

%_image.tex: %.py drawings.py
	python $< > $@

rectangle_table.tex: table.py rectangle_data.yml
	python table.py rectangle_data.yml > $@

arxiv: arxiv/every_square arxiv/gap_number

arxiv/every_square: every_square.tex every_square.bbl $(ES_IMAGES)
	mkdir -p $@
	cp every_square.tex every_square.bbl $(ES_IMAGES) $@

arxiv/every_square: every_square.tex every_square.bbl rectangle_table.tex $(IMAGES)
	mkdir -p $@
	cp every_square.tex every_square.bbl $(IMAGES) rectangle_table.tex $@

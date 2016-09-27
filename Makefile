all: results test article new_results code

.PHONY: test article results new_results code

code:  code_output
	cd code_output/
	python -m unittest discover -p _test*.py

results: Strip13Corner_results

Strip13Corner_results: Strip13Corner
	./Strip13Corner > Strip13Corner_results

Strip13Corner: Strip13Corner.h
	ln -sf ../../Strip13Corner.h Dantz/Dantz/DantzLoad.h
	$(MAKE) -C Dantz/Dantz
	cp Dantz/Dantz/DantzLoad Strip13Corner

Strip13Corner.h: make_strip.py shapes.py
	python make_strip.py > Strip13Corner.h

new_results: Strip15Corner_results

Strip15Corner_results: Dantz/Dantz/DantzCSV
	Dantz/Dantz/DantzCSV names15.txt rows15.txt > Strip15Corner_results

Dantz/Dantz/DantzCSV:
	$(MAKE) -C Dantz/Dantz

names15.txt rows15.txt: make_csv.py shapes.py
	python make_csv.py
	mv names.txt names15.txt
	mv rows.txt rows15.txt

DantzLoad17x17.h: make_header.py
	python make_header.py 17 17 > DantzLoad17x17.h

test:
	python -m unittest discover

article:
	$(MAKE) -C writing

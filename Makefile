all: results test article

.PHONY: test article results

results: Strip13Corner_results

Strip13Corner_results: Strip13Corner
	travis_wait ./Strip13Corner > Strip13Corner_results

Strip13Corner: Strip13Corner.h
	ln -sf ../../Strip13Corner.h Dantz/Dantz/DantzLoad.h
	$(MAKE) -C Dantz/Dantz
	cp Dantz/Dantz/DantzLoad Strip13Corner

Strip13Corner.h: make_strip.py shapes.py
	python make_strip.py > Strip13Corner.h

DantzLoad17x17.h: make_header.py
	python make_header.py 17 17 > DantzLoad17x17.h

test:
	python -m unittest discover

article:
	$(MAKE) -C writing

Strip13Corner.h: make_strip.py shapes.py
	python make_strip.py > Strip13Corner.h

DantzLoad17x17.h: make_header.py
	python make_header.py 17 17 > DantzLoad17x17.h

test:
	python unittest -m discover

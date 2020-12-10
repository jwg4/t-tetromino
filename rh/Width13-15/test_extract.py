import logging

from pytest import mark

from extract import extract_pattern_by_number
from extract import extract_tiles_by_number


def test_get_correct_pattern():
    id_ = 67136011
    height = 7
    source_filename = "examples/9.txt"
    expected_filename = "examples/9_67136011.txt"
    with open(expected_filename) as expected_f:
        expected = expected_f.read()

    with open(source_filename) as source_f:
        pattern = extract_pattern_by_number(source_f, id_, height)

    assert pattern == expected


def test_get_correct_pattern_by_height():
    id_ = 671217151
    height = 7
    source_filename = "examples/17.txt"
    expected_filename = "examples/17_671217151_7.txt"
    with open(expected_filename) as expected_f:
        expected = expected_f.read()

    with open(source_filename) as source_f:
        pattern = extract_pattern_by_number(source_f, id_, height)

    assert pattern == expected


def test_get_correct_pattern_by_height_2():
    id_ = 671217151
    height = 11
    source_filename = "examples/17.txt"
    expected_filename = "examples/17_671217151_11.txt"
    with open(expected_filename) as expected_f:
        expected = expected_f.read()

    with open(source_filename) as source_f:
        pattern = extract_pattern_by_number(source_f, id_, height)

    assert pattern == expected


def test_extract_tiles(caplog):
    caplog.set_level(logging.DEBUG)
    id_ = 67136011
    source_filename = "examples/9.txt"

    with open(source_filename) as source_f:
        tiles = list(extract_tiles_by_number(source_f, id_, 7))

    assert len(tiles) == 21

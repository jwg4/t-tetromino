from shape_dict import ShapeDict


def test_create_empty():
    sut = ShapeDict()
    assert list(sut.components) == []


def test_create_single_node():
    sut = ShapeDict()
    sut.add_new("foo")

    assert list(sut.components) == [set(["foo"])]


def test_create_two_connected_nodes():
    sut = ShapeDict()
    sut.add_new("foo")
    sut.add_connected("bar", "foo")

    assert list(sut.components) == [set(["foo", "bar"])]


def test_create_two_nodes_add_connection():
    sut = ShapeDict()
    sut.add_new("foo")
    sut.add_new("bar")
    sut.add_connection("bar", "foo")

    assert list(sut.components) == [set(["foo", "bar"])]


def test_create_two_edges_add_connection():
    sut = ShapeDict()
    sut.add_new("foo")
    sut.add_new("bar")
    sut.add_connected("baz", "bar")
    sut.add_connected("asdf", "foo")
    sut.add_connection("bar", "foo")

    assert list(sut.components) == [set(["foo", "bar", "baz", "asdf"])]


def test_create_two_edges_add_connection_2():
    sut = ShapeDict()
    sut.add_new("foo")
    sut.add_new("bar")
    sut.add_connected("baz", "bar")
    sut.add_connected("asdf", "foo")
    sut.add_connection("bar", "asdf")

    assert list(sut.components) == [set(["foo", "bar", "baz", "asdf"])]


def test_create_two_edges_add_connection_3():
    sut = ShapeDict()
    sut.add_new("foo")
    sut.add_new("bar")
    sut.add_connected("baz", "bar")
    sut.add_connected("asdf", "foo")
    sut.add_connection("baz", "foo")

    assert list(sut.components) == [set(["foo", "bar", "baz", "asdf"])]


def test_create_two_edges_add_connection_4():
    sut = ShapeDict()
    sut.add_new("foo")
    sut.add_new("bar")
    sut.add_connected("baz", "bar")
    sut.add_connected("asdf", "foo")
    sut.add_connection("baz", "asdf")

    assert list(sut.components) == [set(["foo", "bar", "baz", "asdf"])]


def test_create_two_single_nodes():
    sut = ShapeDict()
    sut.add_new("foo")
    sut.add_new("bar")

    assert list(sut.components) == [set(["foo"]), set(["bar"])]


def test_create_four_connected_nodes():
    sut = ShapeDict()
    sut.add_new("foo")
    sut.add_connected("bar", "foo")
    sut.add_connected("baz", "bar")
    sut.add_connected("asdf", "bar")

    assert list(sut.components) == [set(["foo", "bar", "baz", "asdf"])]


def test_complex_graph():
    sut = ShapeDict()
    sut.add_new((0, 0))
    sut.add_new((1, 0))
    sut.add_new((2, 0))
    sut.add_new((3, 0))
    sut.add_new((4, 0))
    sut.add_new((5, 0))
    sut.add_new((6, 0))
    sut.add_new((7, 0))
    sut.add_new((8, 0))
    sut.add_new((9, 0))
    sut.add_new((10, 0))
    sut.add_new((11, 0))
    sut.add_new((12, 0))
    sut.add_connected((2, 0), (1, 0))
    sut.add_connected((3, 0), (2, 0))
    sut.add_connected((6, 0), (5, 0))
    sut.add_connected((7, 0), (6, 0))
    sut.add_connected((11, 0), (10, 0))
    sut.add_connected((12, 0), (11, 0))
    sut.add_connected((0, 1), (0, 0))
    sut.add_new((1, 1))
    sut.add_connected((2, 1), (2, 0))
    sut.add_new((3, 1))
    sut.add_connected((4, 1), (4, 0))
    sut.add_new((5, 1))
    sut.add_connected((6, 1), (6, 0))
    sut.add_new((7, 1))
    sut.add_connected((8, 1), (8, 0))
    sut.add_connected((9, 1), (9, 0))
    sut.add_new((10, 1))
    sut.add_connected((11, 1), (11, 0))
    sut.add_new((12, 1))
    sut.add_connected((1, 1), (0, 1))
    sut.add_connected((4, 1), (3, 1))
    sut.add_connected((5, 1), (4, 1))
    sut.add_connected((8, 1), (7, 1))
    sut.add_connected((10, 1), (9, 1))
    sut.add_connected((0, 2), (0, 1))
    sut.add_new((1, 2))
    sut.add_new((2, 2))
    sut.add_new((3, 2))
    sut.add_new((4, 2))
    sut.add_new((5, 2))
    sut.add_new((6, 2))
    sut.add_new((7, 2))
    sut.add_connected((8, 2), (8, 1))
    sut.add_connected((9, 2), (9, 1))
    sut.add_new((10, 2))
    sut.add_new((11, 2))
    sut.add_connected((12, 2), (12, 1))
    sut.add_connected((2, 2), (1, 2))
    sut.add_connected((3, 2), (2, 2))
    sut.add_connected((6, 2), (5, 2))
    sut.add_connected((7, 2), (6, 2))
    sut.add_connected((12, 2), (11, 2))
    sut.add_new((0, 3))
    sut.add_new((1, 3))
    sut.add_connected((2, 3), (2, 2))
    sut.add_new((3, 3))
    sut.add_connected((4, 3), (4, 2))
    sut.add_new((5, 3))
    sut.add_connected((6, 3), (6, 2))
    sut.add_new((7, 3))
    sut.add_new((8, 3))
    sut.add_new((9, 3))
    sut.add_connected((10, 3), (10, 2))
    sut.add_new((11, 3))
    sut.add_connected((12, 3), (12, 2))
    sut.add_connected((4, 3), (3, 3))
    sut.add_connected((5, 3), (4, 3))
    sut.add_connected((8, 3), (7, 3))
    sut.add_connected((9, 3), (8, 3))
    sut.add_connected((11, 3), (10, 3))
    sut.add_new((0, 4))
    sut.add_connected((1, 4), (1, 3))
    sut.add_new((2, 4))
    sut.add_new((3, 4))
    sut.add_new((4, 4))
    sut.add_new((5, 4))
    sut.add_new((6, 4))
    sut.add_new((7, 4))
    sut.add_connected((8, 4), (8, 3))
    sut.add_new((9, 4))
    sut.add_connected((10, 4), (10, 3))
    sut.add_new((11, 4))
    sut.add_new((12, 4))
    sut.add_connected((1, 4), (0, 4))
    sut.add_connected((2, 4), (1, 4))
    sut.add_connected((5, 4), (4, 4))
    sut.add_connected((6, 4), (5, 4))
    sut.add_new((0, 5))
    sut.add_new((1, 5))
    sut.add_new((2, 5))
    sut.add_connected((3, 5), (3, 4))
    sut.add_new((4, 5))
    sut.add_connected((5, 5), (5, 4))
    sut.add_new((6, 5))
    sut.add_connected((7, 5), (7, 4))
    sut.add_new((8, 5))
    sut.add_connected((9, 5), (9, 4))
    sut.add_new((10, 5))
    sut.add_connected((11, 5), (11, 4))
    sut.add_new((12, 5))
    sut.add_connected((1, 5), (0, 5))
    sut.add_connected((2, 5), (1, 5))
    sut.add_connected((4, 5), (3, 5))
    sut.add_connected((7, 5), (6, 5))
    sut.add_connected((8, 5), (7, 5))
    sut.add_connected((10, 5), (9, 5))
    sut.add_connected((12, 5), (11, 5))
    sut.add_new((0, 6))
    sut.add_connected((1, 6), (1, 5))
    sut.add_new((2, 6))
    sut.add_connected((3, 6), (3, 5))
    sut.add_new((4, 6))
    sut.add_new((5, 6))
    sut.add_new((6, 6))
    sut.add_new((7, 6))
    sut.add_new((8, 6))
    sut.add_connected((9, 6), (9, 5))
    sut.add_new((10, 6))
    sut.add_connected((11, 6), (11, 5))
    sut.add_new((12, 6))
    sut.add_connection((5, 6), (4, 6))
    sut.add_connection((6, 6), (5, 6))
    sut.add_connection((7, 6), (6, 6))
    sut.add_connection((8, 6), (7, 6))
    sut.add_connected((0, 7), (0, 6))
    sut.add_new((1, 7))
    sut.add_connected((2, 7), (2, 6))
    sut.add_new((3, 7))
    sut.add_connected((4, 7), (4, 6))
    sut.add_connected((5, 7), (5, 6))
    sut.add_connected((6, 7), (6, 6))
    sut.add_connected((7, 7), (7, 6))
    sut.add_connected((8, 7), (8, 6))
    sut.add_new((9, 7))
    sut.add_connected((10, 7), (10, 6))
    sut.add_new((11, 7))
    sut.add_connected((12, 7), (12, 6))
    sut.add_connection((1, 7), (0, 7))
    sut.add_connection((3, 7), (2, 7))
    sut.add_connection((4, 7), (3, 7))
    sut.add_connection((5, 7), (4, 7))
    sut.add_connection((6, 7), (5, 7))
    assert list(sut.components) is not None

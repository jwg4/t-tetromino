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
    sut.add_new((0, 6))
    sut.add_new((2, 6))
    sut.add_new((4, 6))
    sut.add_new((5, 6))
    sut.add_new((6, 6))
    sut.add_new((7, 6))
    sut.add_new((8, 6))
    sut.add_new((10, 6))
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


def test_complex_graph_component():
    sut = ShapeDict()
    sut.add_new((2, 6))
    sut.add_new((4, 6))
    sut.add_new((5, 6))
    sut.add_new((6, 6))
    sut.add_new((7, 6))
    sut.add_new((8, 6))
    sut.add_connection((5, 6), (4, 6))
    sut.add_connection((6, 6), (5, 6))
    sut.add_connection((7, 6), (6, 6))
    sut.add_connection((8, 6), (7, 6))
    sut.add_connected((2, 7), (2, 6))
    sut.add_new((3, 7))
    sut.add_connected((4, 7), (4, 6))
    sut.add_connected((5, 7), (5, 6))
    sut.add_connected((6, 7), (6, 6))
    sut.add_connected((7, 7), (7, 6))
    sut.add_connected((8, 7), (8, 6))
    sut.add_connection((3, 7), (2, 7))
    sut.add_connection((4, 7), (3, 7))
    sut.add_connection((5, 7), (4, 7))
    sut.add_connection((6, 7), (5, 7))
    assert list(sut.components) is not None


def test_mu_shaped_graph():
    sut = ShapeDict()
    sut.add_new((2, 6))
    sut.add_new((4, 6))
    sut.add_new((5, 6))
    sut.add_new((6, 6))
    sut.add_connection((5, 6), (4, 6))
    sut.add_connection((6, 6), (5, 6))
    sut.add_connected((2, 7), (2, 6))
    sut.add_new((3, 7))
    sut.add_connected((4, 7), (4, 6))
    sut.add_connected((5, 7), (5, 6))
    sut.add_connected((6, 7), (6, 6))
    sut.add_connection((3, 7), (2, 7))
    sut.add_connection((4, 7), (3, 7))
    sut.add_connection((5, 7), (4, 7))
    sut.add_connection((6, 7), (5, 7))
    assert list(sut.components) is not None


def test_u_shaped_graph():
    sut = ShapeDict()
    sut.add_new((2, 6))
    sut.add_new((4, 6))
    sut.add_new((5, 6))
    sut.add_connection((5, 6), (4, 6))
    sut.add_connected((2, 7), (2, 6))
    sut.add_new((3, 7))
    sut.add_connected((4, 7), (4, 6))
    sut.add_connected((5, 7), (5, 6))
    sut.add_connection((3, 7), (2, 7))
    sut.add_connection((4, 7), (3, 7))
    sut.add_connection((5, 7), (4, 7))
    assert list(sut.components) is not None

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

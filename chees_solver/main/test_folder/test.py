"""

tests for all chess figures from main.figure.py

"""

import pytest
from chees_solver.main.figure import Pawn, Bishop, King, Knight, Rook, Queen


@pytest.fixture()
def prepareddata_Pawn():
    Data_Pawn = Pawn("a2")

    yield Data_Pawn


def test_Pawn_list_available_moves(prepareddata_Pawn: Pawn):
    assert prepareddata_Pawn.list_available_moves() == ["a3", "a4"]


def test_Pawn_validate_move(prepareddata_Pawn: Pawn):
    assert prepareddata_Pawn.validate_move("a3") == "This move is available"


def test_Pawn_error_list_available_moves(prepareddata_Pawn: Pawn):
    with pytest.raises(AssertionError):
        assert prepareddata_Pawn.list_available_moves() == 6


def test_Pawn_error_validate_move(prepareddata_Pawn: Pawn):
    with pytest.raises(AssertionError):
        assert prepareddata_Pawn.validate_move("a3") == "53"


@pytest.fixture()
def prepareddata_King():
    Data = King("c6")
    yield Data


def test_King_list_available_moves(prepareddata_King: King):
    assert prepareddata_King.list_available_moves() == [
        "b1",
        "b2",
        "b3",
        "c1",
        "c2",
        "c3",
        "d1",
        "d2",
        "d3",
    ]


def test_King_validate_move(prepareddata_King: King):
    assert prepareddata_King.validate_move("a3") == "You can't make this move"


def test_King_error_list_available_moves(prepareddata_King: King):
    with pytest.raises(AssertionError):
        assert prepareddata_King.list_available_moves() == 6


def test_King_error_validate_move(prepareddata_King: King):
    with pytest.raises(AssertionError):
        assert prepareddata_King.validate_move("a3") == 6


@pytest.fixture()
def prepareddata_Bishop():
    Data = Bishop("d4")
    yield Data


def test_Bishop_list_available_moves(prepareddata_Bishop: Bishop):
    assert prepareddata_Bishop.list_available_moves() == [
        "a1",
        "a7",
        "b2",
        "b6",
        "c3",
        "c5",
        "e3",
        "e5",
        "f2",
        "f6",
        "g1",
        "g7",
        "h8",
    ]


def test_Bishop_validate_move(prepareddata_Bishop: Bishop):
    assert prepareddata_Bishop.validate_move("a7") == "This move is available"


def test_Bishop_error_list_available_moves(prepareddata_Bishop: Bishop):
    with pytest.raises(AssertionError):
        assert prepareddata_Bishop.list_available_moves() == 6


def test_Bishop_error_validate_move(prepareddata_Bishop: Bishop):
    with pytest.raises(AssertionError):
        assert prepareddata_Bishop.validate_move("a3") == 6


@pytest.fixture()
def prepareddata_Knight():
    Data = Knight("b5")
    yield Data


def test_Knight_list_available_moves(prepareddata_Knight: Knight):
    assert prepareddata_Knight.list_available_moves() == [
        "a3",
        "a7",
        "c3",
        "c7",
        "d4",
        "d6",
    ]


def test_Knight_validate_move(prepareddata_Knight: Knight):
    assert prepareddata_Knight.validate_move("a3") == "This move is available"


def test_Knight_error_list_available_moves(prepareddata_Knight: Knight):
    with pytest.raises(AssertionError):
        assert prepareddata_Knight.list_available_moves() == 6


def test_Knight_error_validate_move(prepareddata_Knight: Knight):
    with pytest.raises(AssertionError):
        assert prepareddata_Knight.validate_move("a3") == "bz"


@pytest.fixture()
def prepareddata_Rook():
    Data = Rook("b5")
    yield Data


def test_Rook_list_available_moves(prepareddata_Rook: Rook):
    assert prepareddata_Rook.list_available_moves() == [
        "a5",
        "b1",
        "b2",
        "c5",
        "b3",
        "d5",
        "b4",
        "e5",
        "f5",
        "b6",
        "g5",
        "b7",
        "h5",
        "b8",
    ]


def test_Rook_validate_move(prepareddata_Rook: Rook):
    assert prepareddata_Rook.validate_move("a3") == "You can't make this move"


def test_Rook_error_list_available_moves(prepareddata_Rook: Rook):
    with pytest.raises(AssertionError):
        assert prepareddata_Rook.list_available_moves() == 6


def test_Rook_error_validate_move(prepareddata_Rook: Rook):
    with pytest.raises(AssertionError):
        assert prepareddata_Rook.validate_move("a3") == "bibo"


@pytest.fixture()
def prepareddata_Queen():
    Data = Queen("b8")
    yield Data


def test_Queen_list_available_moves(prepareddata_Queen: Queen):
    assert prepareddata_Queen.list_available_moves() == [
        "a7",
        "a8",
        "b1",
        "b2",
        "b3",
        "b4",
        "b5",
        "b6",
        "b7",
        "c7",
        "c8",
        "d6",
        "d8",
        "e5",
        "e8",
        "f4",
        "f8",
        "g3",
        "g8",
        "h2",
        "h8",
    ]


def test_Queen_validate_move(prepareddata_Queen: Queen):
    assert prepareddata_Queen.validate_move("a3") == "You can't make this move"


def test_Queen_error_list_available_moves(prepareddata_Queen: Queen):
    with pytest.raises(AssertionError):
        assert prepareddata_Queen.list_available_moves() == 6


def test_Queen_error_validate_move(prepareddata_Queen: Queen):
    with pytest.raises(AssertionError):
        assert prepareddata_Queen.validate_move("a3") == 6

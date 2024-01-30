import pytest

from app.main import solve


@pytest.mark.parametrize(
    "a,b,c,expected_result",
    [
        (1, 0, 1, []),  # pt. 3
        (1, 0, -1, [1, -1]),  # pt. 5
        (1, 2, 1, [-1]),  # pt. 7
    ],
)
def test_solve(a, b, c, expected_result):
    a, b, c = (
        float(a),
        float(b),
        float(c),
    )
    assert solve(a, b, c) == [float(x) for x in expected_result]


# pt. 9
def test_solve_exception():
    with pytest.raises(ValueError):
        solve(float(0), float(2), float(3))


# pt. 13
@pytest.mark.parametrize(
    "a,b,c",
    [
        (float("inf"), 1, 1),
        (1, float("inf"), 1),
        (2, 2, float("inf")),
        (2, 2, float("nan")),
        (1, float("nan"), 1),
        (float("nan"), 1, 1),
        (float("-inf"), 1, 1),
        (1, float("-inf"), 1),
        (2, 2, float("-inf")),
    ],
)
def test_inf_values_raises(a, b, c):
    with pytest.raises(ValueError):
        solve(a, b, c)

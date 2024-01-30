import math


def solve(a: float, b: float, c: float, eps: float = 1e-5) -> list[float]:
    if any(
        [
            math.isnan(a),
            math.isnan(b),
            math.isnan(c),
            math.isinf(a),
            math.isinf(b),
            math.isinf(c),
        ]
    ):
        raise ValueError

    d = b**2 - 4 * a * c

    if abs(a) < eps:
        raise ValueError

    if d < eps:
        return []
    if d > 0:
        return [(-b + d**0.5) / (2 * a), (-b - d**0.5) / (2 * a)]

    return [-b / (2 * a)]

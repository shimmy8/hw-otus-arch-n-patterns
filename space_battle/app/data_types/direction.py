class Direction:
    direction: int
    dicrections_number: int

    def __init__(self, direction: int, dicrections_number: int) -> None:
        self.direction = direction
        self.dicrections_number = dicrections_number

    def to_next(self, next_direction: int) -> "Direction":
        self.direction = (self.direction + next_direction) % self.dicrections_number
        return self

    @property
    def anlge(self) -> int:
        return int(self.direction / 360) * self.dicrections_number

    def __str__(self) -> str:
        return f"{self.direction}/{self.dicrections_number}"

    def __repr__(self) -> str:
        return f"Direction({self.direction}, {self.dicrections_number})"

    def __eq__(self, other: "Direction") -> bool:
        return (
            self.direction == other.direction
            and self.dicrections_number == other.dicrections_number
        )

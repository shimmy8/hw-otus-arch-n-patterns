class Vector:
    components: list[int]

    def __init__(self, *components: list[int]):
        self.components = components

    def __add__(self, vector2: "Vector") -> "Vector":
        if len(self.components) != len(vector2.components):
            raise ValueError("Can't add vectors with different components length")
        result_components = []
        for ind, val in enumerate(self.components):
            result_components.append(self.components[ind] + vector2.components[ind])
        return Vector(*result_components)

    def __str__(self):
        return str(self.components)

    def __repr__(self):
        return f"Vector({self.components})"

    def __eq__(self, vector2: "Vector") -> bool:
        return self.components == vector2.components

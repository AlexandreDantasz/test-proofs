from __future__ import annotations

class Vector:
    def __init__(self, values: list):
        self.values = values

    def _its_valid_operation(self, other: Vector):
        return (len(self.values) == len(other.values))
        

    def __add__(self, other: Vector):
        if not self._its_valid_operation(other):
            raise ValueError("Vectors must be of the same length to add.") # AI's snippet, but it's obvious

        combined_values = zip(self.values, other.values) # learn from snippet

        result: list = []
        for a, b in combined_values:
            result.append(a + b)

        return Vector(result)

    def __sub__(self, other: Vector):
        if not self._its_valid_operation(other):
            raise ValueError("Vectors must be of the same length to subtract.") # AI's snippet, but it's obvious

        combined_values = zip(self.values, other.values) # learn from snippet

        result: list = []
        for a, b in combined_values:
            result.append(a - b)

        return Vector(result)

    def __mul__(self, other: Vector): # Scalar product
        if not self._its_valid_operation(other):
            raise ValueError("Vectors must be of the same length to multiply.") # AI's snippet, but it's obvious

        combined_values = zip(self.values, other.values) # learn from snippet

        result: list = []
        for a, b in combined_values:
            result.append(a * b)

        return sum(result)

    def __mul__(self, scalar: float): # Scalar multiplication
        result: list = []
        
        for a in self.values:
            result.append(a * scalar)

        return Vector(result)
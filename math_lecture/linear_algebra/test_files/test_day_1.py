from math_lecture.linear_algebra.day_1 import Vector


def test_vector_addition_otimist():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    result = v1 + v2
    assert result.values == [5, 7, 9]

def test_vector_addition_pessimist():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5])
    try:
        result = v1 + v2
    except ValueError as e:
        assert str(e) == "Vectors must be of the same length to add."

def test_vector_addition_edge_case():
    v1 = Vector([])
    v2 = Vector([])
    result = v1 + v2
    assert result.values == []

def test_vector_addition_with_negative_numbers(): # snippet
    v1 = Vector([-1, -2, -3])
    v2 = Vector([-4, -5, -6])
    result = v1 + v2
    assert result.values == [-5, -7, -9]

def test_vector_addition_one_element_vector():
    v1: Vector = Vector([1])
    v2: Vector = Vector([2])
    result: Vector = v1 + v2
    assert result.values == [3]

def test_vector_subtraction_otimist_first_position():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    result = v1 - v2
    assert result.values == [-3, -3, -3]

def test_vector_subtraction_otimist_second_position():
    v1 = Vector([4, 5, 6])
    v2 = Vector([1, 2, 3])
    result = v1 - v2
    assert result.values == [3, 3, 3]

def test_vector_subtraction_edge_case():
    v1 = Vector([])
    v2 = Vector([])
    result = v1 - v2
    assert result.values == []

def test_vector_subtraction_with_different_lengths():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5])
    try:
        result = v1 - v2
    except ValueError as e:
        assert str(e) == "Vectors must be of the same length to subtract."
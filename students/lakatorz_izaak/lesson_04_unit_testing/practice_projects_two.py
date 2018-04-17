# Write test module with 3 unit tests for distance() from The length of the
# segment exercise from previous exercise Snakify / Lesson 8 / Problems:

import length_of_segment
import pytest


def test_if_raises_type_error_for_none():
    with pytest.raises(TypeError):
        length_of_segment.distance(None)


def test_if_raises_value_error_for_string():
    with pytest.raises(ValueError):
        length_of_segment.distance(1, 0, 1, 'aoeu')


def test_corner_cases():
    # Zero length
    assert length_of_segment.distance(3, 5, 3,
                                      5) == 0, 'Non-zero value, should be ' \
                                               'zero. '

    zero_length_dist = length_of_segment.distance(3, 5, 3, 5)

    assert zero_length_dist == 0, 'Non-zero value, should be zero.'

    negative_coordinates_dist = length_of_segment.distance(-5, -1, -1, -4)
    assert negative_coordinates_dist == 5, 'Expected negative coordinates.'

    only_vertical_dist = length_of_segment.distance(3, 7, 3, 1)
    assert only_vertical_dist == 6, 'Distance should be equal to 6.'

    only_horizontal_dist = length_of_segment.distance(7, 3, 1, 3)
    assert only_horizontal_dist == 6, 'Distance should be equal 6.'

    typical_conditions_dist = length_of_segment.distance(5, 3, 7, 2)
    assert typical_conditions_dist

    first_order = length_of_segment.distance(3, 1, 4, 2)
    second_order = length_of_segment.distance(4, 2, 3, 1)
    assert first_order == second_order, 'Not equal after switching order. '

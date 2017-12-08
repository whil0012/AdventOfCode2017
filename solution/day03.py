import unittest
import os
import math


class TestDay03(unittest.TestCase):
    def test_get_nearest_odd_square_root_when74_returns7(self):
        actual = get_nearest_odd_square_root(74)
        self.assertEquals(actual, 7)

    def test_get_coordinate_of_square_when7_returns3AndNegative3(self):
        actual = get_coordinate_of_square(7)
        self.assertEquals(actual, (3, -3))

    def test_get_coordinates_when49_returns3AndNegative3(self):
        actual = get_coordinates(49)
        self.assertEquals(actual, (3, -3))

    def test_get_coordinates_when50_returns4AndNegative3(self):
        actual = get_coordinates(50)
        self.assertEquals(actual, (4, -3))

    def test_get_coordinates_when41_returnsNegative3AndNegative1(self):
        actual = get_coordinates(41)
        self.assertEquals(actual, (-3, -1))

    def test_get_coordinates_when16_returnsNegative1And2(self):
        actual = get_coordinates(16)
        self.assertEquals(actual, (-1, 2))


def get_nearest_odd_square_root(value):
    square_root = math.sqrt(value)
    integer_square_root = int(square_root)
    if integer_square_root % 2 == 0:
        integer_square_root -= 1
    return integer_square_root


def get_coordinate_of_square(value):
    # Does not work for even or negative values
    max_coordinate_value = int((value - 1) / 2)
    return max_coordinate_value, -max_coordinate_value


def get_coordinates(value):
    nearest_odd_square_root = get_nearest_odd_square_root(value)
    current_value = nearest_odd_square_root ** 2
    current_coordinates = get_coordinate_of_square(nearest_odd_square_root)
    max_x_coordinate = abs(current_coordinates[0]) + 1
    max_y_coordinate = abs(current_coordinates[1]) + 1
    min_x_coordinate = -max_x_coordinate
    min_y_coordinate = -max_y_coordinate
    x_delta = 1
    y_delta = 0
    while current_value != value:
        current_value += 1
        current_coordinates = (current_coordinates[0] + x_delta, current_coordinates[1] + y_delta)
        if current_coordinates[0] == max_x_coordinate:
            x_delta = 0
            y_delta = 1
        if current_coordinates[1] == max_y_coordinate:
            x_delta = -1
            y_delta = 0
        if current_coordinates[0] == min_x_coordinate:
            x_delta = 0
            y_delta = -1
        if current_coordinates[1] == min_y_coordinate:
            x_delta = 1
            y_delta = 0
    return current_coordinates


input_value = 265149


def main():
    coordinates = get_coordinates(input_value)
    print('coordinates: ', coordinates)
    manhattan_distance = abs(coordinates[0]) + abs(coordinates[1])
    print('manhattan distance: ', manhattan_distance)


if __name__ == '__main__':
    main()

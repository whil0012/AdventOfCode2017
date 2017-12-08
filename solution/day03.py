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

    def test_get_first_value_larger_than_when700_returns747(self):
        actual = get_first_value_larger_than(700)
        self.assertEquals(actual, 747)


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


def get_first_value_larger_than(value_in):
    values = {(0, 0): 1}
    current_coordinates = (0, 0)
    x_delta = 1
    y_delta = 0
    max_x_coordinate = 1
    max_y_coordinate = 1
    min_x_coordinate = -1
    min_y_coordinate = -1
    current_value = 1
    while current_value < value_in:
        current_coordinates = (current_coordinates[0] + x_delta, current_coordinates[1] + y_delta)
        current_value = get_calculated_value(current_coordinates, values)
        values[current_coordinates] = current_value
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
            if current_coordinates[0] == max_x_coordinate:
                max_x_coordinate += 1
                max_y_coordinate += 1
                min_x_coordinate -= 1
                min_y_coordinate -= 1
    return current_value


def get_calculated_value(coordinates, values):
    result = 0
    for x_delta in [-1, 0, 1]:
        for y_delta in [-1, 0, 1]:
            adjacent_coordinates = (coordinates[0] + x_delta, coordinates[1] + y_delta)
            adjacent_value = get_value(adjacent_coordinates, values)
            result += adjacent_value
    return result


def get_value(coordinates, values):
    if coordinates in values.keys():
        return values[coordinates]
    else:
        return 0


input_value = 265149


def main():
    coordinates = get_coordinates(input_value)
    print('coordinates: ', coordinates)
    manhattan_distance = abs(coordinates[0]) + abs(coordinates[1])
    print('manhattan distance: ', manhattan_distance)
    value_larger_than = get_first_value_larger_than(input_value)
    print('first value larger than: ', value_larger_than)


if __name__ == '__main__':
    main()

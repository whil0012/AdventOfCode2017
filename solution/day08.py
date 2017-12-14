import unittest
from input_utilities.inputfilepath import get_input_file_path
import enum

@enum.unique
class Operation(enum.Enum):
    Increment = 1
    Decrement = 2


@enum.unique
class ComparisonOperator(enum.Enum):
    LessThan = 1
    LessThanEqualTo = 2
    GreaterThan = 3
    GreaterThanEqualTo = 4
    EqualTo = 5
    NotEqualTo = 6


class Instruction():
    def __init__(self, register_operand, operation, value_operand, condition_register, condition_operator, condition_value):
        self.register_operand = register_operand
        self.operation = operation
        self.value_operand = value_operand
        self.condition_register = condition_register
        self.condition_operator = condition_operator
        self.condition_value = condition_value


class TestDay08(unittest.TestCase):
    def test_create_instruction_whenInvoked_returnsRegisterOperand(self):
        actual = create_instruction('b inc 5 if a > 1')
        self.assertEquals(actual.register_operand, 'b')

    def test_create_instruction_whenOperationIsInc_returnsIncrementOperation(self):
        actual = create_instruction('b inc 5 if a > 1')
        self.assertEquals(actual.operation, Operation.Increment)

    def test_create_instruction_whenOperationIsDec_returnsDecrementOperation(self):
        actual = create_instruction('b dec 5 if a > 1')
        self.assertEquals(actual.operation, Operation.Decrement)

    def test_create_instruction_whenValueOperandIs5_returnsValueOperand5(self):
        actual = create_instruction('b dec 5 if a > 1')
        self.assertEquals(actual.value_operand, 5)

    def test_create_instruction_whenConditionRegisterIs_a_returnsConditionRegister_a(self):
        actual = create_instruction('b dec 5 if a > 1')
        self.assertEquals(actual.condition_register, 'a')

    def test_create_instruction_whenConditionOperatorIsLessThan_returnsConditionOperatorLessThan(self):
        actual = create_instruction('b dec 5 if a < 1')
        self.assertEquals(actual.condition_operator, ComparisonOperator.LessThan)

    def test_create_instruction_whenConditionOperatorIsLessThanEqualTo_returnsConditionOperatorLessThanEqualTo(self):
        actual = create_instruction('b dec 5 if a <= 1')
        self.assertEquals(actual.condition_operator, ComparisonOperator.LessThanEqualTo)

    def test_create_instruction_whenConditionOperatorIsGreaterThan_returnsConditionOperatorGreaterThan(self):
        actual = create_instruction('b dec 5 if a > 1')
        self.assertEquals(actual.condition_operator, ComparisonOperator.GreaterThan)

    def test_create_instruction_whenConditionOperatorIsGreaterThanEqualTo_returnsConditionOperatorGreaterThanEqualTo(self):
        actual = create_instruction('b dec 5 if a >= 1')
        self.assertEquals(actual.condition_operator, ComparisonOperator.GreaterThanEqualTo)

    def test_create_instruction_whenConditionOperatorIsEqualTo_returnsConditionOperatorEqualTo(self):
        actual = create_instruction('b dec 5 if a == 1')
        self.assertEquals(actual.condition_operator, ComparisonOperator.EqualTo)

    def test_create_instruction_whenConditionOperatorIsNotEqualTo_returnsConditionOperatorNotEqualTo(self):
        actual = create_instruction('b dec 5 if a != 1')
        self.assertEquals(actual.condition_operator, ComparisonOperator.NotEqualTo)

    def test_create_instruction_whenConditionValueIs42_returnsConditionValue42(self):
        actual = create_instruction('b dec 5 if a != 42')
        self.assertEquals(actual.condition_value, 42)

    def test_process_instruction_whenConditionNotMet_doesNothing(self):
        registers = {}
        instruction = Instruction('b', Operation.Increment, 5, 'a', ComparisonOperator.EqualTo, 42)
        process_instruction(instruction, registers)
        expected_registers = {}
        self.assertDictEqual(registers, expected_registers)


def process_instruction(instruction, registers):
    pass


def create_instruction(instruction_description):
    instruction_parts = instruction_description.split()
    register_operand = get_register_operand(instruction_parts)
    operation = get_operation(instruction_parts)
    value_operand = get_value_operand(instruction_parts)
    condition_register = get_condition_register(instruction_parts)
    condition_operator = get_condition_operator(instruction_parts)
    condition_value = get_condition_value(instruction_parts)
    return Instruction(register_operand, operation, value_operand, condition_register, condition_operator, condition_value)


def get_condition_value(instruction_parts):
    return int(instruction_parts[6])


def get_condition_operator(instruction_parts):
    condition_operator_description = instruction_parts[5]
    if condition_operator_description == '<':
        return ComparisonOperator.LessThan
    elif condition_operator_description == '<=':
        return ComparisonOperator.LessThanEqualTo
    elif condition_operator_description == '>':
        return ComparisonOperator.GreaterThan
    elif condition_operator_description == '>=':
        return ComparisonOperator.GreaterThanEqualTo
    elif condition_operator_description == '==':
        return ComparisonOperator.EqualTo
    elif condition_operator_description == '!=':
        return ComparisonOperator.NotEqualTo


def get_condition_register(instruction_parts):
    return instruction_parts[4]


def get_value_operand(instruction_parts):
    return int(instruction_parts[2])


def get_operation(instruction_parts):
    description = instruction_parts[1]
    if description == 'inc':
        return Operation.Increment
    else:
        return Operation.Decrement


def get_register_operand(instruction_parts):
    return instruction_parts[0]

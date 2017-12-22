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

    def test_process_instruction_whenConditionNotMetAndRegisterInRegisters_doesNothing(self):
        registers = {'a': 1, 'b':1}
        instruction = Instruction('b', Operation.Increment, 5, 'a', ComparisonOperator.GreaterThan, 42)
        process_instruction(instruction, registers)
        expected_registers = {'a': 1, 'b':1}
        self.assertDictEqual(registers, expected_registers)

    def test_process_instruction_whenIncrementGTAndRegisterInRegisters_incrementsRegister(self):
        registers = {'a': 1, 'b':1}
        instruction = Instruction('b', Operation.Increment, 5, 'a', ComparisonOperator.GreaterThan, 0)
        process_instruction(instruction, registers)
        actual = registers['b']
        self.assertEquals(actual, 6)

    def test_process_instruction_whenIncrementLTAndRegisterInRegisters_incrementsRegister(self):
        registers = {'a': 1, 'b':1}
        instruction = Instruction('b', Operation.Increment, 5, 'a', ComparisonOperator.LessThan, 2)
        process_instruction(instruction, registers)
        actual = registers['b']
        self.assertEquals(actual, 6)

    def test_process_instruction_whenIncrementETAndRegisterInRegisters_incrementsRegister(self):
        registers = {'a': 1, 'b':1}
        instruction = Instruction('b', Operation.Increment, 5, 'a', ComparisonOperator.EqualTo, 1)
        process_instruction(instruction, registers)
        actual = registers['b']
        self.assertEquals(actual, 6)

    def test_process_instruction_whenIncrementGETAndGreaterThan_incrementsRegister(self):
        registers = {'a': 1, 'b':1}
        instruction = Instruction('b', Operation.Increment, 5, 'a', ComparisonOperator.GreaterThanEqualTo, 0)
        process_instruction(instruction, registers)
        actual = registers['b']
        self.assertEquals(actual, 6)

    def test_process_instruction_whenIncrementGETAndEqualTo_incrementsRegister(self):
        registers = {'a': 1, 'b':1}
        instruction = Instruction('b', Operation.Increment, 5, 'a', ComparisonOperator.GreaterThanEqualTo, 1)
        process_instruction(instruction, registers)
        actual = registers['b']
        self.assertEquals(actual, 6)

    def test_process_instruction_whenIncrementLETAndLessThan_incrementsRegister(self):
        registers = {'a': 1, 'b':1}
        instruction = Instruction('b', Operation.Increment, 5, 'a', ComparisonOperator.LessThanEqualTo, 2)
        process_instruction(instruction, registers)
        actual = registers['b']
        self.assertEquals(actual, 6)

    def test_process_instruction_whenIncrementLETAndEqualTo_incrementsRegister(self):
        registers = {'a': 1, 'b':1}
        instruction = Instruction('b', Operation.Increment, 5, 'a', ComparisonOperator.LessThanEqualTo, 1)
        process_instruction(instruction, registers)
        actual = registers['b']
        self.assertEquals(actual, 6)

    def test_process_instruction_whenIncrementNET_incrementsRegister(self):
        registers = {'a': 1, 'b':1}
        instruction = Instruction('b', Operation.Increment, 5, 'a', ComparisonOperator.NotEqualTo, 2)
        process_instruction(instruction, registers)
        actual = registers['b']
        self.assertEquals(actual, 6)

    def test_process_instruction_whenDecrement_decrementsRegister(self):
        registers = {'a': 1, 'b':1}
        instruction = Instruction('b', Operation.Decrement, 5, 'a', ComparisonOperator.GreaterThan, 0)
        process_instruction(instruction, registers)
        actual = registers['b']
        self.assertEquals(actual, -4)

    def test_process_instruction_whenConditionRegisterNotInRegisters_Uses0ForConditionRegisterValue(self):
        registers = {'b':1}
        instruction = Instruction('b', Operation.Decrement, 5, 'a', ComparisonOperator.LessThan, 1)
        process_instruction(instruction, registers)
        actual = registers['b']
        self.assertEquals(actual, -4)

    def test_process_instruction_whenOperationRegisterNotInRegisters_Uses0ForOperationRegisterValue(self):
        registers = {'a': 1}
        instruction = Instruction('b', Operation.Decrement, 5, 'a', ComparisonOperator.GreaterThan, 0)
        process_instruction(instruction, registers)
        actual = registers['b']
        self.assertEquals(actual, -5)


def instruction_condition_true(condition_register_value, condition_operator, condition_value):
    if condition_operator == ComparisonOperator.GreaterThan:
        return condition_register_value > condition_value
    elif condition_operator == ComparisonOperator.LessThan:
        return condition_register_value < condition_value
    elif condition_operator == ComparisonOperator.EqualTo:
        return condition_register_value == condition_value
    elif condition_operator == ComparisonOperator.GreaterThanEqualTo:
        return condition_register_value >= condition_value
    elif condition_operator == ComparisonOperator.LessThanEqualTo:
        return condition_register_value <= condition_value
    elif condition_operator == ComparisonOperator.NotEqualTo:
        return condition_register_value != condition_value


def process_instruction_operation(register_operand_value, operation, value_operand):
    if operation == Operation.Increment:
        return register_operand_value + value_operand
    else:
        return register_operand_value - value_operand


def get_register_value(registers, condition_register):
    if condition_register in registers.keys():
        return registers[condition_register]
    else:
        return 0


def process_instruction(instruction, registers):
    condition_register_value = get_register_value(registers, instruction.condition_register)
    if instruction_condition_true(condition_register_value, instruction.condition_operator, instruction.condition_value):
        register_operand_value = get_register_value(registers, instruction.register_operand)
        new_value = process_instruction_operation(register_operand_value, instruction.operation, instruction.value_operand)
        registers[instruction.register_operand] = new_value


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


def main():
    registers = {}
    file_path = get_input_file_path('day08.txt')
    with open(file_path, 'r') as input_file:
        for line in input_file:
            instruction = create_instruction(line.strip())
            process_instruction(instruction, registers)
    max_register_value = max(registers.values())
    print("max register value: ", max_register_value)


if __name__ == '__main__':
    main()

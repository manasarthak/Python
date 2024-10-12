"""
Author: Alexander Joslin
GitHub: github.com/echoaj

Explanation:  https://medium.com/@haleesammar/implemented-in-js-dijkstras-2-stack-algorithm-for-evaluating-mathematical-expressions-fc0837dae1ea

We can use Dijkstra's two stack algorithm to solve an equation
such as: (5 + ((4 * 2) * (2 + 3)))

THESE ARE THE ALGORITHM'S RULES:
RULE 1: Scan the expression from left to right. When an operand is encountered,
        push it onto the operand stack.

RULE 2: When an operator is encountered in the expression,
        push it onto the operator stack.

RULE 3: When a left parenthesis is encountered in the expression, ignore it.

RULE 4: When a right parenthesis is encountered in the expression,
        pop an operator off the operator stack. The two operands it must
        operate on must be the last two operands pushed onto the operand stack.
        We therefore pop the operand stack twice, perform the operation,
        and push the result back onto the operand stack so it will be available
        for use as an operand of the next operator popped off the operator stack.

RULE 5: When the entire infix expression has been scanned, the value left on
        the operand stack represents the value of the expression.

NOTE:   It only works with whole numbers.
"""

__author__ = "Alexander Joslin"

import operator as op
from .stack import Stack

def dijkstras_two_stack_algorithm(equation: str) -> int:
    """
    Evaluate a mathematical expression using Dijkstra's two-stack algorithm.

    DocTests:
    >>> dijkstras_two_stack_algorithm("(5 + 3)")
    8
    >>> dijkstras_two_stack_algorithm("((9 - (2 + 9)) + (8 - 1))")
    5
    >>> dijkstras_two_stack_algorithm("((((3 - 2) - (2 + 3)) + (2 - 4)) + 3)")
    -3

    :param equation: A string representing a mathematical equation.
    :return: The result of the evaluated expression as an integer.
    """
    operators = {
        "*": op.mul,
        "/": op.truediv,
        "+": op.add,
        "-": op.sub,
    }

    operand_stack: Stack[int] = Stack()
    operator_stack: Stack[str] = Stack()

    for char in equation:
        if char.isdigit():
            # RULE 1: Push operands onto the operand stack
            operand_stack.push(int(char))
        elif char in operators:
            # RULE 2: Push operators onto the operator stack
            operator_stack.push(char)
        elif char == ")":
            # RULE 4: Evaluate the expression within the parentheses
            if operator_stack.is_empty():
                raise ValueError("Mismatched parentheses: No operator found.")
            operator = operator_stack.pop()
            
            if operand_stack.is_empty():
                raise ValueError("Mismatched parentheses: Not enough operands.")
            num1 = operand_stack.pop()
            
            if operand_stack.is_empty():
                raise ValueError("Mismatched parentheses: Not enough operands.")
            num2 = operand_stack.pop()

            # Perform the operation and push the result back onto the operand stack
            result = operators[operator](num2, num1)
            operand_stack.push(result)

    # RULE 5: The final result should be on the operand stack
    if operand_stack.is_empty():
        raise ValueError("Invalid expression: No result computed.")
        
    return operand_stack.pop()


if __name__ == "__main__":
    equation = "(5 + ((4 * 2) * (2 + 3)))"
    print(f"{equation} = {dijkstras_two_stack_algorithm(equation)}")

from typing import Dict, Optional, Tuple
from .stack import Stack

class BalancedParenthesesChecker:
    def __init__(
        self,
        bracket_pairs: Optional[Dict[str, str]] = None,
        ignore_non_brackets: bool = True,
        debug: bool = False
    ):
        """
        Initializes a BalancedParenthesesChecker object.

        Args:
            bracket_pairs (Dict[str, str], optional): A custom set of bracket pairs. Defaults to None.
            ignore_non_brackets (bool, optional): Whether to ignore non-bracket characters in the input. Defaults to True.
            debug (bool, optional): Enables debug mode for tracing steps. Defaults to False.
        """
        self.bracket_pairs = bracket_pairs or {"(": ")", "[": "]", "{": "}"}
        self.ignore_non_brackets = ignore_non_brackets
        self.debug = debug

    def balanced_parentheses(self, s: str) -> bool:
        """
        Checks if the given string has balanced parentheses/brackets.

        Args:
            s (str): The input string containing brackets or parentheses.

        Returns:
            bool: True if the parentheses are balanced, False otherwise.

        >>> checker = BalancedParenthesesChecker()
        >>> checker.balanced_parentheses("([]{})")
        True
        >>> checker.balanced_parentheses("[()]{}{[()()]()}")
        True
        >>> checker.balanced_parentheses("[(])")
        False
        >>> checker.balanced_parentheses("1+2*3-4")
        True
        >>> checker.balanced_parentheses("")
        True
        """
        stack: Stack[str] = Stack()

        for char in s:
            if char in self.bracket_pairs:
                stack.push(char)
                if self.debug:
                    print(f"Pushed: {char}, Stack: {stack}")
            elif char in self.bracket_pairs.values():
                if stack.is_empty():
                    if self.debug:
                        print(f"Unmatched closing bracket found: {char}")
                    return False
                popped = stack.pop()
                if self.bracket_pairs[popped] != char:
                    if self.debug:
                        print(f"Mismatched brackets: {popped} and {char}")
                    return False
                if self.debug:
                    print(f"Popped: {popped}, Stack: {stack}")
            elif not self.ignore_non_brackets:
                if self.debug:
                    print(f"Non-bracket character found: {char}")
                return False
        
        if self.debug:
            print(f"Final Stack: {stack}")

        return stack.is_empty()

if __name__ == "__main__":
    from doctest import testmod

    testmod()

    examples = ["((()))", "((())", "(()))", "{[()]}", "[1+2]*(3+4)"]
    checker = BalancedParenthesesChecker(debug=True)
    print("Balanced parentheses demonstration:\n")
    for example in examples:
        not_str = "" if checker.balanced_parentheses(example) else "not "
        print(f"{example} is {not_str}balanced")

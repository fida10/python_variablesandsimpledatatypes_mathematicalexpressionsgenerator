import unittest
from src.ans import generate_expressions

class TestExpressionsGenerator(unittest.TestCase):
    def test_expression_generation(self):        
        target = 8
        expressions = generate_expressions(target)
        for expr in expressions: 
            self.assertEqual(eval(expr), target) # eval takes a string and evaluates it as a math expression. If the expression is invalid, an exception is thrown

# Additional tests might include checking for the uniqueness of expressions, handling of zero and negative numbers, etc.


if __name__ == '__main__':
    unittest.main()

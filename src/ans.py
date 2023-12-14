""" 
4. Mathematical Expressions Generator (Builds on 2-9)

Task: Create a Python program that generates and prints 
four unique arithmetic expressions 
(using addition, subtraction, multiplication, division) 
that result in a user-provided number. 
The expressions must use at least two different numbers each (other than the target number) 
and must be generated programmatically (not hard-coded). Display the expressions and their results.

Key Concepts: Arithmetic operations, loops, conditional logic, input handling.
"""
import random
import sys

def generate_expressions(target): 
    ans = []
    addition_rand_int = random.randint(-sys.maxsize - 1, target)
    # subtracting 1 because I am taking the maxsize (maximium number) allowed in python 
    # and then taking its negative. Because 0 is counted, I am subtracting 1 to get 
    # the minimum number allowed in python.
    ans.append(f'{addition_rand_int} + {target - addition_rand_int}')
    
    subtraction_rand_int = random.randint(target, sys.maxsize)
    ans.append(f'{subtraction_rand_int} - {subtraction_rand_int - target}')
    
    all_factors_of_target = [target]
    for i in range(2, (target // 2) + 1):
        if target % i == 0:
            all_factors_of_target.append(i)
    
    multiplication_rand_int = random.choice(all_factors_of_target)
    ans.append(f'{multiplication_rand_int} * {target / multiplication_rand_int}')
    
    
    all_multiples_of_target = [target]
    #for i in range(2, sys.maxsize): #this is too much
    for i in range(2, 1000): # putting hard limit to stop this from running forever
        try:
            print(i)
            all_multiples_of_target.append(target * i)
        except OverflowError:
            break
    
    division_rand_int = random.choice(all_multiples_of_target)
    ans.append(f'{division_rand_int} / {division_rand_int / target}')
    
    return ans


print(generate_expressions(8))

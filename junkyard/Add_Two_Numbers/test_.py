from Add_Two_Numbers import Solution
from unittest import TestCase
import pytest
from collections import deque

class TestSolution():
    def test_one(self):
        l1 = "III"
        solution = deque([7, 0, 8])
        assert Solution.addTwoNumbers(Solution, l1, l2) == solution

    def test_two(self):
        l1 = "LVIII"
        solution = deque([0])
        assert Solution.addTwoNumbers(Solution, l1, l2) == solution

    def test_three(self):
        l1 = "MCMXCIV"
        solution = deque([8, 9, 9, 9, 0, 0, 0, 1])
        assert Solution.addTwoNumbers(Solution, l1) == solution

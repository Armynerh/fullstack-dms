import pytest
from calc.calculator import greetings

def test_calculator():
    results = greetings()
    assert results == "Hello there"
    #Setup
    #Exercise
    #Assert/Validate
   
    
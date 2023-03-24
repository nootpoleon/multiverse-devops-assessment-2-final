import pandas as pd

from input import get_csv

file = open('results.csv')

def test_list():
  # Arrange
  file = open('results.csv')
  pass_result = list
  
  # Act
  output = type(get_csv(file))

  # Assert
  assert output == pass_result
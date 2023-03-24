import pandas as pd

from input import get_csv
from input import drop_duplicate

file = open('results.csv')

def test_list():
  # Arrange
  file = open('results.csv')
  pass_result = list
  
  # Act
  output = type(get_csv(file))

  # Assert
  assert output == pass_result

def test_duplicatesremoved():

  # Arrange
  df = pd.read_csv('results.csv')  # read CSV
  df = df.drop_duplicates() # drop duplicate values
  passresult = len(df)

  # Act
  file = open('results.csv')
  nodupldf = drop_duplicate(file)
  output = len(nodupldf) - 1

  # Assert
  assert output == passresult
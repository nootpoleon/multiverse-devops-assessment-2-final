import pandas as pd

from input import get_csv
from input import drop_duplicate
from input import drop_null

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


def test_nadropped():

  # Arrange
  df = pd.read_csv('results.csv')  # read CSV
  nodupldf = df.drop_duplicates() # drop duplicate values
  nonan = nodupldf.dropna(how='all') # drop rows with full na values
  passresult = len(nonan) # length of array
  
  # Act
  file = open('results.csv') # open file
  noduplarr = drop_duplicate(file) # run drop duplicates
  nonanarr = drop_null(noduplarr) # run drop NA
  output = len(nonanarr) - 1 # return length without column headers

  # Assert
  assert output == passresult

datanonull = drop_null(file)


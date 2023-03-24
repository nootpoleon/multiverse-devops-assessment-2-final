import pandas as pd
import numpy as np

from input import get_csv
from input import drop_duplicate
from input import drop_null
from input import capitalise_username

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

def column(matrix, i):
    return [row[i] for row in matrix]

def test_capitalisedcolumns():
  
  # Arrange
  capitalise = np.rec.fromrecords(datanonull, names = 'user_id, first_name, last_name, answer_1, answer_2, answer_3')
  capitalise['first_name'] = np.char.title(capitalise['first_name'])
  capitalise['last_name'] = np.char.title(capitalise['last_name'])
  capitalise[0] = 'user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3'
  passresult1 = capitalise['first_name']
  passresult2 = capitalise['last_name']
  
  # Act
  file = open('results.csv') # open file
  noduplarr = drop_duplicate(file) # run drop duplicates
  nonanarr = drop_null(noduplarr) # run drop NA
  capitalisearr = capitalise_username(nonanarr) 
  output1 = column(capitalisearr, 1)
  output2 = column(capitalisearr, 2)

  # Assert
  np.testing.assert_array_equal(passresult1, output1)
  np.testing.assert_array_equal(passresult2, output2)

capitaliseddata = np.array(capitalise_username(file))
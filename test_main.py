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

def test_validans3():

  #Arrange
  passresult = len(ans3valid(capitaliseddata)) -1 #bring in the code, with the length

  #Act
  df = capitaliseddata #take the file
  noblankentries = []
  for row in capitaliseddata:
        if all(cell != '' for cell in row): # append rows with no blanks at all
            noblankentries.append(row)
  
  noblankentries = pd.DataFrame(noblankentries) #dataframe declare
  noblankentries.columns=noblankentries.iloc[0] #column name find
  column_headers = list(noblankentries.columns.values) #column name declare
  noblankentries = noblankentries.tail(-1) #remove first row (old headers)
  noblankentries = np.array(noblankentries) #cast as array
  isvalid_ans3 = [x for x in noblankentries[0:] if int(x[5]) == 1 or int(x[5]) == 2 or int(x[5]) == 3 or int(x[5]) == 4 or int(x[5]) == 5 or int(x[5]) == 6 or int(x[5]) == 7 or int(x[5]) == 8 or int(x[5]) == 9 or int(x[5]) == 10] #check answers
  output = len(isvalid_ans3) #check the length of the dataframe
  
  #Assert
  assert passresult == output

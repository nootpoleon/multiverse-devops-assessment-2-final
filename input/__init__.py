import csv
import numpy as np
import pandas as pd

file = open('results.csv')

def get_csv(file):
  file = open('results.csv')
  type(file)
  csvreader = csv.reader(file)
  data = list(csvreader)
  return data

data = get_csv('results.csv')

def drop_duplicate(file):
  no_duplicates = []
  for x in data:
    if x not in no_duplicates:
      no_duplicates.append(x)
  return no_duplicates

datanodupl = drop_duplicate(file)

def drop_null(file):
  remove_na = []
  for x in datanodupl:
    if x != ['','','','','','']:
      remove_na.append(x)
  return remove_na

datanonull = drop_null(file)

def capitalise_username(file):
  capitalise = np.rec.fromrecords(datanonull, names = 'user_id, first_name, last_name, answer_1, answer_2, answer_3')
  capitalise['first_name'] = np.char.title(capitalise['first_name'])
  capitalise['last_name'] = np.char.title(capitalise['last_name'])
  capitalise[0] = 'user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3'
  capitalise = capitalise.tolist()
  return capitalise

capitaliseddata = capitalise_username(file)

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
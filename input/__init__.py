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

def ans3valid(file):
  noblanks =[]
  for i in capitaliseddata:
      if len([x for x in i if x != '']) == 6: #removes any line nan entries
          noblanks.append(i)
  
  noblanks = np.array(noblanks)
  
  valid_ans3 = [x for x in noblanks[1:] if int(x[5]) > 0 and int(x[5])<11]
  valid_ans3.insert(0, noblanks[0])
  valid_ans3 = np.array(valid_ans3)
  return valid_ans3

def exportcsv(file):
  with open('cleansedresults.csv','w', newline='')as f:
    writer =csv.writer(f)
    writer.writerows(ans3valid(file))

def finalresult(file):
  cleansedfile = open('cleansedresults.csv')
  readcleansedfile = pd.read_csv(cleansedfile)
  print(readcleansedfile)
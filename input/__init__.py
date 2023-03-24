import csv

file = open('results.csv')

def get_csv(file):
  file = open('results.csv')
  type(file)
  csvreader = csv.reader(file)
  data = list(csvreader)
  return data

data = get_csv('results.csv')
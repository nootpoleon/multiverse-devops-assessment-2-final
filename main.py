import pytest
import pandas as pd
from input import get_csv
from input import drop_duplicate
from input import drop_null
from input import capitalise_username
from input import ans3valid
from input import exportcsv
from input import finalresult

file = open('results.csv')
data = get_csv(file)
data = drop_duplicate(data)
data = drop_null(data)
data = capitalise_username(data)
data = ans3valid(data)
data = exportcsv(data)
data = finalresult(data)
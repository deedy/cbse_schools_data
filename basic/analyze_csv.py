import csv
import time

RES_FILE_CSV = 'schools.csv'
print('Reading {0}...'.format(RES_FILE_CSV))
start = time.time()
with open(RES_FILE_CSV, 'r') as f:
  r = csv.reader(f)
  data = list(r)
header = data[0]
data = data[1:]
print('Loaded {0} rows in {1:0.2f} seconds.'.format(len(data), time.time() - start))
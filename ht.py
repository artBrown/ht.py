import os
import re
import glob
import subprocess

from os.path import exists
from sys import exit
cwd = os.getcwd()
IN_FOLDER = cwd + '/py/input/'
OT_FOLDER = cwd + '/py/output/'
RS_FOLDER = cwd + '/py/result/'
SOLUTION = cwd + '/solution.py'
WRONG_PLACE_TO_RUN = 'You have to run this program under, downloaded inputs and outputs.'
FOLDERS = [IN_FOLDER, OT_FOLDER, RS_FOLDER]
RE_NUM = re.compile(r'\d+.txt$')
def of_(in_file):
  return OT_FOLDER + 'output%s' % RE_NUM.findall(in_file)[0]
def rf_(in_file):
  return RS_FOLDER + 'output%s' % RE_NUM.findall(in_file)[0]
wrong_place_to_run = False
for folder in FOLDERS:
  if not exists(folder):
    print('Folder \'%s\' does not exists. ' % folder)
    wrong_place_to_run = True

if wrong_place_to_run:
  print(WRONG_PLACE_TO_RUN)
  exit(1)

passed, failed = 0, 0
if not exists(SOLUTION):
  print('Solution must be inside solution.py, put your solution to there and run this command again.')
  exit(1)

in_files = sorted(glob.glob(IN_FOLDER + '*.txt'))

print('')
for in_file in in_files:
  ot_file = of_(in_file)
  rs_file = rf_(in_file)
  cmd = 'python3 solution.py ' + str(os.getpid())
  
  process = subprocess.Popen(
    cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,
    text=True,
    shell=True)
  
  with open(in_file) as f:
    in_data = f.read()
  with open(ot_file) as f:
    ot_data = f.read()
  _ot, err = process.communicate(input=in_data)
  if err:
    print(err)
    exit(1)
  ot = ''
  for ot_ in _ot:
    ot += ot_
  res = open(rs_file, 'w+')
  res.write(ot)
  res.close()
  if ot and ot.strip() == ot_data.strip():
    passed += 1
  else:
    print(os.path.basename(ot_file) + ':\n' + ot_data.strip() + '\n' + ot)
    failed += 1
print('total: {} passed: {} failed: {}'.format(passed + failed, passed, failed))

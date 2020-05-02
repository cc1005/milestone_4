import os
from os import path
if path.exists("env.py"):
  import env 

print(os.getenv("TESTVAR"))
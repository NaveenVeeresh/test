from  bankAccount import *

naveen =bankAccount(2300,'naveen')
suresh =bankAccount(3500,'suresh')

# naveen.deposit(2300)
# naveen.getbalance()
# naveen.viabletransaction(23000)
# naveen.withdraw(1000)
naveen.transfer(1000,suresh)
# suresh.getbalance()
import glob
from pathlib import Path

# Define the target directory
target_dir = "dir1/dir2/dir3"

print("=== Using glob module ===")
# Using glob
txt_files_glob = glob.glob(f"{target_dir}/*.txt")

for file_path in txt_files_glob:
    with open(file_path, 'r') as f:
        line_count = sum(1 for _ in f)
    print(f"{file_path}: {line_count} lines")

print("\n=== Using pathlib module ===")
# Using pathlib
p = Path(target_dir)
txt_files_pathlib = p.glob("*.txt")

for file in txt_files_pathlib:
    with file.open('r') as f:
        line_count = sum(1 for _ in f)
    print(f"{file}: {line_count} lines")


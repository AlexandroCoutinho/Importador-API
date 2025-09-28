import os
import re

pattern = re.compile(r"^(\d{2})-(\d{2})-(.*)")

for filename in os.listdir("."):
    match = pattern.match(filename)
    if match:
        first, second, rest = match.groups()
        new_name = f"S{first}L{second}_{rest}"
        print(f"renaming: {filename} to {new_name}")
        os.rename(filename, new_name)
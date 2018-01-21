#reclass.py

import re

print("******RE******")

text = "aAsmr3idd4bgs7Dlsf9eAF"

print("".join(re.findall('[\d|.]+',text)))

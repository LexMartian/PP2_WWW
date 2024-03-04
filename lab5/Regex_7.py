import re

text = "snake_case_del cdef_adwwa _xacsc_csaas"
pattern = r'_(\w)'  

print(re.sub(pattern, lambda x: x.group(1).upper(), text))  

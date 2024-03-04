import os

print('Exist:', os.access('C:\\Users\\User\\Desktop\\PP2_WWW\\test.txt', os.F_OK))
print('Readable:', os.access('C:\\Users\\User\\Desktop\\PP2_WWW\\test.txt', os.R_OK))
print('Writable:', os.access('C:\\Users\\User\\Desktop\\PP2_WWW\\test.txt', os.W_OK))
print('Executable:', os.access('C:\\Users\\User\\Desktop\\PP2_WWW\\test.txt', os.X_OK))

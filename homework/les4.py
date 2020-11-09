from time import sleep, time
import random
import datetime as dt
import sys
import os

_, strdate = sys.argv
b_date = dt.datetime.strptime(str_date, '%d.%m.%Y')
age = dt.datetime.now().year - b_date.year
print(b_date)
print(sys.argv)

# def sleep(a):
#     print(f'IM SLEEP {a} sec')
#
# for itm in range(random.randint(10, 25)):
#     print(itm)
#     # sl(0.5)
# sleep(1.5)
# print('END')
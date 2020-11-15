# lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
# Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
# Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
# Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""


# file = open('lorem.txt', 'r', encoding='UTF-8')
# file.write(lorem)
# file.close()

# file = open('lorem.txt', 'r', encoding='UTF-8')
# for line in file:
#     print(line, end='')
# file.close()


# file = open('lorem.txt', 'r', encoding='UTF-8')
# lines = file.readlines()
# print(lines)
# file.close()

# file = open('lorem.txt', 'r', encoding='UTF-8')
# lines = file.read(8)
# print(lines)
# file.close()
#
# file.seek(0)
# file.tell()
# file.read(8)

# file = open('lorem.txt', 'r', encoding='UTF-8')
# try:
#     lines = file.read(16)
#     print(lines)
# except IOError:
#     pass
# finally:
#     file.close()

# def file_content(file_name):
#     file = open(file_name, 'r')
#     try:
#         return file.read(16)
#     except IOError:
#         pass
#     finally:
#         print('FINALLY')
#         file.close()
# result = file_content('lorem.txt')
#
# with open('lorem.txt', 'r', encoding='UTF-8') as file:
#     print(file.read())

# def log(func):
#     def wrapper(*args, **kwargs):
#         with open('some.log', 'a', encoding='UTF-8') as log_file:
#             log_file.write(f'{func.__name__} start with args: {args}, kwargs: {kwargs}')
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
#
# @log
# def some_one(a, b):
#     return a + b
# some_one(2, 7)

import os
import sys

print(os.path.dirname(__file__))

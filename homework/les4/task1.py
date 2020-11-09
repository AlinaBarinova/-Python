from sys import argv

_, hours, rate, bonus = argv

salary = (int(hours) * int(rate)) + int(bonus)

print(salary)

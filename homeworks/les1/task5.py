sales = input('Объем выручки от продаж\n>>>')
costs = input('Объем издержек\n>>>')
if int(sales) > int(costs):
    print('Результат: Прибыль')
    profit = int(sales) - int(costs)
    rent_sales = round(profit / int(sales), 2)
    print(f"Рентабельность выручки составила = {rent_sales}")
    empoyees = input('Количество сотрудников\n>>>')
    profit_per_employee = round(profit / int(empoyees), 2)
    print(f"Прибыль на одного сотрудника = {profit_per_employee}")
elif int(sales) == int(costs):
    print('Результат: 0')
else: print('Результат: Убыток')
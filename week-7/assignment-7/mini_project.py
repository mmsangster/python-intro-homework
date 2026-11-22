
import os
import csv
import datetime

path = os.path.join('..', 'data', 'expenses.csv')

if os.path.exists('c:/users/user/desktop/code the dream/python-intro-homework/week-7/data'):
    print('The file was found.')
else:
    print('Error: The file was not found.')
    

with open('c:/users/user/desktop/code the dream/python-intro-homework/week-7/data/expenses.csv', 'r') as file:
    records = list(csv.DictReader(file))
    for item in records:
        item['amount'] = float(item['amount'])
        food = [item for item in records if item['category'] == 'Food']
        
total_food_spending = sum(item['amount'] for item in food)

from datetime import datetime
now = datetime.now()

with open('food_report.txt', 'w') as file:
  file.write(f"Food Expense Report - generated: {now.strftime('%B %d, %Y')}")

with open('c:/users/user/desktop/code the dream/python-intro-homework/week-7/data/expenses.csv') as csv_file, \
    open('food_report.txt', 'a', encoding='utf-8') as txt_file:

    reader = csv.DictReader(csv_file)
    for row in food:
        line = f'\n{row['date']}: ${row['amount']}'
        txt_file.write(line)

with open('food_report.txt', 'a', encoding='utf-8') as file:
  file.write(f'\nTotal: ${total_food_spending:.2f}')


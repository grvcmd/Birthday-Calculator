
print('\n')
print('Birthday Calculator')
print('-')
# Ask for current month, day, year
current_month = str(input('What month is it: '))
current_day = int(input('What day is it: '))
current_year = int(input('What year is it: '))
print('\n')
print('CURRENT DAY')
print('Month:', current_month)
print('Day:', current_day)
print('Year:', current_year)

print('\n')

# Ask for birthday
birthday_month = str(input('Birthday month: '))
birthday_day = int(input('Birthday day: '))
birthday_year = int(input('Birthday year: '))
print('\n')
print('BIRTHDAY')
print('Month:', birthday_month)
print('Day:', birthday_day)
print('Year:', birthday_year)

# print how old user is
age = (current_year - birthday_year)
print('-')
print('You are', age, 'years old!')

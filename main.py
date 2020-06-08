print('\n')
print('Birthday Calculator')
print('-')
# Ask for current month, day, year
current_month = str(input('What month is it: '))
current_day = int(input('What day is it: '))
current_year = int(input('What year is it: '))
print('Today is:', current_month, current_day, current_year, '\n')

# Ask for birthday
birthday_month = str(input('Birthday month: '))
birthday_day = int(input('Birthday day: '))
birthday_year = int(input('Birthday year: '))
print('Your birthday is on:', birthday_month, birthday_day, birthday_year)

# print how old user is
age = (current_year - birthday_year)
print('-')
print('You are', age, 'years old!')

if (current_month == birthday_month) and (current_day == birthday_day):
    print('ITS YOUR BIRTHDAY TODAY!')
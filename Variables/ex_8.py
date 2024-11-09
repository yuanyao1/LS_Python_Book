# Assume you have $1,000.00 in the bank, and you've somehow managed to find a bank that pays you 5% (this is a wish-fulfillment fantasy) compounded interest every year. After one year, you will have $1,050 ($1,000 times 1.05). After two years, you will have $1,050 times 1.05, or $1102.50. Create a variable named balance that contains the amount of money you will have after 5 years, then print the result. Use a single expression if you can to set balance to the correct value.

balance = 1000.00
balance = balance * ((1 + 0.05)**5)
print(f'The total balance after 5 years is: {balance:.2f}')

# balance = 1000.00
# balance *= 1.05
# balance *= 1.05
# balance *= 1.05
# balance *= 1.05
# balance *= 1.05
# print(f'The total balance after 5 years is: {balance}')

# balance = 1000
# for years in range(5):
#     balance = balance * (1 + 0.05)
# print(f'The total balance after 1 years is: {balance}')

# balance = 1000
# years = 5
# interest_rate = 0.05

# if years > 0:
#     new_balance = balance
#     for _ in range(years):
#         new_balance *= (1 + interest_rate)
#     print(f'The total balance after {years} years is: {new_balance}')
# elif years == 0:
#     print(f'The total balance after {years} years is: {balance}')
# else:
#     print(f'You gave {years} which is not a positive time period. Positive '
#           'time periods are needed to perform compound interest calculations.')


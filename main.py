print('Welcome to the tip calculator')

total_bill = float(input('What was the total bill? $'))

tip = float(input('What percentage tip would you like to give? 10, 12 or 15? '))

split = int(input('How many people to split the bill? '))

result = (total_bill * (1 + tip / 100)) / split
final_result = "{:.2f}".format(result)
print(f'Each person should pay: ${final_result}')

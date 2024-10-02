# 1. bug collector
total_bugs = 0 #make a variable for total bugs 

# Loop through each of the 5 days
for day in range(1, 6):
    # Ask for the number of bugs collected on the current day
    bugs_collected = int(input(f"Enter the number of bugs collected on day {day}: "))

    # Add the number of bugs collected to the total
    total_bugs += bugs_collected

# After the loop ends, display the results
print(f"Total number of bugs collected over 5 days: {total_bugs}")
print('-----------------------------------------------------------------------------------------------')
#----------------------------------------------------------------------------------------

# 2. Calories burned per minute
calories_per_minute = 4.2

# List of minutes to track calories burned
minutes_list = [10, 15, 20, 25, 30]

# Loop through each minute in the list
for minutes in minutes_list:
    # Calculate calories burned
    calories_burned = calories_per_minute * minutes
    # Display the result
    print(f"\nCalories burned after {minutes} minutes: {calories_burned:.1f}")
print('-----------------------------------------------------------------------------------------------')
#----------------------------------------------------------------------------------------

# 3. write a rpogram for monthly budget/expenses
#maka a variable for monthly budget
Budget = float(input("\nEnter the amount you have budgeted for the month: $ "))

total_expenses = 0.0

num_expenses = int(input("enter the number of expenses for the month: "))

for i in range(1, num_expenses + 1):
    expense = float(input(f"enter your expense amount for expense {i}: $"))

    total_expenses += expense #calculate the total expense
    
    difference = Budget - total_expenses #calculate the difference (if any)

# Determine if over or under budget
if difference > 0:
    print(f"You are under budget by: ${difference:,.2f}")
elif difference < 0:
    print(f"You are over budget by: ${abs(difference):,.2f}")
else:
    print("You are exactly on budget!")
print('-----------------------------------------------------------------------------------------------')
#------------------------------------------------------------------------------------------------

# 4. distance traveled program
# Ask for the speed of the vehicle in mph
speed = int(input("\nWhat is the speed of the vehicle in mph? "))

# Ask for the number of hours the vehicle has traveled
hours = int(input("How many hours has it traveled? "))

# Display the header for the output
print("\nHour\t\tDistance Traveled")

# Loop through each hour and calculate the distance traveled
for hour in range(1, hours + 1):
    distance_traveled = speed * hour
    print(f"{hour}\t\t\t{distance_traveled}")
print('-----------------------------------------------------------------------------------------------')
#---------------------------------------------------------------------------------------------

# 5. average rainfall program
# Ask for the number of years
years = int(input("\nEnter the number of years of rainfall: "))

# Initialize total rainfall and total months to 0
total_rainfall = 0
total_months = 0

# Outer loop to iterate over each year
for year in range(1, years + 1):
    print(f"\nYear {year}:")
    
    # Inner loop to iterate over each of the 12 months
    for month in range(1, 13):
        # Ask for the inches of rainfall for the current month
        rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
        
        # Add the monthly rainfall to the total rainfall
        total_rainfall += rainfall
    
    # Add 12 months for each year to the total months
    total_months += 12

# Calculate the average rainfall per month
average_rainfall = total_rainfall / total_months

# Display the total months, total rainfall, and average rainfall per month
print(f"\nTotal number of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")
print('-----------------------------------------------------------------------------------------------')
#-------------------------------------------------------------------------------------------------

# 6. celcius to farenheit table 
# Display the header for the table
print("\nCelsius\tFahrenheit")

# Loop through Celsius values from 0 to 20
for celsius in range(0, 21):
    # Convert Celsius to Fahrenheit using the formula
    fahrenheit = (9/5) * celsius + 32
    # Display the Celsius and Fahrenheit values in a formatted table
    print(f"{celsius}\t{fahrenheit:.2f}")
print('-----------------------------------------------------------------------------------------------')
#-----------------------------------------------------------------------------------------------

# 7. pennies pay
# Ask for the number of days
days = int(input("\nEnter the number of days worked: "))

# Initialize variables for the salary and total pay (both in pennies)
salary = 1  # starting with 1 penny on the first day
total_pay = 0

# Display the header for the table
print("\nDay\tSalary (in dollars)")

# Loop through each day to calculate the salary and total pay
for day in range(1, days + 1):
    # Convert the salary to dollars and display it
    salary_in_dollars = salary / 100  # converting pennies to dollars
    print(f"{day}\t${salary_in_dollars:,.2f}")
    
    # Add the salary of the current day to the total pay
    total_pay += salary
    
    # Double the salary for the next day
    salary *= 2

# Convert total pay to dollars
total_pay_in_dollars = total_pay / 100

# Display the total pay at the end of the period
print(f"\nTotal pay after {days} days: ${total_pay_in_dollars:,.2f}")
print('-----------------------------------------------------------------------------------------------')
#---------------------------------------------------------------------------------------------------

# 8. Sum of numbers
# Initialize the sum of numbers to 0
total_sum = 0

# Initialize the variable to store user input
number = 0

# Start a loop to get numbers from the user
while number >= 0:
    # Ask the user for a number
    number = float(input("\nEnter positive numbers to add (or a negative number to stop): "))
    
    # Check if the number is positive, and if so, add it to the total sum
    if number >= 0:
        total_sum += number

# Display the total sum of the positive numbers entered
print(f"\nThe sum of the positive numbers entered is: {total_sum}")
print('-----------------------------------------------------------------------------------------------')
#-----------------------------------------------------------------------------------------------------

# 9. ocean levels
# Define the rate of ocean level rise per year 
rise_per_year = 1.6

# Display the header
print("\nYear\tOcean Level Rise (in mm)")

# Loop through the next 25 years
for Year in range(1, 26):
    # Calculate the ocean level rise for the current year
    ocean_rise = rise_per_year * Year
    # Display the year and corresponding ocean level rise
    print(f"{Year}\t{ocean_rise:.2f}")
print('-----------------------------------------------------------------------------------------------')
#---------------------------------------------------------------------------------------------------------

# 10. tuition increas
# Define the initial tuition amount
initial_tuition = 8000
# Define the annual increase rate
increase_rate = 0.03

# Display the header
print("\nYear\tProjected Tuition")

# Loop through the next 5 years
for year in range(1, 6):
    # Calculate the projected tuition for the current year
    projected_tuition = initial_tuition * (1 + increase_rate) ** year
    # Display the year and the corresponding projected tuition
    print(f"{year}\t${projected_tuition:.2f}")
#-------------------------------------------------------------------------------------------------------------------

# I could not figure question 11, 12, 13, and 14 out 











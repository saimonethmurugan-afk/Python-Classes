#My Weather App

#Part 1: Accepting input 

city = input("Please enter your city name: ")
temperature = float(input("What is the current temperature in degrees Celsius?: "))

#Part 2:If statement

if temperature > 35:
    print("It is very hot! Make sure to wear sun cream!")

#Part 3 :If else
if temperature >= 15:
    print("Warm and sunny! Try to go outside and enjoy the sunshine!")
else:
    print("May be a bit cold outside. Maybe use a jacket if you want.")

#Part 4:Elif else
if temperature >= 35:
    print("It is very hot! Make sure to wear sun cream!")
elif temperature >= 20:
    print("Warm and sunny! Try to go outside and enjoy the sunshine!")
elif temperature >= 15:
    print("May be a bit cold outside. Maybe use a jacket if you want.")
else:
    print("It is going to be cold outside. Take a jacket and stay warm.")


#Part 5: Modules in Python
 
import datetime
import calendar

#now = datetime.datetime.now.strftime("%H:%m")
now = datetime.datetime.now()
print("City Name: ",city)
print("Current Time: ",now)

#This is used to display the calendar
print(calendar.calendar(now.year))
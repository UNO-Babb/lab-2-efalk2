#FutureTime.py
#Name: Ella Falk
#Date: 1/29/25
#Assignment: Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  hours = input("Provide a number of hours: ")
  #Ask user for minutes
  minutes = input("Provide a number of minutes: ")
  #Calculate the time after the user-supplied time has passed.
  
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()

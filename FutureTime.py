#FutureTime.py
#Name: Ella Falk
#Date: 1/29/25
#Assignment: Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24
  currentMinute = now.minute

  

  #TODO:
  #Ask user for hours
  hours = input("Provide a number of hours: ")
  hours = int(hours) # change from text to number
  #Ask user for minutes
  minutes = input("Provide a number of minutes: ")
  minutes = int(minutes)
  #Calculate the time after the user-supplied time has passed.
  futureMinutes = currentMinute + minutes
  extraHours = futureMinutes // 60
  futureMinutes = futureMinutes % 60
  
  futureHour = (extraHours + currentHour + hours - 12) 
  futureHour = futureHour % 24

  #Do not use any if statements in calculating the time.
  print("This will be the future time.")
  strHour = str(futureHour)
  strMinutes = str(futureMinutes)
  if futureMinutes < 10:
    strMinutes = "0" + strMinutes
  print(strHour + ":" + strMinutes)
  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()

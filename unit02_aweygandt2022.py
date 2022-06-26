############################################################################
#     Aidan Weygandt                        2.11.2021                      #
#     Unit 2 Problems                                                      #
#.    Age calculator, sum of digits, initial deposit, current time.        #
############################################################################
import datetime
x = datetime.datetime.now()
print ("Problem #1 Age Calculator")
print ("What will be your age on your next birthday?")
age = int(input("Age:"))
print ("You were born in",x.year - age)
print ("You will have lived on your next birthday:")
print ((age*365),"days or")
print ((age*365*24),"hours or")
print ((age*365*24*60), "minutes")
print ("You have about", int(100-(age/80*100)), end="% of your lifespan left\n\n")
print ("Problem #2 Sum of digits")
digit = int(input("Enter a digit between 0 and 999:"))
num1 = digit%10 #gets last digit in number
num2 = (digit//10)%10
num3 = (digit//100)%10 #incase theres more than 3 numbers
print ("The sum of these digits is", num1+num2+num3,"\n")
print ("Problem #3 Initial Deposit")
money = int(input("Enter current account balance(whole #):"))
interest = float(input("Enter annual interest rate(e.g. 4.5):")) #uses float instead becuse it needs decimals
time = int(input("Enter number of years(whole #):"))
print ("Your initial deposit was: $", end=str(round(money/((1+(interest/100))**time), 2))) #finds initial deposit with compounding interest and rounds to the nearest hundredth
x = datetime.datetime.now() #updates time again                                            #^also had to convert to string for it to put money sign without space inbetween
current_time = x.strftime("%H:%M:%S") #formats the hours minutes and seconds
print ("\n\nProblem #4 Current Time", "\nThe current time is", current_time)
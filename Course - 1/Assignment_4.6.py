# Assignment 4.6 - Statement
"""Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours
worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and u
se the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour
to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the
string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types
numbers properly. Do not name your variable sum or use the sum() function."""


def computepay(h, r): # Creating a function to compute the pay
    if h <= 40:  # calculation of gross pay if work is less than 40 hours
        gross_pay = h * r;
        return gross_pay
    else:  # calculation of gross pay if work is more than 40 hours at
        forty_hrs_pay = 40 * r;  # calculated the pay for 40 hours at same rate
        extra_hrs = h - 40  # calculated the extra hours which are above 40
        extra_hrs_pay = extra_hrs * r * 1.5  # calculated the extra amount at 1.5 times for extra hours
        gross_pay = forty_hrs_pay + extra_hrs_pay  # calculation of gross pay by adding amount of first 40 hours and extra hours
        return gross_pay

hrs = input("Enter Hours:")
rate_per_hr = input("Enter Rate:")

hours = float(hrs)
rates = float(rate_per_hr)

p = computepay(hours, rates) # Calling the function
print("Pay", p)
hrs = input("Enter Hours:")
rate_per_hr = input("Enter Rate:")
h = float(hrs)
r = float(rate_per_hr)

if h <= 40:  # calculation of gross pay if work is less than 40 hours
    gross_pay = h * r;
    print(gross_pay)
else:  # calculation of gross pay if work is more than 40 hours at
    forty_hrs_pay = 40 * r;  # calculated the pay for 40 hours at same rate
    extra_hrs = h - 40  # calculated the extra hours which are above 40
    extra_hrs_pay = extra_hrs * r * 1.5  # calculated the extra amount at 1.5 times for extra hours
    gross_pay = forty_hrs_pay + extra_hrs_pay  # calculation of gross pay by adding amount of first 40 hours and extra hours
    print(gross_pay)

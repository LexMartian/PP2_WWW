from datetime import datetime

def date_diff_in_seconds(dt2, dt1):
    timedelta = dt2 - dt1
    return timedelta.days * 24 * 3600 + timedelta.seconds

date_input1 = input("Enter the first date and time (YYYY-MM-DD HH:MM:SS): ")
date1 = datetime.strptime(date_input1, '%Y-%m-%d %H:%M:%S')

date_input2 = input("Enter the second date and time (YYYY-MM-DD HH:MM:SS): ")
date2 = datetime.strptime(date_input2, '%Y-%m-%d %H:%M:%S')

difference_seconds = date_diff_in_seconds(date2, date1)

print("\nThe difference between the two dates is: {} seconds".format(difference_seconds))
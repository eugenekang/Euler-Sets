"""
How many Sundays fell on the first of the month during the twentieh century (1 Jan 1901 to 31 Dec 2000)?
"""
import calendar, datetime

# Function to produce the number of Sundays falling on the first of the month between Jan 1 and Dec 31 of a range of years, specified by start and end.
def get_first_sundays(start, end):
    ctr = 0

    # For each month from Jan 1901 - Dec 2000
    for x in range (start, end + 1):
        for y in range(1, 13):
            # Check first of the month if Sunday
            if calendar.day_name[datetime.datetime(x,y,1).weekday()] == "Sunday":
                ctr += 1
    return ctr

if __name__ == "__main__":
      print("The number of Sundays falling on the first of the month between 1 Jan 1901 and 31 Dec 2000 are: " + str(get_first_sundays(1901, 2000)))
#Joshua Perez
#PSID: 1837170

# using the datetime import to check current year and converting it to an integer
from datetime import date
today = date.today()
yr = int(today.year)
# Dictionary to set up month values
months= {"January": 1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}
# asking for dates inside file 
a = open("inputDates","r")

# first condition is to keep going until -1 is put
for i in a:
    if i == "-1":
        break
    else:
# second condition is to have correct space between month and day 
        space_search = i.find(" ")
# third condition is to have the comma and space between day and year
        comma_search = i[space_search+1:].find(", ")
# Second and third condition have passed so they move on
        if space_search != -1 and comma_search != -1:
            month = i[:space_search] 
            day = i [space_search+1:][:comma_search]
# Converting the year space to integer and compare to current year
            year = int(i[space_search+1:][comma_search+2:])
            exact_month = months[month]
# comparing years
            if year > yr:
                print()
            else:
                print(f"{exact_month}/{day}/{year}\n")
# program repeats until stopped.
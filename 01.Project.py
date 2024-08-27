length = int (input ("Enter length of time in days"))
years = (length) // 365 
length = (length) - (years*365)
weeks = int(length) // 7
#days = int(length) % (weeks)
print (years)
print (weeks)
#print(days)



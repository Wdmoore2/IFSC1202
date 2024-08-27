length = int (input ("Enter length of time in days"))
years = (length) // 365 
length = (length) - (years*365)
weeks = (length) // 7 
length =(length) - (weeks*7)
days = (length)
print ("Years:" + str (years))
print ("Weeks:" + str (weeks))
print ("Days:" + str(days))
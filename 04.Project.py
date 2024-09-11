start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))

for n in range(start,end):
    for i in range(2, n//2+1):
        if n % i == 0:
            break
    else:
        print(n)

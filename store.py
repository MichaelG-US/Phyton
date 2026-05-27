hour = int(input("Enter the hour (0-23): "))

if hour >= 9 and hour < 17:
    print("The store is OPEN")
else:
    print("The store is CLOSED")
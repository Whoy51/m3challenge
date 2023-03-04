# United States

us_data = [369, 423, 416, 750, 928]

us_rateOfChange = []

for i in range(len(us_data)):
    if not len(us_data) - 1 <= i:
        us_rateOfChange.append(us_data[i + 1] / us_data[i])
        print(us_rateOfChange)

print("Finished: " + str(us_rateOfChange))

us_average = 0

for x in us_rateOfChange:
    us_average += x

us_average = us_average / (len(us_data) - 1)

print("Average rate of change (in 1000s): " + str(us_average))

# United Kingdom - DATA NEEDED

uk_data = []

uk_rateOfChange = []

for i in range(len(uk_data)):
    if not len(uk_data) - 1 <= i:
        uk_rateOfChange.append(uk_data[i + 1] / uk_data[i])
        print(uk_rateOfChange)

print("Finished: " + str(uk_rateOfChange))

uk_average = 0

for x in uk_rateOfChange:
    uk_average += x

uk_average = uk_average / (len(uk_data) - 1)

print("Average rate of change (in 1000s): " + str(us_average))
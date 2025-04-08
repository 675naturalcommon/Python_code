#使用break语句退出循环

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]

for city in cities:
    print(city)
    if city == "Phoenix":
        break
    # Output: New York
    #          Los Angeles
    #          Chicago
    #          Houston
    #          Phoenix

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]

for city in cities:
    if city == "Phoenix":
        break
    print(city)
    # Output: New York
    #          Los Angeles
    #          Chicago
    #          Houston

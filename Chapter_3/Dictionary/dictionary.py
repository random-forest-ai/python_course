if __name__ == '__main__':
    # Declare
    # x = {}
    # x = {"Apple": 1, 10000: [1,2,3]}
    x = dict( [("London", 9623), ("New York", 12947)] ) # dict(list of tuples)

    # x = {[1,2,3]: 100} # Not OK, keys should be immutable
    # x = {100: [1,2,3]}
    # x = {2: 4, 2: 6}
    x = {-2: 4, 2: 4}

    distance_from_HK = {"London": 9623, "New York": 12947,
                        "Lima": 18349, "Singapore": 2587}

    # distance_from_HK["London"]
    # distance_from_HK["Taipei"]

    # distance_from_HK.get("London")
    # distance_from_HK.get("Taipei")

    distance_from_HK["Vienna"] = 8729
    distance_from_HK.update({"Londres": 9623, "Wien": 8729})

    distance_from_HK["Istanbull"] = 80170

    # Modify
    distance_from_HK["Istanbull"] = 8017

    del distance_from_HK["Istanbull"]
    distance_from_HK["Istanbul"] = 8017

    val = distance_from_HK.pop("Wien")
    print(val)

    entry = distance_from_HK.popitem()
    print(entry)

    # Keys, values, items
    keys = distance_from_HK.keys()
    values = distance_from_HK.values()
    items = distance_from_HK.items()

    # Iterating through Dict
    # for city in distance_from_HK:
    #     print(city, end = " ")

    # for distance in distance_from_HK.values():
    #     print(distance, end = " ")

    for city, distance in distance_from_HK.items():
        print("The distance from Hong Kong to {} is: {} km".format(city, distance))
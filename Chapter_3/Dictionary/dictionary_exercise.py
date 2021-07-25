if __name__ == '__main__':
    distance_from_HK = {"London": 9623, "New York": 12947,
                        "Lima": 18349, "Singapore": 2587,
                        "Vienna": 8729, "Londres": 9623,
                        "Wien": 8729, "Istanbul": 8017}
    distance_in_miles = {}
    for city, distance in distance_from_HK.items():
        distance_in_miles[city] = distance * 0.621
    print(distance_in_miles)
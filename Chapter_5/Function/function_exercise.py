if __name__ == '__main__':
    def to_seconds(hour, minutes=0, seconds=0):
        return hour * 60 * 60 + minutes * 60 + seconds

    print(to_seconds(0, 25, 30))
distances = {
    "Voyager 1": 164,
    "Voyager 2": 134,
    "Pioneer 10": 80,
    "New Horizons": 54,
    "Pioner 11": 44
}


def main():
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")


def convert(au):
    return au * 149597870700         



main()
    

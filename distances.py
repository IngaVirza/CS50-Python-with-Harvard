distances = {
    "Voyager 1": 164,
    "Voyager 2": 134,
    "Pioneer 10": 80,
    "New Horizons": 54,
    "Pioner 11": 44
}


def main():

    spacecraft = input("Enter a spacecraft: ")
    try:
        au = float(distances[spacecraft])
    except KeyError:
        print(f"'{spacecraft}' is not in dictionary")

    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' to a float") 
        return   
    
    m = convert(au)
    print(f"{m} m away")

def convert(au):
    return au * 149597870700         



main()
    

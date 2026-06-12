def main():
    spacecraft = {"name": "Voyager 1"}
    spacecraft.update({"distance": 0.04, "orbit": "Sun"})
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f""""

    ======== REPORT ==============
    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")}
    Orbit: {spacecraft.get("orbit")}

    ==============================
    """


main()

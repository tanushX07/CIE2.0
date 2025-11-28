def calculate_speed(distance, time):
    if time == 0:
        return "Time cannot be zero"
    return distance / time

if _name_ == "_main_":
    distance = float(input("Enter distance (in km): "))
    time = float(input("Enter time (in hours): "))

    speed = calculate_speed(distance, time)
    print("Speed is:", speed, "km/h")

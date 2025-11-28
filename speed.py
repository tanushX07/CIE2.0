# speed.py

def calculate_speed(distance_km, time_hours):
    if time_hours == 0:
        return "Time cannot be zero."
    return distance_km / time_hours


if __name__ == "__main__":
    distance = 100  # km
    time = 2        # hours
    print("Speed:", calculate_speed(distance, time), "km/h")

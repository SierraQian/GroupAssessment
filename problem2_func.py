# problem2_func.py

def calc_number_of_seconds(time_period, unit):
    # Check if time_period is a non-negative float or integer
    if not (isinstance(time_period, (int, float)) and time_period >= 0):
        raise Exception("Time period must be a non-negative float or integer.")

    # Check if unit is a string
    if not isinstance(unit, str):
        raise Exception("Unit must be a string.")

    # Convert the time_period to seconds based on the given unit
    if unit == "second":
        return time_period
    elif unit == "minute":
        return time_period * 60
    elif unit == "hour":
        return time_period * 3600
    elif unit == "day":
        return time_period * 86400
    elif unit == "week":
        return time_period * 604800
    elif unit == "month":
        return time_period * 2592000
    elif unit == "year":
        return time_period * 31536000
    else:
        raise Exception("Invalid unit. Permissible values are 'second', 'minute', 'hour', 'day', 'week', 'month', and 'year'.")

from datetime import timedelta

def add_gigasecond(moment):
    time = moment + timedelta(seconds=1000000000)
    return time

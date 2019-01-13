from datetime import timedelta

def add_gigasecond(moment):
    """
    add a gigasecond to a specific moment 
    returns the new moment with the gigasecond added
    """
    time = moment + timedelta(seconds=1000000000)
    return time

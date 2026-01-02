from datetime import datetime

def convert_apple_time(apple_timestamp_ns):
    if apple_timestamp_ns is None:
        return None

    #Convert Apple nanosecond timestamps to EST datetime manually.
    #    Formula:
    #      1. Divide by 10^9 (nanoseconds to seconds)
    #      2. Add 978,307,200 (Apple Epoch → Unix Epoch)
    #      3. Subtract 18,000 (UTC → EST)
    #      4. Convert to datetime

    apple_epoch = apple_timestamp_ns /1_000_000_000
    unix_time = apple_epoch + 978_307_200
    est_time = unix_time - 18_000

    return datetime.utcfromtimestamp(est_time)
from datetime import datetime

"""
Given a datetime string in the format YYYY/MM/DD hh:mm, returns it as a datetime object.

- `datetime_string`: The datetime string to parse. Assumes the string is in the given format.
"""
def from_string_to_datetime(datetime_string):
    date_format = "%Y/%m/%d %H:%M"
    return datetime.strptime(datetime_string, date_format)

"""
Given two datetime strings in the format YYYY/MM/DD hh:mm or datetime objects, returns the time difference
between the datetimes in minutes.

- `dt1`: The first datetime object to compute the difference between.
- `dt2`: The second datetime object to compute the difference between.
"""
def get_time_difference_in_minutes(dt1="2024/01/01 00:01", dt2="2024/01/01 23:59"):
    assert(isinstance(dt1, datetime) or isinstance(dt1, str))
    assert(isinstance(dt2, datetime) or isinstance(dt2, str))

    if isinstance(dt1, str):
        dt1 = from_string_to_datetime(dt1)

    if isinstance(dt2, str):
        dt2 = from_string_to_datetime(dt2)

    return abs((dt1 - dt2).total_seconds()) / 60
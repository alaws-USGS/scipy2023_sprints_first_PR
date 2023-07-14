import math


def angle_to_sexigesimal(angle_in_degrees: float, decimals:int =3):
    """
    Convert the given angle to a sexigesimal string of hours of RA.

    Parameters
    ----------
    angle_in_degrees : float
        A scalar angle, expressed in degrees

    Returns
    -------
    hms_str : str
        The sexigesimal string giving the hours, minutes, and seconds of RA for
        the given `angle_in_degrees`

    """
    if type(decimals) != int:
        raise TypeError('decimals should be an integer!')

    hours_num = angle_in_degrees*24/360
    hours = math.floor(hours_num)
    str_hours = str(hours).zfill(2)

    min_num = (hours_num - hours)*60
    minutes = math.floor(min_num)
    str_minutes = str(minutes).zfill(2)

    seconds = round((min_num - minutes)*60, 2)
    str_seconds = str(seconds).zfill(2)

    format_string = f"{str_hours}:{str_minutes}:{str_seconds}"
    return format_string

test_angle = angle_to_sexigesimal(89)
print(test_angle)
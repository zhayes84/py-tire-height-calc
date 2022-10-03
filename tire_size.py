# tire_size.py


def sidewall_height(tread_width: int, sidewall: int) -> float:
    """
    Takes tread_width + sidewall as inputs and returns the sidewall height in inches.
    Sidewall height must be divided by 100 in order to be used correctly as a percentage value.
    ---
    Arguments:

    tread_width : int
        the tire width measured in millimeters
    sidewall : int
        the sidewall value listed on the tire size
    """
    return (tread_width * (sidewall / 100)) / 25.4


def wheel_height(tread_width: int, sidewall: int, rim: int) -> float:
    """
    Takes tread_width, sidewall, and rim values as inputs. The tread width value is sent as
    an argument to sidewall_height() which returns a float of the sidewall height in inches.
    Finally, wheel_height returns (sidewall height * 2) + rim size.
    ---
    Arguments:

    tread_width : int
        the tire width measured in millimeters
    sidewall : int
        the sidewall value listed on the tire size
    rim : int
        the height of the rim in inches
    """
    sidewall_height_value: float = sidewall_height(tread_width, sidewall)
    return (sidewall_height_value * 2) + rim


print(f"This wheel is: {wheel_height(225, 40, 16)} inches tall.\n")

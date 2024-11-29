"""import math
import warnings

# NEED TO UPDATE THIS
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def raise_custom_error_if_hit(radius, water_height):
    if radius <= 0:
        raise CustomError("Radius must be greater than 0.")#show customer error
    if water_height < 0:
        raise CustomError("Water height must be non-negative.")
    # Calculate the volume
    return math.pi * (radius ** 2) * water_height


def water_volume_warning(radius, water_height):
    if not isinstance(radius, (int, float)):
        warnings.warn("Radius has to be a number.")#show warning
    if not isinstance(water_height, (int, float)):
        warnings.warn("Water height has to be a number.")

    if isinstance(radius, (int, float)) and isinstance(water_height, (int, float)):
        try:
            return raise_custom_error_if_hit(radius, water_height)
        except CustomError as e:
            warnings.warn(e.message)
    return None
"""
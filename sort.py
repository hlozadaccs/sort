import math
from enum import StrEnum, auto

MAX_VOLUME = 1_000_000
MAX_DIMENSION = 150
MAX_MASS = 20


class PackageCategory(StrEnum):
    """
    Enum representing the category of a package:

    - NORMAL: not bulky or heavy
    - BULKY: large volume or oversized dimension
    - HEAVY: mass greater than or equal to 20 kg
    """

    NORMAL = auto()
    BULKY = auto()
    HEAVY = auto()


class Stack(StrEnum):
    """
    Enum representing the stack to which a package should be dispatched:

    - STANDARD: normal packages
    - SPECIAL: either bulky or heavy (but not both)
    - REJECTED: both bulky and heavy
    """

    STANDARD = auto()
    SPECIAL = auto()
    REJECTED = auto()


def validate_params(param: float) -> None:
    """
    Validates that the provided parameter is a positive float greater than 0.

    Args:
        param (float): A numeric value expected to be greater than 0.

    Raises:
        ValueError: If the value is less than or equal to 0.

    Returns:
        None: This function does not return any value.
              It raises an error if validation fails.
    """
    if param <= 0:
        raise ValueError(f"Invalid parameter value: {param}. Must be greater than 0.")


def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Sorts a package into the appropriate stack based on its volume and mass.

    A package is considered:
    - BULKY if its volume (width × height × length) is ≥ 1,000,000 cm³
      OR any of its dimensions is ≥ 150 cm.
    - HEAVY if its mass is ≥ 20 kg.

    Based on these conditions, packages are dispatched as follows:
    - STANDARD: neither bulky nor heavy
    - SPECIAL: either bulky or heavy (but not both)
    - REJECTED: both bulky and heavy

    Args:
        width (float): Package width in centimeters.
        height (float): Package height in centimeters.
        length (float): Package length in centimeters.
        mass (float): Package mass in kilograms.

    Returns:
        str: The name of the stack (STANDARD, SPECIAL, REJECTED) in uppercase.
    """
    volume_params = (width, height, length)
    volume_condition = math.prod(volume_params) >= MAX_VOLUME
    dimension_condition = any(val >= MAX_DIMENSION for val in volume_params)

    for param in volume_params + (mass,):
        try:
            validate_params(param)
        except ValueError:
            return Stack.REJECTED.upper()

    volume = dimension = PackageCategory.NORMAL
    if volume_condition or dimension_condition:
        volume = PackageCategory.BULKY

    if mass >= MAX_MASS:
        dimension = PackageCategory.HEAVY

    if volume == PackageCategory.NORMAL and dimension == PackageCategory.NORMAL:
        return Stack.STANDARD.upper()
    elif volume == PackageCategory.BULKY and dimension == PackageCategory.HEAVY:
        return Stack.REJECTED.upper()

    return Stack.SPECIAL.upper()

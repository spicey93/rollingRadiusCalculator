import math


def calc_rolling_radius(width, profile, diameter):

    def calc_sidewall_height(width, profile):
        return width * (profile / 100)

    def convert_inc_to_mm(inches):
        return inches * 25.4

    def calc_radius_from_diameter(diameter):
        return diameter / 2

    sidewall_height = calc_sidewall_height(width, profile)
    diameter_mm = convert_inc_to_mm(diameter)
    radius_mm = calc_radius_from_diameter(diameter_mm)

    # Return the outer circumference of the tyre
    return int(2 * math.pi * (radius_mm + sidewall_height))


# Return the difference between two circumferences as a percentage
def return_perc_dif(alt_circ, orig_circ):
    return f"{(alt_circ/orig_circ)*100-100:.1}%"


# Check that two values are within a certain range of each other
def is_within_range(alt_circ, orig_circ):
    if 1.005 > alt_circ / orig_circ > 0.995:
        return True
    return False

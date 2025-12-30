
EXPECTED_BAKE_TIME = 40
def bake_time_remaining(elapsed_bake_time):
    """
    Takes the elapsed baking time in minutes and returns the remaining baking time.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    Calculates preparation time based on the number of lasagna layers.
    Each layer takes 2 minutes to prepare.
    """
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculates the total cooking time.
    Includes preparation time and the time already spent baking.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time



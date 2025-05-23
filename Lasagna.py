"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the time to prepare the lasanga.
    
    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - time (in minutes) to prepare the lasagna
    
    Function that calculates how long it will take to prepare the lasagna determined by how
    many layers will be included and how long a layer takes as defined in 'PREPARATION_TIME
    """

    return number_of_layers * PREPARATION_TIME



#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    
    return number_of_layers * PREPARATION_TIME + elapsed_bake_time



# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)

print(EXPECTED_BAKE_TIME)
print(bake_time_remaining(30))
print(preparation_time_in_minutes(2))
print(elapsed_time_in_minutes(3, 20))
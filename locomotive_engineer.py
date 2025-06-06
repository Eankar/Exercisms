"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """

    *wagon_list, = args
    return wagon_list


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    wagon_one, wagon_two, wagon_three, *rest = each_wagons_id

    *remaining, = missing_wagons

    #wagon_list = []

    *wagon_list, = wagon_three, *remaining, *rest, wagon_one, wagon_two

    print(wagon_one)
    print(wagon_two)
    print(*rest)
    print(wagon_list)
    return wagon_list


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    route["stops"] = list(kwargs.values())

    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    output = {**route, **more_route_information}

    return output


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    
    col_1, col_2, col_3, = zip(*wagons_rows)

    return[list(col_1), list(col_2), list(col_3)]

#fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15])
#add_missing_stops({'from': 'Berlin', 'to': 'Hamburg'}, **{'stop_1': 'Lepzig', 'stop_2': 'Hannover', 'stop_3': 'Frankfurt'})
fix_wagon_depot([[(2, 'red'), (4, 'red'), (8, 'red')], [(5, 'blue'), (9, 'blue'), (13, 'blue')], [(3, 'orange'), (7, 'orange'), (11, 'orange')]])
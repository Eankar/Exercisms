def transform(legacy_data):
    point_values = dict()

    for key, values in legacy_data.items():
        #point_values[key] = value
        for value in values:
            point_values[value.lower()] = key

    return point_values
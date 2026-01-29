def transform(legacy_data):
    data = dict()
    for i, val in legacy_data.items():
        for j in val:
            data[j.lower()] = i
    return data
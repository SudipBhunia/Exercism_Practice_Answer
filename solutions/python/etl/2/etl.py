def transform(legacy_data):
    return {
        num.lower() : key
        for key, val in legacy_data.items()
        for num in val
    }
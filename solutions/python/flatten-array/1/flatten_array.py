def flatten(iterable):
    result = []
    
    for item in iterable:
        if item is None:
            continue
        elif isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    
    return result


def flatten_generator(iterable):
    for item in iterable:
        if item is None:
            continue
        elif isinstance(item, list):
            yield from flatten_generator(item)
        else:
            yield item


def flatten_oneliner(iterable):
    return [
        item
        for element in iterable
        for item in (flatten_oneliner(element) if isinstance(element, list) else [element])
        if item is not None
    ]
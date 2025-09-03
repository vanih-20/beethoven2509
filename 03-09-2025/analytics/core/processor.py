from .validator import validate_data #sibling module calling

def process_data(data):
    if validate_data(data):
        return f"Processed data: {data}"
    else:
        return "Invalid data"
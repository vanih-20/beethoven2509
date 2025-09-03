from ..tools.formatter import format_data #if need to call from other module, 1st call parent using ..

def write_data(data):
    formatted_data = format_data(data)
    return f"Written: {formatted_data}"
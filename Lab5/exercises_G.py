def merge_settings(defaults, **overrides):
    settings = {**defaults}
    for key, value in overrides.items():
        settings[key] = value

    return settings

def call_summary(function_name, *args, **kwargs):
    return f"Calling {function_name} with args {args} and kwargs {kwargs}"

def statistics(*numbers):
    min_value = None
    max_value = None
    counts = len(numbers) 
    total = sum(numbers)
    
    if not numbers:
        return {
            'counts': counts,
            'total': None,
            'max': max_value,
            'min': min_value,
            'average': None
        } 

    for number in numbers:
        if min_value is None or min_value > number:
            min_value = number
        if max_value is None or max_value < number:
            max_value = number

    return {
        'counts': counts,
        'total': total,
        'max': max_value,
        'min': min_value,
        'average': total/counts
    }

# --- Main like section ---
defaults = {'volume':10, 'on': True, 'schedule': None, 'lobation': 'Unknown', 'owner': 'default'}
numbers = [1, 3, 4, 5, 6, -10, 113]

print(merge_settings(defaults, volume = 55, location = 'Stockholm'))

print(call_summary('function', 10, 20, **defaults))

print(statistics(*numbers))
print(statistics())
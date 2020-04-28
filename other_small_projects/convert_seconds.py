def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remianing_seconds = seconds - hours*3600 - minutes*60
    return hours, minutes, remianing_seconds

result = convert_seconds(5000)
print(type(result))
hours, minutes, seconds = result

print(hours, minutes, seconds)
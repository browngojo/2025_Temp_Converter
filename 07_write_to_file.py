from datetime import date

calculations = ['Converting 10.0°F to -12°C', 'Converting 20.0°F to -7°C',
                'Converting 30.0°F to -1°C', 'Converting 40.0°F to 4°C',
                'Converting 50.0°F to 10°C', 'Converting 60.0°F to 16°C']

# ***** Get current date for heading and filename *****
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

file_name = f"temperatures_{year}_{month}_{day}"
write_to = f"{file_name}.txt"

with open(write_to, "w") as text_file:

    text_file.write("***** Temperature Calculations ***** \n")
    text_file.write(f"Generated: {day}/{month}/{year}\n\n")
    text_file.write("Here is your calculation history (oldest to newest)...\n")

    # write the item to file
    for item in calculations:
        text_file.write(item)
        text_file.write("\n")


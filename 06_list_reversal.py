all_calculations = ['Converting 10.0°F to -12°C', 'Converting 20.0°F to -7°C',
                    'Converting 30.0°F to -1°C', 'Converting 40.0°F to 4°C',
                    'Converting 50.0°F to 10°C', 'Converting 60.0°F to 16°C']

newest_first = list(reversed(all_calculations))

print("=== Oldest to Newest ===")
for item in all_calculations:
    print(item)

print()
print("=== Most Recent First ===")
for item in newest_first:
    print(item)
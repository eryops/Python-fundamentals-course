seconds = int(input("Enter the number of seconds: "))
whole_hours = seconds // 3600
remaining_minutes_after_hours = (seconds % 3600) // 60
remaining_seconds_after_minutes = seconds % 60

print(f"""
Time Conversion:
Total Seconds: {seconds}
Whole Hours: {whole_hours}
Remaining Minutes (after hours): {remaining_minutes_after_hours}
Remaining Seconds (after minutes): {remaining_seconds_after_minutes}
""")

four_digit_number = 2345
print(four_digit_number // 1000)
print(four_digit_number // 100 % 10)
print(four_digit_number // 10 % 10)
print(four_digit_number % 10)

text = input("Enter some text: ")
if len(text) >= 4:
    text = text[:2] + ("*" * (len(text) - 4)) + text[-2:]

print(text)

# predict the value output
value = int('1') + 3
print(value)

text = "Python"
print(text[1:4])

print(text[-4:])

numbers = [10, 20, 30]
print(numbers[2]*2)

name = "Johanna"
print(name[::-1])
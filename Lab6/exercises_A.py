squares_for_loop = []
for number in range(1, 21):
    squares_for_loop.append(number ** 2)
print(squares_for_loop)

squares_list_compression = [number ** 2 for number in range(1, 21)]
print(squares_list_compression)

even_numbers_list = [number for number in range(1, 100) if number % 2 == 0]
print(even_numbers_list)

names = ['berit  ', 'JONAS', ' anna']
normalize_names = [name.strip().title() for name in names]
print(normalize_names)

scores = [34, 45, 67, 88, 3, 6]
passing_scores = [score for score in scores if score >= 34]
print(passing_scores)

passing_scores_labels = ['PASS' if score >= 34 else 'FAIL' for score in scores]
print(passing_scores_labels)

numbers = [1, 4, 9, 6]

# sum_of_numbers = 0
# for number in numbers:
#     sum_of_numbers += number
# print(sum_of_numbers)

sum_of_numbers = sum(number for number in numbers)

# largest_number = 0
# for number in numbers:
#     if number > largest_number:
#         largest_number = number
# print(largest_number)
largest_number = max(number for number in numbers)

# passes = 0
# fails = 0
# for score in scores:
#     if score >= 70:
#         passes += 1
#     else:
#         fails += 1

passed = sum(1 for score in scores if score >= 70)
fails = sum(1 for score in scores if score < 70)

print(passed)
print(fails)

list_with_numbers = [4, 7, 2, 7, 9, 4, 3, 8, 2, 10, 3, 3, 11, 7]
# duplicates = set()
# seen = set()

# for number in list_with_numbers:
#     if number in seen:
#         duplicates.add(number)
#     else:
#       seen.add(number)
duplicates = [number for number in list_with_numbers if list_with_numbers.count(number) > 1]
print(duplicates)
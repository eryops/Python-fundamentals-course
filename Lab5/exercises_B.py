def add_all(*numbers):
    total = 0

    for number in numbers:
        total += number
    return total

def average(*numbers):
    if not numbers:
        return "No numbers where supplied"

    total = 0
    for number in numbers:
        total += number

    return total / len(numbers)

def longest_word(*words):
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def build_sentence(separator, *words):
    string = ""
    for word in words:
        if not string:
            string = word
        else:
            string += separator + word
    return string

def describe_scores(student_name, *scores):
    number_of_scores = len(scores)
    if not scores: 
        average_score = None
    else:
        total_scores = 0
        for score in scores:
            total_scores += score
        average_score = total_scores/number_of_scores

    return {'name': student_name, 'number_of_scores': number_of_scores, 'average_score': average_score}

# --- Main like section ---
print(add_all(4,5,6,3,4))

print(average())
print(average(3,4,5,6,47))

print(longest_word('word', 'long', 'horse', 'forest'))

print(build_sentence(' ','word', 'long', 'horse', 'forest'))
print(build_sentence('*','word', 'long', 'horse', 'forest'))

print(describe_scores('Lisa'))
print(describe_scores('Stina', 4,4,3,4))

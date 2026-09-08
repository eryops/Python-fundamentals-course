word = "algorithm"

print(word[:3])  # prints the first alg
print(word[-3:])  # prints the last thm
print(word[::-1])  # prints the string in reverse order
print(word[::2])  # prints every second character agrtm
print(word[1::2]) # prints every second character starting from index 1 lroih
print(word[2:5])  # prints the characters from index 2 to 4 gor
print(word[-3:])  # prints the characters from index -3 thm
print(word[3:])  # prints the characters from index 3 to the end rithm

text = "Artificial Intelligence"
print(text[:10])  # prints the first 10 characters Artificial
print(text[10:21])  # prints characters from index 10 to 20 Intelligence
print(text[-10:])  # prints the last 10 characters telligence
print(text[::-1])  # prints the string in reverse order ecnegilletnI laicifitrA
print(text[::2])  # prints every second character Atfca nelgne
print(text[1:6:2]) # prints every second character starting from index 1 to index 5 irii

text = "Data Science    "
print(text.strip())  # prints the string without leading and trailing whitespace Data Science
print(text.split())  # splits the string into a list of words ['Data', 'Science']
print(text.replace("Data", "Big"))  # replaces "Data" with "Big Data" Big Data Science

text = "word"
# text[0] = "o"  # This will raise an error because strings are immutable in Python
text = text.replace("w", "o")
print(text)  # prints "oord"
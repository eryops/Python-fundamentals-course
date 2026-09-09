books = [
    {
        "title": "boken",
        "author": "en person",
        "pages": 345,
        "available": False
    },
    {
        "title": "Flera författare",
        "author": "Ingen vet",
        "pages": 400,
        "available": True
    },
    {
        "title": "En flygande get",
        "author": "the goat",
        "pages": 35,
        "available": True
    },
    {
        "title": "Python coding",
        "author": "Ormen",
        "pages": 333,
        "available": True
    },
    {
        "title": "Min självbiografi",
        "author": "Grodan Cermit",
        "pages": 345,
        "available": False
    }
    
]

print("Third author: ", books[2]["author"])
print("Third author: ", books[-1]["available"])

books[0]["author"] = "Greta Gris"
print(books[0])

books[-1]["score"] = 2
print(books[-1])

departments = {
    "dep_1": ['Greger', 'Lisa'],
    "dep_2": ['Yngve', 'Stina', 'Berit'],
    "dep_3": ['Yrsa', 'Lena', 'Ann-Britt'],
    "dep_4": ['Lars', 'Arne', 'Kurt']
}

courses = [
    {
        "name": "Python Basics",
        "teacher": "Anna",
        "topics": ["variables", "loops", "functions"]
    },
    {
        "name": "Web Development",
        "teacher": "Johan",
        "topics": ["HTML", "CSS", "JavaScript"]
    },
    {
        "name": "Databases",
        "teacher": "Maria",
        "topics": ["SQL", "joins", "indexes"]
    }
]

print(courses[2]["topics"][0])
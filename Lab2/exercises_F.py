catalogue = [
    {
        "title": "Inception",
        "year": 2010,
        "genre": "Sci-Fi",
        "rating": 8.8,
        "identifier": ('ID1', 2022)
    },
    {
        "title": "The Witcher 3",
        "year": 2015,
        "genre": "RPG",
        "rating": 9.3,
        "identifier": ('ID2', 2022)
    },
    {
        "title": "Interstellar",
        "year": 2014,
        "genre": "Sci-Fi",
        "rating": 8.6,
        "identifier": ('ID3', 2022)
    },
    {
        "title": "The Last of Us",
        "year": 2013,
        "genre": "Action/Drama",
        "rating": 9.7,
        "identifier": ('ID4', 2022)
    },
    {
        "title": "Dune",
        "year": 2021,
        "genre": "Sci-Fi",
        "rating": 8.0,
        "identifier": ('ID5', 2022)
    },
    {
        "title": "Hades",
        "year": 2020,
        "genre": "Fantasy",
        "rating": 9.0,
        "identifier": ('ID6', 2022)
    },
    {
        "title": "The Hobbit",
        "year": 1937,
        "genre": "Fantasy",
        "rating": 9.1,
        "identifier": ('ID7', 2022)
    },
    {
        "title": "Portal 2",
        "year": 2011,
        "genre": "Puzzle",
        "rating": 9.5,
        "identifier": ('ID8', 2022)
    }
]


unique_genres  = {item["genre"] for item in catalogue}

print(unique_genres)

print(catalogue[0]["title"])
print(catalogue[-1]["identifier"][0])
print(catalogue[-3]["rating"])
print(catalogue[2]["rating"])
print(catalogue[5]["genre"])
print(catalogue[5].values())
print(catalogue[2].keys())
print(catalogue[-2].items())

catalogue[0]["director"] = "Christopher Nolan"
catalogue[2]["identifier"] = ("ID-new", catalogue[1]["year"])

print(f"""
Item 1:
Title: {catalogue[0]["title"]}
Year: {catalogue[0]["year"]}
Genre: {catalogue[0]["genre"]}
Rating: {catalogue[0]["rating"]}
Identifier: {catalogue[0]["identifier"]}
Director: {catalogue[0]["director"]}
""")
print(f"""
Item 2:
Title: {catalogue[1]["title"]}
Year: {catalogue[1]["year"]}
Genre: {catalogue[1]["genre"]}
Rating: {catalogue[1]["rating"]}
Identifier: {catalogue[1]["identifier"]}
""")
print(f"""
Item 3:
Title: {catalogue[2]["title"]}
Year: {catalogue[2]["year"]}
Genre: {catalogue[2]["genre"]}
Rating: {catalogue[2]["rating"]}
Identifier: {catalogue[2]["identifier"]}
""")
print(f"""
Item 4:
Title: {catalogue[3]["title"]}
Year: {catalogue[3]["year"]}
Genre: {catalogue[3]["genre"]}
Rating: {catalogue[3]["rating"]}
Identifier: {catalogue[3]["identifier"]}
""")
print(f"""
Item 5:
Title: {catalogue[4]["title"]}
Year: {catalogue[4]["year"]}
Genre: {catalogue[4]["genre"]}
Rating: {catalogue[4]["rating"]}
Identifier: {catalogue[4]["identifier"]}
""")
print(f"""
Item 6:
Title: {catalogue[5]["title"]}
Year: {catalogue[5]["year"]}
Genre: {catalogue[5]["genre"]}
Rating: {catalogue[5]["rating"]}
Identifier: {catalogue[5]["identifier"]}
""")
print(f"""
Item 7:
Title: {catalogue[6]["title"]}
Year: {catalogue[6]["year"]}
Genre: {catalogue[6]["genre"]}
Rating: {catalogue[6]["rating"]}
Identifier: {catalogue[6]["identifier"]}
""")
print(f"""
Item 8:
Title: {catalogue[7]["title"]}
Year: {catalogue[7]["year"]}
Genre: {catalogue[7]["genre"]}
Rating: {catalogue[7]["rating"]}
Identifier: {catalogue[7]["identifier"]}
""")
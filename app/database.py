import json

def save_languages(languages_data):
    try:
        with open("languages.json", "w") as file:
            json.dump(languages_data, file)
    except Exception as e:
        print("Error saving languages:", e)

def load_languages():
    try:
        with open("languages.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# languages = {
# "language": "C",
# "appeared": 1972,
# "created": [
# "Dennis Ritchie"
# ],
# "functional": True,
# "object-oriented": False,
# "relation": {
# "influenced-by": [
# "B",
# "ALGOL 68",
# "Assembly",
# "FORTRAN"
# ],
# "influences": [
# "C++",
# "Objective-C",
# "C#",
# "Java",
# "JavaScript",
# "PHP",
# "Go"
# ]
# }
# }
    
# languages = {
#     "language": "C",
#     "appeared": 1972,
#     "created": ["Dennis Ritchie"],
#     "functional": True,
#     "object_oriented": False,
#     "relation": {
#         "influenced-by": ["B", "ALGOL 68", "Assembly", "FORTRAN"],
#         "influences": ["C++", "Objective-C", "C#", "Java", "JavaScript", "PHP", "Go"]
#     }
# }
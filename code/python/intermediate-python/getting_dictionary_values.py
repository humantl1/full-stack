courses = {
    "js": "JavaScript 101",
    "python": ["Python 101", "Python 201"],
    "html": "HTML 101"
}

# arguments(<key to return>, <optional: if key doesn't exist(default=None)>)
print(courses.get("js"))
print(courses.get("css", "Not found"))
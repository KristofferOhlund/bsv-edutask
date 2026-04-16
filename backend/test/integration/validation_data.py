OK_VALIDATION_DATA = [
    ("task", {"title": "1", "description": "my_description"},  # Created task object
     object),
    ("todo", {"description": "my_description"},  # Created Todo object
     object),
    ("user", {"firstName": "Exempel", "lastName": "Pettersson", "email": "email@hello.org"},  # Created user object
     object),
    ("video", {"url": "https://yahoo.com"},  # Created video object
     object),
]

INVALID_VALIDATION_DATA = [
    # TASK
    ("task", [], 'Document failed validation'),  # input data is array
    ("task", {"titles": "1", "description": "my_description"},  # title exists
     'Document failed validation'),
    ("task", {"title": 1, "description": "my_description"},  # title is string
     'Document failed validation'),
    ("task", {
        # title is empty
        "title": "", "description": "my_description"}, 'Document failed validation'),
    ("task", {"title": "1", "descriptions": 1},  # description is exists
     'Document failed validation'),
    ("task", {"title": "1", "description": 55},  # description is string
     'Document failed validation'),
    ("task", {"title": "1", "description": ""},  # description is empty string
     'Document failed validation'),
    ("task", {"title": "1", "description": "my_description"},  # Title is unique
     'Document failed validation'),

    # _TODO
    ("todo", [], 'Document failed validation'),  # input data is array
    ("todo", {"title": "1", "descriptions": 1},  # description does not exists
     'Document failed validation'),
    ("todo", {"title": "1", "description": 55},  # description is not string
     'Document failed validation'),
    ("todo", {"title": "1", "description": ""},  # description is empty string
     'Document failed validation'),
    ("todo", {"title": "1", "description": "my_description"},  # Description is unique (object already created)
     'Document failed validation'),

    # USER
    ("user", [], 'Document failed validation'),  # input data is array
    ("user", {"firstNam": "name", "lastName": "lastName", "email": "email@hello.org"},  # No firstName
     'Document failed validation'),
    ("user", {"firstName": 1, "lastName": "lastName", "email": "email@hello.org"},  # First name is int
     'Document failed validation'),
    ("user", {"firstName": "", "lastName": "lastName", "email": "email@hello.org"},  # First name empty
     'Document failed validation'),
    ("user", {"firstName": "", "no last": "name", "email": "email@hello.org"},  # Last name does not exist
     'Document failed validation'),
    ("user", {"firstName": "", 1: "lastName", "email": "email@hello.org"},  # Last name is int
     'Document failed validation'),
    ("user", {"firstName": "", "lastName": "", "email": "email@hello.org"},  # Last name empty
     'Document failed validation'),
    ("user", {"firstName": "", "lastName": "lastName", "no mail": "email@hello.org"},  # email does not exist
     'Document failed validation'),
    ("user", {"firstName": "", "lastName": "lastName", "email": ["email@mail.org"]},
     'Document failed validation'),


    ("user", {"firstName": "", "lastName": "lastName", "email": ""},  # email is empty
     'Document failed validation'),
    # VIDEO
    ("video", [], 'Document failed validation'),  # input data is array
    # url does not exist
    ("video", {"urls": ""}, 'Document failed validation'),
    ("video", {"url": 55}, 'Document failed validation'),  # url is not string
    # url is empty string
    ("video", {"url": ""}, 'Document failed validation'),
]

import InputValidator
import datetime

userDataFields = {
    "firstname":"John",
    "lastname":u"Smith",
    "age":19,
    "birthday":datetime.datetime.now(),
    "gender":u"male",
    "weight":150,
    "email":"john.smith@gmail.com",
}


expectedDataFields = {
        "firstname":[str, unicode],
        "lastname":[str, unicode],
        "email":"[a-zA-Z0-9\.\-\_]+@[a-zA-Z]+\.[a-zA-Z]",
        "age":{
            "required":True,
            "type":int,
            "min":18,
            "max":120,
            "default":0,
            },
        "birthday":datetime.datetime,
        "gender":{
            "required":False,
            "type":unicode
        },
        "weight":{
            "required":False,
            "type":int
        }
}

validator = InputValidator.Validator(expectedDataFields, userDataFields)
print validator.validate()


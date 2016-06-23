import InputValidator
import datetime

userDataFields = {
    "firstname":u"John",
    "lastname":u"Smith",
    "age":45,
    "birthday":datetime.datetime.now(),
    "gender":u"male",
    "weight":150,
    "email":"john.smith@gmail.com",
}


expectedDataFields = {
        "firstname":unicode,
        "lastname":unicode,
        "email":"[a-zA-Z0-9\.\-\_]+@[a-zA-Z]+\.[a-zA-Z]",
        "age":{
            "required":True,
            "type":int,
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


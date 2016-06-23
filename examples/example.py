import InputValidator
import datetime

userDataFields = {
    "firstname":u"John",
    "lastname":u"Smith",
    "age":45,
    "birthday":datetime.datetime.now(),
    "gender":u"male",
    "weight":150,
}


expectedDataFields = {
        "firstname":unicode,
        "lastname":unicode,
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


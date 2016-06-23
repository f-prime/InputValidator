Overview
========

A small module that is used as an input validator for untrusted form data. Mainly meant to be used for validating data before being inserted into a database such as MongoDB. 


Docs
===

`class Validator(formValidationDict, userInputDict)`

`def validator()` -> Returns filtered userInputDict if successful, otherwise returns None


Building Expected Data Dictionary
---------------------------------

This is passed as the first argument when creating an instance of the Validator class. 

expected data is a dictionary that describes the names of the input fields expected mapped to the types that they should be.

    fields = {
        "firstname":unicode,
        "lastname":unicode,
        "age":int
    }

By default all fields are required and will raise an error when not in the user input dictionary (the second argument in the class instantiation)
If more complex logic is needed, the type can be replaced with a dictionary that would look like the following

    {
        "required":<bool>,
        "type":<type>,
        "default":<default value set if required is True>
    }

`required` and `type` are required fields while `default` is optional.

Using the above, another fields dictionary might look like the following

    fields = {
        "firstname":unicode,
        "lastname":unicode,
        "age":int
        "birthday":{
            "required":False,
            "type":datetime.datetime
        }
    }


If birthday is not passed in the use input data dictionary then no error will be raised.

Example
=======


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


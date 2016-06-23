Overview
========

A small module that is used as an input validator for untrusted form data. Mainly meant to be used for validating data before being inserted into a database such as MongoDB. 


Docs
===

`class Validator(formValidationDict, userInputDict)`

`def validator()` -> Returns filtered userInputDict if successful, otherwise returns `None`


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

`required` and `type` are required fields while `default` is optional, however if you use `default` on a required field and the required field is not found the `default` will be used.

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

The field types can also be a regex pattern. For example, If I wanted to verify that a field is a valid email, I might do something like the following.

    fields = {
        "email":"[a-zA-Z0-9\.\-\_]+@[a-zA-Z]+\.[a-zA-Z]"
    }

If the `email` field does not match this pattern `None` will be returned when `.validator()` is called.


Type fields can also contain multiple types using a list of types.

    fields = {
        "money":[int, float],
    }


The `money` field will have to match one of the two types `int` or `float`

Int types can contain ranges as well

    fields = {
        "age":{
            "required":True,
            "min":18,
            "max":110,
            "type":int
        }
    }

Example
=======

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

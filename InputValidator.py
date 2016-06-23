import re

class Validator:
    def __init__(self, fields, form, debug=False):
        """
            fields = {
                "firstname":unicode,
                "lastname":unicode,
                "age":int,
                "birthday":datetime.datetime,
            }

            OR

            fields = {
                "firstname":{
                    "required":True,
                    "type":unicode,
                    "default":"John" # Optional
                }

                "lastname": {
                    "required":True,
                    "type":unicode,
                    "default":"Smith",
                }

                "age":{
                    "required":False,
                    "type":int,
                }
            }


            fields = <dictionary of form data submitted by user>

        """
        self.fields = fields
        self.form = form
        self.debug = debug
        
    def validate(self):

        """
            Views the form restrictions (self.fields) and the form (self.form) and checks whether the inputs are valid or not based on the types provided in the self.fields variable.

            If it's valid the filtered form is returned with any extra values removed.

            Otherwise None is returned.
        """

        output = {}
        for field in self.fields:
            if type(self.fields[field]) == dict:
                required = self.fields[field]['required']
                type_ = self.fields[field]['type']
                default = "default" in self.fields[field]

                if required and field not in self.form:
                    if default:
                        output[field] = self.fields[field]['default']
                    else:
                        self.__debug(1)
                        return None
                elif required:
                    if type(self.form[field]) != type_ and self.form[field] != None:
                        self.__debug(2)
                        return None

            elif field not in self.form: # Means there is no default and the field just does not exist
                self.__debug(3)
                return None

            elif type(self.fields[field]) == str: # Meaning regex
                pattern = self.fields[field]
                if re.search(pattern, self.form[field]) == None and self.form[field] != None:
                    self.__debug(4)
                    return None
            else:
                if type(self.form[field]) != self.fields[field] and self.form[field] != None:
                    self.__debug(5)
                    return None
            
            output[field] = self.form[field]
                
        return output

    def __debug(self, code):
        if self.debug == True:
            print code

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

                elif (type_ == int or type_ == float) and field in self.form and self.form[field] != None:
                    if "min" in self.fields[field]:
                        if self.form[field] < self.fields[field]['min']:
                            self.__debug(6)
                            return None
                    if "max" in self.fields[field]:
                        if self.form[field] > self.fields[field]['max']:
                            self.__debug(7)
                            return None
                
                elif required:
                    if not self.__typeprocess(field):
                        return None

            elif field not in self.form: # Means there is no default and the field just does not exist
                self.__debug(3)
                return None

            elif not self.__typeprocess(field):
                return None

            if field in self.form:
                output[field] = self.form[field]
                
        return output

    def __typeprocess(self, field):
        form = self.form[field]
        _type = self.fields[field]
        
        if type(_type) == dict:
            _type = self.fields[field]['type']

        self.__debug([type(form), _type])

        if self.form[field] == None:
            self.__debug(1)
            return True

        elif type(_type) == type and type(form) != _type:
            self.__debug(2)
            return False

        elif type(_type) == str:
            if re.search(_type, form) == None:
                self.__debug(3)
                return False

        elif type(_type) == list:
            if type(form) not in _type:
                self.__debug(4)
                return False

        return True

    def __debug(self, code):
        if self.debug == True:
            print code

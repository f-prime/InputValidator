class Validator:
    def __init__(self, fields, form):
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
                        print 1
                        return None
                elif required:
                    if type(self.form[field]) != type_:
                        print 2
                        return None
                    output[field] = self.form[field]
                elif field in self.form:
                    output[field] = self.form[field]

            else:
                if field not in self.form:
                    print 3
                    return None
                elif type(self.form[field]) != self.fields[field]:
                    print field
                    print 4
                    return None
                output[field] = self.form[field]
                
        return output

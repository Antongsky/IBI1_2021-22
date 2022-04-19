class Staff():
    def __init__(self,first_name,last_name,location,role):
        self.first_name=first_name
        self.last_name=last_name
        self.location=location
        self.role=role
    def info(self):
        return "Full name: %s %s, location: %s, role: %s." %(self.first_name,self.last_name,self.location,self.role)
        
#Example
a=Staff(first_name="Antongsky",last_name="Lin",location="International campus",role="faculty")
print(a.info())
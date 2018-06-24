class Developer:
    
    def __init__(self, name, age, oss_projects):
        self._name = name
        self._age = age
        self._oss_projects = oss_projects
    
    def name(self):
        return self._name 
    
    def age(self):
        return self._age
    
    def oss_projects(self):
        return self._oss_projects


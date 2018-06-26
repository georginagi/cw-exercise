from operator import itemgetter, methodcaller

class Developer:
    
    def __init__(self, name, age, oss_projects):
        self.name = name
        self.age = age
        self.oss_projects = oss_projects

    def __repr__(self):
        return repr((self.name, self.age, self.oss_projects))
from operator import itemgetter, attrgetter

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

    def sort_by(self, args):
        pass


devs = []
devs.append(Developer("Sofia", 27, 5))
devs.append(Developer("Anna", 27, 4))
devs.sort(key=lambda x: x._oss_projects, reverse=True)
for dev in devs:
    print("Name: {}, Age: {}, OSS_Projects: {}".format(dev.name(), dev.age(), dev.oss_projects()))
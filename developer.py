from operator import itemgetter, methodcaller

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

    def sort_by(self, args, reverse):
        if len(args)==0:
            print("invalid")
        elif len(args)==1:
            devs.sort(key=lambda x: x._oss_projects, reverse=True)
        else:
            devs.sort(key=lambda x, y: (x._name - x._oss_projects), reverse=False)
devs = [
    Developer("John", 29, 3),
    Developer("Linda", 29, 5),
    Developer("Robert", 24, 1),
    Developer("Amanda", 21, 8),
    Developer("Lawrence", 32, 2),
    Developer("Steven", 24, 4)
    ]
#devs.sort(key=lambda x: (x._age + x._oss_projects), reverse=False)
for dev in sorted(devs, key=methodcaller('name')):
    print("Name: {}, Age: {}, OSS_Projects: {}".format(dev.name(), dev.age(), dev.oss_projects()))
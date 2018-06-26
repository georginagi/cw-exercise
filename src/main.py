from operator import itemgetter, attrgetter, methodcaller
import argparse
from developer import Developer
from cmd import Cmd 
import argparse


class MyPrompt(Cmd):

    def do_help(self, args):
        help_message = """
                        ****  List of commands ****
                        - show_list
                        Shows the existing data
                        - add_developer
                        Adds a certain developer to a list given a name, age and number of oss_projects
                        - add_developers
                        Add more than one developer at once given a type of file --- not implemented
                        - order_by
                        Order the list of developers given a certain set of filters, enter the command followed by the specified filters seperated by space
                        - exit
                        Exit command line
                       """
        print(help_message)
    
    def do_exit(self, args):
        print("Exiting...")
        raise SystemExit
    
    def do_show_list(self, args):
        if len(args) == 0:
            self.do_show_list(devs)
        for dev in args:
            print("Name: {}, Age: {}, OSS_Projects: {}".format(dev.name, dev.age, dev.oss_projects))
    
    def do_add_developer(self, args):
        if len(args.split(" ")) < 3:
            print("Specify name, age and oss projects")
        else:
            print("Adding new developer to our list...")
            devs.append(Developer(args.split(" ")[0], args.split(" ")[1], args.split(" ")[2]))
            self.do_show_list(devs)
    
    def do_add_developers(self, file):
        pass

    def do_sort_by(self, args):
        args_len = len(args.split(" "))
        if args_len==0:
            print("Specify filters: name and/or age and/or oss_projects as well as ASC or DESC order")
        filters = []
        filters = args.split(" ")
        if 'DESC' in filters[args_len-1]:
            reverse = True
            filters.remove('DESC')
        else: 
            reverse = False

        print("==============================")
        self.do_show_list(self.sort_by_attributes(devs, filters, reverse))

    def sort_by_attributes(self, devs, filters, reverse):
        sorted_devs = []
        sorted_devs = sorted(devs, key=attrgetter(*filters), reverse=reverse)
        return sorted_devs

if __name__ == '__main__':
    print("Setting up initial list...")
    devs = [
        Developer("John", 29, 3),
        Developer("Linda", 29, 5),
        Developer("Robert", 24, 1),
        Developer("Amanda", 21, 8),
        Developer("Lawrence", 32, 2),
        Developer("Steven", 24, 4)
    ]
    prompt = MyPrompt()
    prompt.do_show_list(devs)
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt... Type help for list of commands')

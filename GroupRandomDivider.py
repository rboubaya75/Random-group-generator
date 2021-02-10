


GROUP RANDOM DIVIDER 

"""
This script aims to divid a group of students in several groups. A list of names is to be loaded or entered directely by the user.
"""

import random
import json 
import logging


LogFormat='%(name)s - %(levelname)s - %(message)s'

logging.basicConfig(filename='GroupDivisor.log', level=logging.DEBUG,format=LogFormat,filemode="w")
logger=logging.getLogger()


logger.info("Group division has started")

class Student_divisor():
    
    def __init__ (self):

        self.list_names=[]
        self.nb_groups=int(input("inter a group numb :"))
        logging.warning('please enter an integer')
        #self.file="students.txt"
      
  
    def Student_list(self):
        
        self.list_names = input("enter students' names separated by a space: ").split(" ")
        logging.warning("to make the script function, names must be be separated by as space")

        self.list_names= list(map(lambda s: s.strip(), self.list_names)) 

        return self.list_names

        logger.info("Students'list has been successfully filled")
        """
        with open('students.txt', 'r' ) as f:
            self.list_names = f.readlines()
            self.list_names=list(map(lambda s: s.strip(), self.list_names)) 
            return self.list_names
        """
        
    def groups(self,list_names):

    
        self.n= int(len(self.list_names)/(self.nb_groups))

        for i in range (self.nb_groups):

            self.selected = random.sample(self.list_names,self.n)
        
            print("Group n°%s : %s" % (i,self.selected))

        
            for sel in self.selected:
                self.list_names.remove(sel)
logger.info("Group division has been successfully completed")
    
            

def Main():
    
    s=Student_divisor()
    s.groups(s.Student_list())

Main()

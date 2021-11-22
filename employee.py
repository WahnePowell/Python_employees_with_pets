import pet

class Employee:
   'Common base class for all employees'
   empCount = 0
   
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def fedPet(self, obj):
      obj.isfed = True
      
##   def displayCount():
##     print ("Total Employees: %d" % empCount)
##     print("Total Employees: " + empCount)
##     return Employee.empCount

   def displayEmployee(self):
      print ("Name: ", self.name,  ", Salary: ", self.salary)

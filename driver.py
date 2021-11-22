import employee
import pet

def main():
    emp1 = employee.Employee("Zara", 2000)
    emp2 = employee.Employee("Mandy", 3000)
    emp3 = employee.Employee("Thanos", 2800)
    
    emp1.displayEmployee()
    emp2.displayEmployee()
    emp3.displayEmployee()

    empCount = employee.Employee.empCount
    print('Total number of employees is: ', empCount)

    pet1 = pet.Pet('Kujo', 'dog')
    pet2 = pet.Pet('Frisky', 'cat')
    pet3 = pet.Pet('Chompy', 'shark')

    emp1.fedPet(pet1)
    #emp2.fedPet(pet2)
    emp3.fedPet(pet3)

    pet1.displayPet()
    pet2.displayPet()
    pet3.displayPet()

    petCount = pet.Pet.petCount
    print('Total pets: ', petCount)

main()

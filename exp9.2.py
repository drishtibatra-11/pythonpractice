class Student:
    def __init__(self, name, sap_id, phy, chem, maths):
        self.name = name
        self.sap_id = sap_id
        self.phy = phy
        self.chem = chem
        self.maths = maths

    def display(self):
        print(f"\nName: {self.name}")
        print(f"SAP ID: {self.sap_id}")
        print(f"Marks -> Phy: {self.phy}, Chem: {self.chem}, Maths: {self.maths}")

    def marks_percentage(self):
        total = self.phy + self.chem + self.maths
        percentage = total / 3
        return percentage

    def result(self):
        if self.phy > 40 and self.chem > 40 and self.maths > 40:
            return "Pass"
        else:
            return "Fail"

n = int(input("Enter number of students: "))
students = []

for i in range(n):
    print(f"\nEnter details for Student {i+1}")
    name = input("Enter name: ")
    sap_id = input("Enter SAP ID: ")
    phy = int(input("Physics: "))
    chem = int(input("Chemistry: "))
    maths = int(input("Maths: "))

    students.append(Student(name, sap_id, phy, chem, maths))


total_avg = 0

for s in students:
    s.display()
    perc = s.marks_percentage()
    print("Percentage:", perc)
    print("Result:", s.result())
    total_avg += perc

# Class average
print("\nClass Average Percentage:", total_avg / n)
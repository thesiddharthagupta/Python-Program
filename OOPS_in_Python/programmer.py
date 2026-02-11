class programmer:
    company = "microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("Siddhu", 24000000, 24016 )
print(p.name, p.salary, p.pin, p.company)

r = programmer("Rahul", 24000000, 24016 )
print(r.name, r.salary, r.pin, r.company)
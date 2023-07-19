class nokia:
    company_name="nokia"
    web_site="www.nokia007@gamil.com"

    def address(self):
        print("address: dhubai ,sunny leon street")
class nokia1100(nokia):
    def __init__(self):
        self.name="nokia"
        self.year="1995"
    def product(self):
        print(self.name)
        print(self.year)
        print(self.company_name)
        print(self.web_site)
        super().address()

o=nokia1100()

o.product()
o.address()

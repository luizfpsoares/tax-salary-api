class Salary:
    def __init__(self, grossSalary):
        self.grossSalary = grossSalary
        self.netSalary = 0.0
        self.inssTax = 0.0
        self.irrfTax = 0.0
        self.tax = 0.0

    def irrfCalc(self):
        irrfTax = 0.0
        aliquot1 = 7.5
        aliquot2 = 15.0
        aliquot3 = 22.5
        aliquot4 = 27.5

        base0 = 2259.20
        base1Start = 2259.21
        base1End = 2826.65
        base2Start = 2826.66
        base2End = 3751.05
        base3Start =  3751.06
        base3End =  4664.68
        base4 = 4664.68

        if self.grossSalary >= base1Start:
            if self.grossSalary >= base1End:
                base1 = base1End - base1Start
                base1Tax = (aliquot1 / 100) * base1
                self.irrfTax += base1Tax
            else:
                base1 = self.grossSalary - base1Start
                taxBase1 = (aliquot1 / 100) * base1
                self.irrfTax += taxBase1
        if self.grossSalary >= base2Start:
            if self.grossSalary >= base2End:
                base2 = base2End - base2Start
                taxBase2 = (aliquot2 / 100) * base2
                self.irrfTax += taxBase2
            else:
                base2 = self.grossSalary - base2Start
                taxBase2 = (aliquot2 / 100) * base2
                self.irrfTax += taxBase2

        if self.grossSalary >= base3Start:
            if self.grossSalary >= base3End:
                base3 = base3End - base3Start
                taxBase3 = (aliquot3 / 100) * base3
                self.irrfTax += taxBase3
            else:
                base3 = self.grossSalary - base3Start
                taxBase3 = (aliquot3 / 100) * base3
                self.irrfTax += taxBase3

        if self.grossSalary >= base4:
            base4Result = self.grossSalary - base4
            taxBase4 = (aliquot4 / 100) * base4Result
            self.irrfTax += taxBase4
        
        return self.irrfTax

    def inssCalc(self):
        inssTax = 0.0
        inssAliquot1 = 7.5
        inssAliquot2 = 9.0
        inssAliquot3 = 12.0
        inssAliquot4 = 14.0

        inssBase1 = 1412.00
        inssBase2 = 2666.68
        inssBase3 = 4000.03
        inssBase4 = 7786.02

        if self.grossSalary >= inssBase1:
            self.inssTax = (inssAliquot1 / 100) * self.grossSalary
        elif self.grossSalary >= inssBase2:
            self.inssTax = (inssAliquot2 / 100) * self.grossSalary
        elif self.grossSalary >= inssBase3:
            self.inssTax = (inssAliquot3 / 100) * self.grossSalary
        elif self.grossSalary >= inssBase4:
            self.inssTax = (inssAliquot4 / 100) * self.grossSalary
        
        return self.inssTax

    def netSalaryCalc(self):
        self.tax += self.irrfCalc()
        self.tax += self.inssCalc()
        self.netSalary = self.grossSalary - self.tax

    def toString(self):
        return {
            "salary": f"{self.grossSalary:.2f}",
            "netSalary": f"{self.netSalary:.2f}",
            "inssTax": f"{self.inssTax:.2f}",
            "irrfTax": f"{self.irrfTax:.2f}",
            "tax": f"{self.tax:.2f}"
        }
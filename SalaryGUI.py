"""
Program: salaryGUI.py
Author: Elijah
Chapter 8 practice project
1/24/2024

NOTE: the module breezypythongui.py needs to be in the same directory as this file for the app to run correctly!

GUI-based version of the Salary Calculator app which calculates an employee's weekly earnings.

"""

from breezypythongui import EasyFrame
from tkinter.font import Font

class SalaryCalculator(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title="Salary Calculator 2.0", background="lightblue")
        labelFont = Font(family="Wensley", size=16)

        self.addLabel(
            text="Salary Calculator",
            row=0,
            column=0,
            sticky="NSEW",
            columnspan=2,
            background="lightblue",
            font=Font(family="Impact", size=22)
        )
        self.addLabel(
            text="Hourly Wage:",
            row=1,
            column=0,
            background="lightblue",
            foreground="darkorchid2",
            font=labelFont
        )
        self.wageField = self.addFloatField(value=0.0, row=1, column=1)
        self.addLabel(
            text="No. of Hours Worked:",
            row=2,
            column=0,
            background="lightblue",
            foreground="darkorchid2",
            font=labelFont
        )
        self.hoursField = self.addIntegerField(value=0, row=2, column=1)

        # Bind the hoursField to the press of the Enter key event
        self.hoursField.bind("<Return>", lambda event: self.compute())

        self.button = self.addButton(
            text="Compute",
            row=3,
            column=0,
            columnspan=2,
            command=self.compute
        )
        self.button["background"] = "wheat2"
        self.button["width"] = 15

        self.addLabel(
            text="The employee's salary is: ",
            row=4,
            column=0,
            background="lightblue",
            font=labelFont
        )
        self.outputField = self.addFloatField(
            value=0.0,
            row=4,
            column=1,
            precision=2,
            state="readonly"
        )

    def compute(self):
        wage = self.wageField.getNumber()
        hours = self.hoursField.getNumber()
        salary = wage * hours
        self.outputField.setNumber(salary)


def main():
    SalaryCalculator().mainloop()


if __name__ == '__main__':
    main()

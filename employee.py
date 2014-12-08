__author__ = 'Sean'
from ss import *


class Employee:
    def __init__(self, first=None, last=None, start=None, pay_rate=None, social=None):
        if first is None:
            self.first = input("First Name:")
            self.last = input("Last Name:")
            self.start = input("Date Started (mm/dd/yyyy):")
            self.pay_rate = float(input("Rate of Pay:"))
            self.social = SS()

        else:
            self.first = first
            self.last = last
            self.start = start
            self.pay_rate = pay_rate
            self.social = social

    def __str__(self):
        return self.first + ' ' + self.last + ' ' + 'Started working here on ' + self.start + '.' + '\n'\
        + 'They Make ' + str(self.pay_rate) + ' an hour.' + ' Their social security number is ' + str(self.social)
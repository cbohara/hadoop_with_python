#!/usr/local/bin/python3

from mrjob.job import MRJob
from mrjob.step import MRStep
import csv

columns = ['Name', 'JobTitle', 'AgencyID', 'Agency', 'HireDate', 'AnnualSalary', 'GrossPay']

class salarymax(MRJob):
    def mapper(self, _, line):
        # create array from csv line and then zip the column name to the value and create a dictionary
        row = dict(zip(columns, [x.strip() for x in csv.reader([line]).next()]))
        # generator contains string, (
        yield 'salary', (float(row['AnnualSalary'][1:]), line)

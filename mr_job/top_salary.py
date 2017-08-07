#!/usr/bin/python

from mrjob.job import MRJob
from mrjob.step import MRStep
import csv

columns = ['Name', 'JobTitle', 'AgencyID', 'Agency', 'HireDate', 'AnnualSalary', 'GrossPay']

class salarymax(MRJob):
    def mapper(self, _, line):
        # create array from csv line and then zip the column name to the value and create a dictionary
        row = dict(zip(columns, [x.strip() for x in csv.reader([line]).next()]))

        # key is salary and value is tuple with (salary value, all info in line)
        yield 'salary', (float(row['AnnualSalary'][1:]), line)

        # attempt to generate key-value pair for gross as well
        try:
            yield 'gross', (float(row['GrossPay'][1:]), line)
        # hadoop lets you track counters that are aggregates over a step
        # a counter has a group, a name, and an int value
        # mrjob will print job counters to stdout 
        except ValueError:
            self.increment_counter('warn', 'missing gross', 1)

    def reducer(self, key, values):
        topten = []

        # iterate through the sorted values provided by the mapper and hadoop shuffle
        for pay in values:
            # append all salaries and gross income to the list
            topten.append(pay)
            # then sort
            topten.sort()
            # and get the last 10 values in the list
            topten = topten[-10:]

        for pay in topten:
            # yield 'salary' or 'gross' and associated pay
            yield key, pay

    combiner = reducer


if __name__ == "__main__":
    salarymax.run()


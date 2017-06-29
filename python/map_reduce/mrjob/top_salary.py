#!/usr/local/bin/python3
from mrjob.job import MRJob
from mrjob.step import MRStep
import csv

columns = 'Name,JobTitle,AgencyID,Agency,HireDate,AnnualSalary,Gross Pay'.split(',')


class SalaryMax(MRJob):
    # input - key, value (line number, values in each line in csv)
    # output - ('salary', number) and potentially ('gross', number)
    def mapper(self, _, line):
        # convert each line into a dictionary (column key, line value) 
        row = dict(zip(columns, [x.strip() for x in csv.reader([line]).next()]))
        # yield salary
        yield 'salary', (float(row['AnnualSalary'][1:]), line)
        # yield gross pay
        try:
            yield 'gross', (float(row['GrossPay'][1:]), line)
        except ValueError:
            self.increment_counter('warn', 'missing gross', 1)

    # hadoop shuffle will create 2 key, value pairs
    # ('salary', [list of all salaries])
    # ('gross', [list of all gross pay])

    # input - ('salary', [list of salaries]) and ('gross', [list of gross income])
    # output -
    def reducer(self, key, values):
        topten = []

        # iterate over 'salary' and 'gross' and append all values to topten
        for x in values:
            topten.append(x)
            topten.sort()
            topten = topten[-10:]

        # generator stores (key, top salar/gross pay) for 10 salaries
        for x in topten:
            yield key, x

    # mapper output > combiner function > reducer input
    # combiner minimizines the amount of data shuffled between mapper and reducer
    combiner = reducer


if __name__ == '__main__':
    SalaryMax.run()

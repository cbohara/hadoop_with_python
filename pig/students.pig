--LOAD data from the system into Pig
--if not specified default loading function PigStorage is used
--default delimiter \t

--AS defines schema for data being loaded
--if no schema defined then fields are not named and datatype is bytearray

students = LOAD '/Users/cbohara/code/hadoop_with_python/data/students.csv' USING PigStorage(',') AS (name:chararray, age:int, gpa:float);
DUMP students;

-- FILTER works on tuples or rows of data
-- selects tuples from a relation based on a condition
over_20 = FILTER students BY age >= 20;
DUMP over_20;

-- condition statements include AND OR and NOT
old_and_smart = FILTER students BY (age > 20) AND (gpa > 3.5);
DUMP old_and_smart;

-- FOREACH works on columns of data
-- similar to SQL SELECT statement
no_name = FOREACH students GENERATE age, gpa;
DUMP no_name;

-- GROUP groups together tuples that have the same group key into a relation
same_age = GROUP students BY age;
ILLUSTRATE same_age;

-- can grab specific fields from a bag
same_age_names = FOREACH same_age GENERATE group, students.name;
DUMP same_age_names;

-- STORE alias INTO 'directory' [USING function]
-- if the directory already exists the STORE command will fail
STORE students INTO '/Users/cbohara/code/hadoop_with_python/data/pig_output/' USING PigStorage('|');

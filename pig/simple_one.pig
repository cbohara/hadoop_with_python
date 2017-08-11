REGISTER '/Users/cbohara/code/hadoop_with_python/pig/udf/return_one.py' USING streaming_python AS pyudfs;

students = LOAD '/Users/cbohara/code/hadoop_with_python/data/students.csv' USING PigStorage(',');
silly_example = FOREACH students GENERATE pyudfs.return_one();
DUMP silly_example;

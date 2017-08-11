REGISTER '/Users/cbohara/github/hadoop_with_python/pig/strings.py' USING streaming_python AS string_udf;

records = LOAD '/Users/cbohara/github/hadoop_with_python/data/input.txt';

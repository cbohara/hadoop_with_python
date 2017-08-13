-- when data is read into pig the default data type is bytearray

records = LOAD '/Users/hduser/code/hadoop_with_python/data/input.txt';

-- (chararray)$0 will cast bytearray to chararray
-- (jack be nimble jack be quick)

-- TOKENIZE splits a string of words in a single tuple and outputs a bag of words with each word in a single tuple
-- {(jack), (be), (nimble), (jack), (be), (quick)}

-- FLATTEN substitutes the fields of a tuple in place of the tuple
-- (jack), (be), (nimble), (jack), (be), (quick)

terms = FOREACH records GENERATE FLATTEN(TOKENIZE((chararray)$0)) AS word;
-- dump terms;
/*
(jack)
(be)
(nimble)
(jack)
(be)
(quick)
(jack)
(jumped)
(over)
(the)
(candlestick)
*/

grouped_terms = GROUP terms BY word;
-- dump grouped_terms;
/*
(be,{(be),(be)})
(the,{(the)})
(jack,{(jack),(jack),(jack)})
(over,{(over)})
(quick,{(quick)})
(jumped,{(jumped)})
(nimble,{(nimble)})
(candlestick,{(candlestick)})
*/

word_counts = FOREACH grouped_terms GENERATE COUNT(terms), group;
-- dump word_counts;
/*
(2,be)
(1,the)
(3,jack)
(1,over)
(1,quick)
(1,jumped)
(1,nimble)
(1,candlestick)
*/

-- cannot store into folder that already exists 
-- need to create folder for output
STORE word_counts INTO '/Users/hduser/code/hadoop_with_python/data/pig_output';

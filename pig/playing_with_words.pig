-- before a python UDF can be used in a pig script it must be registered
-- so pig knows where to look when the UDF is called
REGISTER '/Users/cbohara/github/hadoop_with_python/pig/strings.py' USING streaming_python AS string_udf;

records = LOAD '/Users/hduser/github/hadoop_with_python/data/meta.txt';

-- (chararray)$0 will cast bytearray to chararray
-- (jack be nimble jack be quick)

-- TOKENIZE splits a string of words in a single tuple and outputs a bag of words with each word in a single tuple
-- {(jack), (be), (nimble), (jack), (be), (quick)}

-- FLATTEN removes the outer complex data structure for direct access to each word in a tuple
-- (jack), (be), (nimble), (jack), (be), (quick)
terms = FOREACH records GENERATE FLATTEN(TOKENIZE((chararray) $0)) AS word;

-- group similar words
grouped_words = GROUP terms BY word;
-- describe grouped_words;
-- grouped_words: {group: chararray,terms: {(word: chararray)}}
-- dump grouped_words;
/*
(BY,{(BY)})
(as,{(as),(as),(as)})
(in,{(in),(in)})
(of,{(of),(of)})
(and,{(and),(and)})
(the,{(the),(the),(the),(the),(the)})
(DUMP,{(DUMP),(DUMP)})
(each,{(each),(each),(each)})
(term,{(term)})
(word,{(word),(word),(word),(word),(word)})
(Count,{(Count)})
(GROUP,{(GROUP)})
*/

-- generate list of unique words
unique_words = FOREACH grouped_words GENERATE group AS word;
-- describe unique_words;
-- {word: chararray}
-- dump unique_words;
/*
(BY)
(as)
(in)
(of)
(and)
(the)
(DUMP)
(each)
(term)
(word)
(Count)
*/

-- calculate the length for each unique word
word_length = FOREACH unique_words GENERATE word, string_udf.num_chars(word) AS length;
-- dump word_length;
/*
(BY,2)
(as,2)
(in,2)
(of,2)
(and,3)
(the,3)
(DUMP,4)
(each,4)
(term,4)
(word,4)
(Count,5)
(GROUP,5)
*/

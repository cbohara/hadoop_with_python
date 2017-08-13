REGISTER '/Users/hduser/github/hadoop_with_python/pig/movies.py' USING streaming_python AS movies_udf;

records = LOAD '/Users/hduser/github/hadoop_with_python/data/movies.txt' USING PigStorage('|')
    AS (id:int, title:chararray, release_date:chararray);

title_release_date = FOREACH records GENERATE movies_udf.parse_title(title), movies_udf.days_since_release(release_date);
--dump title_release_date;
--describe title_release_date;
--title_release_date: {title: chararray,days_since_release: int}

most_recent = ORDER title_release_date BY days_since_release ASC;
top_ten = LIMIT most_recent 10;
dump top_ten;
/*
(unknown,)
(Apt Pupil,6868)
(Mighty, The,6882)
(City of Angels,7071)
(Big One, The,7078)
(Lost in Space,7078)
(Mercury Rising,7078)
(Spanish Prisoner, The,7078)
(Hana-bi,7085)
(Object of My Affection, The,7085)
*/

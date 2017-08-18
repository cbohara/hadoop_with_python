from pig_util import outputSchema
from datetime import datetime
import re


@outputSchema('title:chararray')
def parse_title(title):
    """
    Return the title without the year
    input: 'Toy Story (1995)'
    output: 'Toy Story'
    """
    return re.sub(r'\s*\(\d{4}\)','',title)


@outputSchema('days_since_release:int')
def days_since_release(date):
    """
    Calculate the number of days since the movie release
    """
    if date is None:
        return None

    today = datetime.today()
    # %d is zero padded day number ex: 01, 02, 31
    # %b is local abrev month name ex: Jan, Feb, Dec
    # %Y is year
    release_date = datetime.strptime(date, '%d-%b-%Y')
    delta = today - release_date
    return delta.days

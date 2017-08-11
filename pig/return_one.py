from pig_util import outputSchema

# UDF = user defined function
# decorator defines alias and datatype for the data being returned by the UDF
@outputSchema('value:int')
def return_one():
    return 1

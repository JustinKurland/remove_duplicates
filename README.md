# drop_duplicates

Function for the removal of duplicate columns from a feature set. The function is impervious to the types of dtype problems that arise in the absence of consistent numeric feature types. There are various functions in the Python-world around that attempt to deal with the removal of identical features, but they generally fall into two buckets. (1) They are very slow, e.g., ```df.T.drop_duplicates(keep='first').T```, or (2) they fail to capture all the repeating features as a result of variable dtypes. The latter means that you will be left with duplicates that you are simply unaware of. 

Can be method chained if used with ```Pandas-Flavor``` making it more flexible for the development of a cleaning operation prior to modelling efforts. 

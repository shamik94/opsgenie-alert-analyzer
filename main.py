import sys
import pandas as pd
from group_by_monitor import group_by_monitor
from group_by_facet import group_by_facet


group_by_user_input = input(" <<<< Enter >>>> \n 0 -> Group by Monitor \n 1 -> Group by Facets \n")

if group_by_user_input == '0':
    group_by_monitor(pd.read_csv(sys.argv[1]))
elif group_by_user_input == '1':
    group_by_facet(pd.read_csv(sys.argv[1]))
else:
    print('Invalid Input')
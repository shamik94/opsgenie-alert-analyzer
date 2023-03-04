import re
from chart import plot_chart


def group_by_facet(df):
    facets = set([])

    for row in df.iterrows():
        alias = row[1]['Alias']
        try:
            row_facets_string = re.search(r'#(.*)', alias).group(1)
            row_facets = row_facets_string.split(",")
            for row_facet in row_facets:
                facets.add(row_facet.split(":")[0])
        except:
            continue

    print("Found the following Facets:")
    print(facets)

    input_facet = input("Which facet do you want to group by? \n")
    facet_map = {}

    for row in df.iterrows():
        alias = row[1]['Alias']
        try:
            row_facets_string = re.search(r'#(.*)', alias).group(1)
            row_facets = row_facets_string.split(",")
            for row_facet in row_facets:
                key = row_facet.split(":")[0]
                value = row_facet.split(":")[1]
                if key == input_facet:
                    facet_map[value] = facet_map.get(value, 0) + 1
        except:
            continue

    plot_chart(facet_map, df.shape[0], 'Grouping by ' + input_facet)

import re
from chart import plot_chart


def group_by_monitor(df):
    monitors_map = {}

    for row in df.iterrows():
        alias = row[1]['Alias']
        try:
            monitor = re.search(r'monitor_id:(.*?)\|', alias).group(1)
            monitors_map[monitor] = monitors_map.get(monitor, 0) + 1
        except:
            continue

    plot_chart(monitors_map, df.shape[0], 'Grouping by Monitors')

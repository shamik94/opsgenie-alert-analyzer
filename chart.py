import matplotlib.pyplot as plt
import seaborn as sns


def plot_chart(data_map, total_alert_count, chart_title):
    # Remove low count monitors and sort them
    for key in list(data_map.keys()):
        if data_map[key] / total_alert_count < 0.01:
            # monitors_map['others'] = monitors_map.get('others', 0) + monitors_map[key]
            del data_map[key]

    data_map = dict(sorted(data_map.items(), key=lambda item: item[1], reverse=True))

    # Data to plot
    labels = []
    sizes = []

    for x, y in data_map.items():
        labels.append(x)
        sizes.append(y)

    # Plot
    plt.pie(sizes, colors=sns.color_palette('Set2'))
    plt.axis('equal')
    plt.title(chart_title)
    labels = [f'{l}, {s}' for l, s in zip(labels, sizes)]
    plt.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=labels)
    plt.show()
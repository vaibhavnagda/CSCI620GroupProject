"""
    file        :   visualize_data.py
    language    :   python3
    version     :   19/10/17/10/2017 1:19 PM, v1.0
    author      :   Vaibhav Nagda
    description :   
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

DIR = 'DATA_TABLES'
files = map(lambda x: os.path.join(DIR, x), os.listdir(DIR))
files = filter(lambda x: 'csv' in x, files)


def piechart_age(data, title):
    labels = data.index.tolist()
    sizes = data.values.tolist()
    new_labels = ['under 18', '18-24', '25-34', '35-50', '50+']
    new_sizes = [0] * 5
    for i in range(len(labels)):
        if labels[i] < 18:
            new_sizes[0] += sizes[i]
        elif labels[i] >= 18 and labels[i] < 24:
            new_sizes[1] += sizes[i]
        elif labels[i] >= 24 and labels[i] < 34:
            new_sizes[2] += sizes[i]
        elif labels[i] >= 34 and labels[i] < 50:
            new_sizes[3] += sizes[i]
        else:
            new_sizes[4] += sizes[i]
    colors = ['yellowgreen', 'lightskyblue', 'lightcoral', 'red', 'orange']
    patches, texts = plt.pie(new_sizes, colors=colors, labels=new_labels, startangle=90)
    plt.legend(patches, new_labels, loc="best")
    plt.axis('equal')
    plt.title(title)
    plt.tight_layout()
    plt.show()


def piechart_country(data, title):
    labels = data.index.tolist()
    sizes = data.values.tolist()
    new_labels = ['US', 'Outside US']
    new_sizes = [0] * 2
    for i in range(len(labels)):
        if labels[i] == 'United States':
            new_sizes[0] += sizes[i]
        else:
            new_sizes[1] += sizes[i]
    colors = ['red', 'orange']
    patches, texts = plt.pie(new_sizes, colors=colors, labels=new_labels, startangle=90)
    plt.legend(patches, new_labels, loc="best")
    plt.axis('equal')
    plt.title(title)
    plt.tight_layout()
    plt.show()


def piechart_state(data, title):
    labels = data.index.tolist()
    sizes = data.values.tolist()
    regions = ['New England', 'Mid-Atlantic', 'East North Central', 'West North Central', 'South Atlantic',
               'East South Central', 'West South Central', 'Mountain', 'Pacific']
    new_sizes = [0] * len(regions)
    for i in range(len(labels)):
        if 'CT' in labels[i] or 'ME' in labels[i] or 'MA' in labels[i] or 'NH' in labels[i] or 'RI' in labels[
            i] or 'VT' in labels[i]:
            new_sizes[0] += sizes[i]
        elif 'NJ' in labels[i] or 'NY' in labels[i] or 'PA' in labels[i]:
            new_sizes[1] += sizes[i]
        elif 'IL' in labels[i] or 'IN' in labels[i] or 'MI' in labels[i] or 'OH' in labels[i] or 'WI' in labels[i]:
            new_sizes[2] += sizes[i]
        elif 'IA' in labels[i] or 'KS' in labels[i] or 'MN' in labels[i] or 'MO' in labels[i] or 'NE' in labels[
            i] or 'SD' in labels[i] or 'ND' in labels[i]:
            new_sizes[3] += sizes[i]
        elif 'DE' in labels[i] or 'FL' in labels[i] or 'GA' in labels[i] or 'MD' in labels[i] or 'NC' in labels[
            i] or 'SC' in labels[i] or 'VA' in labels[i] or 'WA' in labels[i] or 'WV' in labels[i]:
            new_sizes[4] += sizes[i]
        elif 'AL' in labels[i] or 'KY' in labels[i] or 'MS' in labels[i] or 'TN' in labels[i]:
            new_sizes[5] += sizes[i]
        elif 'AR' in labels[i] or 'LA' in labels[i] or 'OK' in labels[i] or 'TX' in labels[i]:
            new_sizes[6] += sizes[i]
        elif 'AZ' in labels[i] or 'CO' in labels[i] or 'ID' in labels[i] or 'MT' in labels[i] or 'NV' in labels[
            i] or 'NM' in labels[i] or 'UT' in labels[i] or 'WY' in labels[i]:
            new_sizes[7] += sizes[i]
        elif 'AK' in labels[i] or 'CA' in labels[i] or 'HI' in labels[i] or 'OR' in labels[i] or 'WA' in labels[i]:
            new_sizes[8] += sizes[i]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red', 'orange', 'pink', 'yellow', 'blue']
    patches, texts = plt.pie(new_sizes, colors=colors, labels=regions, startangle=90)
    plt.legend(patches, regions, loc="best")
    plt.axis('equal')
    plt.title(title)
    plt.tight_layout()
    plt.show()


def piechart(data, title):
    labels = data.index.tolist()
    sizes = data.values.tolist()
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red', 'orange', 'pink']
    patches, texts = plt.pie(sizes, colors=colors, labels=labels, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.title(title)
    plt.tight_layout()
    plt.show()


def getfeatures(file_name, flags):
    data = pd.read_csv(file_name)
    features = {}
    for i in data.columns.values:
        features[i] = data[i].value_counts()

    for i in data.columns.values:
        if 'id' not in i:
            try:
                val = flags[i]
            except:
                val = 0
                pass
            if val == 0:
                piechart(features[i], i)
            elif val == 1 and 'age' in i:
                piechart_age(features[i], i)
            elif val == 1 and 'country' in i:
                piechart_country(features[i], i)
            elif val == 1 and 'state' in i:
                piechart_state(features[i], 'division')


def main():
    complicated_data = ['age', 'gender', 'country', 'state']
    flags = {}
    for i in complicated_data:
        flags[i] = 1
    for f in files:
        if 'Survey' not in f:
            getfeatures(f, flags)
    pass


if __name__ == '__main__':
    main()  # setting the entry point

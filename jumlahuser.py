# import pandas as pd

# # header = ['user_id', 'item_id']
# df=pd.read_csv('tesr.csv',skiprows=3)
# print (df[0].value_counts())
# df = pd.read_csv('tesr.csv', sep=' ', names=header)

# n_users = df.user_id.unique().shape[0]
# n_items = df.item_id.unique().shape[0]
# print 'Number of users = ' + str(n_users) + ' | Number of location = ' + str(n_items)
# print 'Number of location = ' + str(n_items)  

import csv
from collections import defaultdict
from pprint import pprint
import timeit


def method1():
    rows = list(csv.reader(open('DATASET1.csv', 'r'), delimiter=','))
    cols = zip(*rows)
    unik = set(cols[0])


    indexed = defaultdict(list)

    for x in unik:
        i = cols[0].index(x)
        indexed[i] = rows[i]

    return indexed

def method2():
    rows = list(csv.reader(open('DATASET1.csv', 'r'), delimiter=','))
    cols = zip(*rows)
    unik = set(cols[4])


    indexed = defaultdict(list)

    for x in unik:
        i = cols[4].index(x)
        indexed[i] = rows[i]

    return indexed
# def method2():
#     rows = list(csv.reader(open('tesr.csv', 'r'), delimiter=','))
#     cols = zip(*rows)
#     unik = set(cols[0])

#     indexed = defaultdict(list)

#     for x in unik:
#         i = next(index for index,fid in enumerate(cols[0]) if fid == x)
#         indexed[i] = rows[i]

#     return indexed

# def method3():
#     rows = list(csv.reader(open('tesr.csv', 'r'), delimiter=','))
#     cols = zip(*rows)
#     indexes = [cols[0].index(x) for x in set(cols[0])]

#     for index in indexes:
#         yield (index,rows[index])


if __name__ == '__main__':

    results = method1()    
    print 'indexed:'
    pprint(dict(results))
    count=len(results)

    print '-' * 80

    results = method2()    
    print 'indexed:'
    pprint(dict(results))
    cou=len(results)

    print '-' * 80

    print count
    print cou

    # results = dict(method3())
    # print 'indexed:'
    # pprint(results)

    #--- Timeit ---

    # print 'method1:', timeit.timeit('dict(method1())', setup="from __main__ import method1", number=10000)
    # print 'method2:', timeit.timeit('dict(method2())', setup="from __main__ import method2", number=10000)
    # print 'method3:', timeit.timeit('dict(method3())', setup="from __main__ import method3", number=10000)
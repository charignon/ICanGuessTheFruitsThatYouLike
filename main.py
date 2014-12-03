#!/usr/bin/env/python 
# -*- coding: utf-8 -*-
import csv
from random import shuffle

import networkx
from ffnet import ffnet, mlgraph

TEST_SIZE = 10
def read_data():
    with open("fruits.csv","rb") as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
        header = rows[0]
        data = rows[1:]
        shuffle(data)
        return header, data[1:TEST_SIZE], data[TEST_SIZE:]

def main():
    def formatPrediction(u):
        if (u>0.5):
            return 1
        else:
            return 0
    res = []
    for k in range(100):
        header, tests, train = read_data()
        inputLength = len(header) - 2
        # 2 here is the middle layer, you can remove it and try, it does not 
        # seem to have much impact in that very case
        conec = mlgraph( (inputLength,1) )
        net = ffnet(conec)
        train_input = [ u[1:-1] for u in train ]
        target_input  = [ u[-1] for u in train ]
        test_input = [ u[1:-1] for u in tests ]
        test_target  = [ u[-1] for u in tests ]
        net.train_tnc(train_input, target_input, maxfun = 1000)
        # Print the name of the fruits used for test 
        o = net.test(test_input, test_target,iprint=0)#), iprint = 2)
        res.append(float(sum([formatPrediction(u[0]) ^ int(test_target[i]) for i,u in enumerate(o[0])]))/len(test_target))
    print sum(res)/len(res)




if __name__ == '__main__':
    main()

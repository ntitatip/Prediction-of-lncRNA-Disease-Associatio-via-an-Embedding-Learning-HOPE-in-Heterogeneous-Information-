#
# import numpy as np
# import random
# import math
# import os
# import time
# import pandas as pd
#
# import math
# import random
import Tool
import csv
from numpy import *
def ReadMyCsv(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:          # 注意表头
        SaveList.append(row)
    return

def ReadMyCsv2(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:
        for i in range(len(row)):       # 转换数据类型
            row[i] = float(row[i])
        SaveList.append(row)
    return

def StorFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return


# 数据
# 节点
AllNode = []
ReadMyCsv(AllNode, "AllNode.csv")
print('len(AllNode)', len(AllNode))
print('AllNode[0]', AllNode[0])

# ALLEdge中存放的是LD的关系
AllEdge = []
ReadMyCsv(AllEdge, "LDAllLncDisease.csv")
print('len(AllEdge)', len(AllEdge))
print('AllEdge[0]', AllEdge[0])

# 将LD的关系转换策成对应的在ALLNode中的位置
AllEdgeNum = []
counter = 0
while counter < len(AllEdge):

    flag1 = 0
    counter1 = 0
    while counter1 < len(AllNode):
        if AllEdge[counter][0] == AllNode[counter1][0]:
            flag1 = 1
            break
        counter1 = counter1 + 1

    flag2 = 0
    counter2 = 0
    while counter2 < len(AllNode):
        if AllEdge[counter][1] == AllNode[counter2][0]:
            flag2 = 1
            break
        counter2 = counter2 + 1

    if flag1 == 1 and flag2 == 1:
        Name = ''
        pair = []
        pair.append(Name + str(counter1))
        pair.append(Name + str(counter2))
        AllEdgeNum.append(pair)

    print(counter)
    counter = counter + 1

print(len(AllEdgeNum))


StorFile(AllEdgeNum, 'LMSNPLncDiNum.csv')

# 生成AllLncNum，AllMiNum
# 把LD关系表中的LncRNA和Disease的位置信息都找出来，一共有多少个LncRNA和Disease
AllLncNum = Tool.GenerateAllDrug(AllEdgeNum)
AllDiNum = Tool.GenerateAllDisease(AllEdgeNum)


Tool.StorFile(AllLncNum, 'AllLncNum.csv')
Tool.StorFile(AllDiNum, 'AllDiNum.csv')

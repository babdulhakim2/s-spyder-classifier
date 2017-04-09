# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 13:24:34 2017

@author: Abdulhakim Bashir
"""
import random
import pandas as pd
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

dataset = { 'k': [[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7,],[8,6]] }
new_features = [5,7]

#[[plt.scatter(ii[0], ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]
#plt.scatter(new_features[0], new_features[1])
#plt.show()

def k_nearest_neigbors(data, predict, k=3):
    if len(data) >=k:
        warnings.warn('K is Set to value less than total voting groups')
    distances = []
    for group in data:
        for features in data[group]:
            #euclidean_distance = sqrt((features[0]-predict[0])**2 + (features[1]-predict[1])**2)
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distance, group])
            
    votes = [i[1] for i in sorted(distances)[:k]]
    #print(Counter(votes).most_common(1))
    vote_result = Counter(votes).most_common(1)[0][0]
    confidence = Counter(votes).most_common(1)[0][1] /k
    
    print(vote_result,confidence*100,'%')
#    if vote_result==2:
#        vote_class = 'benign'
#    elif vote_result ==4:
#        vote_class = 'malignant'
#    print('The class is ', vote_class)
    return vote_result, confidence

#result = k_nearest_neigbors(dataset, new_features,k=3)
#print(result)
accuracies = []
#for i in range(5):
df = pd.read_csv('../datasets/breast-cancer-wisconsin.data.txt')
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)

full_data = df.astype(float).values.tolist()
random.shuffle(full_data)

#print(full_data)

test_size =0.2
train_set = {2:[], 4:[]}
test_set =  {2:[], 4:[]}

data = [7,4,2,1,4,5,6,1,3]
train_data = full_data[:-int(test_size*len(full_data))]
test_data = full_data[-int(test_size*len(full_data)):]

for i in train_data:
    train_set[i[-1]].append(i[:-1])

for i in test_data:
    test_set[i[-1]].append(i[:-1])

correct = 0
total = 0
#    for group in test_set:
#        for data in test_set[group]:
#            vote, confidence = k_nearest_neigbors(train_set, data, k=5)
#            if group == vote:
#                correct +=1
#    #        else:
#    #            print(confidence)
#            total +=1
#    #print('Accuracy: ', correct/total)
#    accuracies.append(correct/total)
#print(sum(accuracies)/len(accuracies))
[[plt.scatter(ii[0], ii[1], s=100, color='r') for ii in train_set[i]] for i in train_set]
plt.scatter(data[0], data[1])
plt.show()
k_nearest_neigbors(train_set,data, k=4)
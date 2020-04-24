import networkx as nx
import time
import argparse
import csv
import numpy as np
import os
from multiprocessing import Pool as ThreadPool
from functools import partial
import glob
import random
from sklearn.model_selection import KFold
from sklearn.metrics import f1_score, precision_score, accuracy_score, recall_score
from itertools import islice

def parseargs():
    parser = argparse.ArgumentParser(description='Malware Detection with centrality.')
    parser.add_argument('-d', '--dir', help='The path of a dir contains feature_CSV.', required=True)
    parser.add_argument('-o', '--output', help='The path of output.', required=True)
    parser.add_argument('-t', '--type', help='The type of centrality: degree, closeness, harmonic, katz', required=True)

    args = parser.parse_args()
    return args

def feature_extraction(file):
    vectors = []
    labels = []
    with open(file, 'r') as f:
        csv_data = csv.reader(f)
        for line in islice(csv_data, 1, None):
            vector = [float(i) for i in line[1:-1]]
            label = int(float(line[-1]))
            vectors.append(vector)
            labels.append(label)

    return vectors, labels

def degree_centrality_feature(feature_dir):
    feature_csv = feature_dir + 'degree_features.csv'
    vectors, labels = feature_extraction(feature_csv)
    return vectors, labels

def katz_centrality_feature(feature_dir):
    feature_csv = feature_dir + 'katz_features.csv'
    vectors, labels = feature_extraction(feature_csv)
    return vectors, labels

def closeness_centrality_feature(feature_dir):
    feature_csv = feature_dir + 'closeness_features.csv'
    vectors, labels = feature_extraction(feature_csv)
    return vectors, labels

def harmonic_centrality_feature(feature_dir):
    feature_csv = feature_dir + 'harmonic_features.csv'
    vectors, labels = feature_extraction(feature_csv)
    return vectors, labels

def random_features(vectors, labels):
    Vec_Lab = []

    for i in range(len(vectors)):
        vec = vectors[i]
        lab = labels[i]
        vec.append(lab)
        Vec_Lab.append(vec)

    random.shuffle(Vec_Lab)

    return [m[:-1] for m in Vec_Lab], [m[-1] for m in Vec_Lab]

from sklearn.neighbors import KNeighborsClassifier
def knn_1(vectors, labels):
    X = np.array(vectors)
    Y = np.array(labels)

    kf = KFold(n_splits=10)
    i = 0
    F1s = []
    Precisions = []
    Recalls = []
    Accuracys = []
    TPRs = []
    FPRs = []
    TNRs = []
    FNRs = []
    for train_index, test_index in kf.split(X):
        train_X, train_Y = X[train_index], Y[train_index]
        test_X, test_Y = X[test_index], Y[test_index]

        clf = KNeighborsClassifier(n_neighbors=1)
        clf.fit(train_X, train_Y)

        y_pred = clf.predict(test_X)
        f1 = f1_score(y_true=test_Y, y_pred=y_pred)
        precision = precision_score(y_true=test_Y, y_pred=y_pred)
        recall = recall_score(y_true=test_Y, y_pred=y_pred)
        accuracy = accuracy_score(y_true=test_Y, y_pred=y_pred)

        # print(f1)
        TP = np.sum(np.multiply(test_Y, y_pred))
        FP = np.sum(np.logical_and(np.equal(test_Y, 0), np.equal(y_pred, 1)))
        FN = np.sum(np.logical_and(np.equal(test_Y, 1), np.equal(y_pred, 0)))
        TN = np.sum(np.logical_and(np.equal(test_Y, 0), np.equal(y_pred, 0)))

        TPR = TP / (TP + FN)
        FPR = FP / (FP + TN)
        TNR = TN / (TN + FP)
        FNR = FN / (TP + FN)

        F1s.append(f1)
        Precisions.append(precision)
        Recalls.append(recall)
        Accuracys.append(accuracy)
        TPRs.append(TPR)
        FPRs.append(FPR)
        TNRs.append(TNR)
        FNRs.append(FNR)

    print(F1s, FPRs)
    return [np.mean(F1s), np.mean(Precisions), np.mean(Recalls), np.mean(Accuracys), np.mean(TPRs), np.mean(FPRs),
            np.mean(TNRs), np.mean(FNRs)]

def knn_3(vectors, labels):
    X = np.array(vectors)
    Y = np.array(labels)

    kf = KFold(n_splits=10)
    i = 0
    F1s = []
    Precisions = []
    Recalls = []
    Accuracys = []
    TPRs = []
    FPRs = []
    TNRs = []
    FNRs = []
    for train_index, test_index in kf.split(X):
        train_X, train_Y = X[train_index], Y[train_index]
        test_X, test_Y = X[test_index], Y[test_index]

        clf = KNeighborsClassifier(n_neighbors=3)
        clf.fit(train_X, train_Y)

        y_pred = clf.predict(test_X)
        f1 = f1_score(y_true=test_Y, y_pred=y_pred)
        precision = precision_score(y_true=test_Y, y_pred=y_pred)
        recall = recall_score(y_true=test_Y, y_pred=y_pred)
        accuracy = accuracy_score(y_true=test_Y, y_pred=y_pred)

        # print(f1)
        TP = np.sum(np.multiply(test_Y, y_pred))
        FP = np.sum(np.logical_and(np.equal(test_Y, 0), np.equal(y_pred, 1)))
        FN = np.sum(np.logical_and(np.equal(test_Y, 1), np.equal(y_pred, 0)))
        TN = np.sum(np.logical_and(np.equal(test_Y, 0), np.equal(y_pred, 0)))

        TPR = TP / (TP + FN)
        FPR = FP / (FP + TN)
        TNR = TN / (TN + FP)
        FNR = FN / (TP + FN)

        F1s.append(f1)
        Precisions.append(precision)
        Recalls.append(recall)
        Accuracys.append(accuracy)
        TPRs.append(TPR)
        FPRs.append(FPR)
        TNRs.append(TNR)
        FNRs.append(FNR)

    print(F1s, FPRs)
    return [np.mean(F1s), np.mean(Precisions), np.mean(Recalls), np.mean(Accuracys), np.mean(TPRs), np.mean(FPRs),
            np.mean(TNRs), np.mean(FNRs)]

from sklearn.ensemble import RandomForestClassifier
def randomforest(vectors, labels):
    X = np.array(vectors)
    Y = np.array(labels)

    kf = KFold(n_splits=10)
    i = 0
    F1s = []
    Precisions = []
    Recalls = []
    Accuracys = []
    TPRs = []
    FPRs = []
    TNRs = []
    FNRs = []
    for train_index, test_index in kf.split(X):
        train_X, train_Y = X[train_index], Y[train_index]
        test_X, test_Y = X[test_index], Y[test_index]

        clf = RandomForestClassifier(max_depth=8, random_state=0)
        clf.fit(train_X, train_Y)

        y_pred = clf.predict(test_X)
        f1 = f1_score(y_true=test_Y, y_pred=y_pred)
        precision = precision_score(y_true=test_Y, y_pred=y_pred)
        recall = recall_score(y_true=test_Y, y_pred=y_pred)
        accuracy = accuracy_score(y_true=test_Y, y_pred=y_pred)

        # print(f1)
        TP = np.sum(np.multiply(test_Y, y_pred))
        FP = np.sum(np.logical_and(np.equal(test_Y, 0), np.equal(y_pred, 1)))
        FN = np.sum(np.logical_and(np.equal(test_Y, 1), np.equal(y_pred, 0)))
        TN = np.sum(np.logical_and(np.equal(test_Y, 0), np.equal(y_pred, 0)))

        TPR = TP / (TP + FN)
        FPR = FP / (FP + TN)
        TNR = TN / (TN + FP)
        FNR = FN / (TP + FN)
        # print(FPR)

        F1s.append(f1)
        Precisions.append(precision)
        Recalls.append(recall)
        Accuracys.append(accuracy)
        TPRs.append(TPR)
        FPRs.append(FPR)
        TNRs.append(TNR)
        FNRs.append(FNR)

    print(F1s, FPRs)
    return [np.mean(F1s), np.mean(Precisions), np.mean(Recalls), np.mean(Accuracys), np.mean(TPRs), np.mean(FPRs),
            np.mean(TNRs), np.mean(FNRs)]

def classification(vectors, labels):
    Vectors, Labels = random_features(vectors, labels)

    csv_data = [[] for i in range(4)]
    csv_data[0] = ['ML_Algorithm', 'F1', 'Precision', 'Recall', 'Accuracy', 'TPR', 'FPR', 'TNR', 'FNR']
    csv_data[1].append('KNN-1')
    csv_data[1].extend(knn_1(Vectors, Labels))
    csv_data[2].append('KNN-3')
    csv_data[2].extend(knn_3(Vectors, Labels))
    csv_data[3].append('Random Forest')
    csv_data[3].extend(randomforest(Vectors, Labels))

    return csv_data


def main():
    args = parseargs()
    feature_dir = args.dir
    out_put = args.output
    type = args.type

    if feature_dir[-1] == '/':
        feature_dir = feature_dir
    else:
        feature_dir += '/'

    if out_put[-1] == '/':
        out_put = out_put
    else:
        out_put += '/'

    if type == 'degree':
        degree_vectors, degree_labels = degree_centrality_feature(feature_dir)
        degree_csv_data = classification(degree_vectors, degree_labels)
        degree_reults = out_put + 'degree_result.csv'
        with open(degree_reults, 'w', newline='') as f_degree:
            csvfile = csv.writer(f_degree)
            csvfile.writerows(degree_csv_data)
    elif type == 'harmonic':
        harmonic_vectors, harmonic_labels = harmonic_centrality_feature(feature_dir)
        harmonic_csv_data = classification(harmonic_vectors, harmonic_labels)
        harmonic_reults = out_put + 'harmonic_result.csv'
        with open(harmonic_reults, 'w', newline='') as f_harmonic:
            csvfile = csv.writer(f_harmonic)
            csvfile.writerows(harmonic_csv_data)
    elif type == 'katz':
        katz_vectors, katz_labels = katz_centrality_feature(feature_dir)
        katz_csv_data = classification(katz_vectors, katz_labels)
        katz_reults = out_put + 'katz_result.csv'
        with open(katz_reults, 'w', newline='') as f_katz:
            csvfile = csv.writer(f_katz)
            csvfile.writerows(katz_csv_data)
    elif type == 'closeness':
        closeness_vectors, closeness_labels = closeness_centrality_feature(feature_dir)
        closeness_csv_data = classification(closeness_vectors, closeness_labels)
        closeness_reults = out_put + 'closeness_result.csv'
        with open(closeness_reults, 'w', newline='') as f_closeness:
            csvfile = csv.writer(f_closeness)
            csvfile.writerows(closeness_csv_data)
    else:
        print('Error Centrality Type!')


if __name__ == '__main__':
    main()
import networkx as nx
import time
import argparse
import csv
from multiprocessing import Pool as ThreadPool
from functools import partial
import glob

def parseargs():
    parser = argparse.ArgumentParser(description='Malware Detection with centrality.')
    parser.add_argument('-d', '--dir', help='The path of a dir contains benign and malware.', required=True, type=str)
    parser.add_argument('-o', '--output', help='The dir_path of output', required=True, type=str)
    parser.add_argument('-c', '--centrality', help='The type of centrality: degree, katz, closeness, harmonic', required=True, type=str)
    args = parser.parse_args()
    return args

def obtain_sensitive_apis(file):
    sensitive_apis = []
    with open(file, 'r') as f:
        for line in f.readlines():
            if line.strip() == '':
                continue
            else:
                sensitive_apis.append(line.strip())
    return sensitive_apis

def callgraph_extraction(file):
    CG = nx.read_gexf(file)
    return CG

def degree_centrality_feature(file, sensitive_apis):
    sha256 = file.split('/')[-1].split('.')[0]
    CG = callgraph_extraction(file)
    node_centrality = nx.degree_centrality(CG)
    
    vector = []
    for api in sensitive_apis:
        if api in node_centrality.keys():
            vector.append(node_centrality[api])
        else:
            vector.append(0)

    return (sha256, vector)

def katz_centrality_feature(file, sensitive_apis):
    sha256 = file.split('/')[-1].split('.')[0]
    CG = callgraph_extraction(file)
    node_centrality = nx.katz_centrality(CG)

    vector = []
    for api in sensitive_apis:
        if api in node_centrality.keys():
            vector.append(node_centrality[api])
        else:
            vector.append(0)

    return (sha256, vector)

def closeness_centrality_feature(file, sensitive_apis):
    sha256 = file.split('/')[-1].split('.')[0]
    CG = callgraph_extraction(file)
    node_centrality = nx.closeness_centrality(CG)
    
    vector = []
    for api in sensitive_apis:
        if api in node_centrality.keys():
            vector.append(node_centrality[api])
        else:
            vector.append(0)

    return (sha256, vector)

def harmonic_centrality_feature(file, sensitive_apis):
    sha256 = file.split('/')[-1].split('.')[0]
    CG = callgraph_extraction(file)
    node_centrality = nx.harmonic_centrality(CG)
    
    vector = []
    for api in sensitive_apis:
        if api in node_centrality.keys():
            vector.append(node_centrality[api])
        else:
            vector.append(0)

    return (sha256, vector)

def obtain_dataset(dataset_path, centrality_type, sensitive_apis):
    Vectors = []
    Labels = []

    if dataset_path[-1] == '/':
        apps_b = glob.glob(dataset_path + 'benign/*.gexf')
        apps_m = glob.glob(dataset_path + 'malware/*.gexf')
    else:
        apps_b = glob.glob(dataset_path + '/benign/*.gexf')
        apps_m = glob.glob(dataset_path + '/malware/*.gexf')

    pool_b = ThreadPool(15)
    pool_m = ThreadPool(15)
    if centrality_type == 'degree':
        vector_b = pool_b.map(partial(degree_centrality_feature, sensitive_apis=sensitive_apis), apps_b)
        vector_m = pool_m.map(partial(degree_centrality_feature, sensitive_apis=sensitive_apis), apps_m)
    elif centrality_type == 'katz':
        vector_b = pool_b.map(partial(katz_centrality_feature, sensitive_apis=sensitive_apis), apps_b)
        vector_m = pool_m.map(partial(katz_centrality_feature, sensitive_apis=sensitive_apis), apps_m)
    elif centrality_type == 'closeness':
        vector_b = pool_b.map(partial(closeness_centrality_feature, sensitive_apis=sensitive_apis), apps_b)
        vector_m = pool_m.map(partial(closeness_centrality_feature, sensitive_apis=sensitive_apis), apps_m)
    elif centrality_type == 'harmonic':
        vector_b = pool_b.map(partial(harmonic_centrality_feature, sensitive_apis=sensitive_apis), apps_b)
        vector_m = pool_m.map(partial(harmonic_centrality_feature, sensitive_apis=sensitive_apis), apps_m)
    else:
        print('Error Centrality Type!')

    Vectors.extend(vector_b)
    Labels.extend([0 for i in range(len(vector_b))])

    Vectors.extend(vector_m)
    Labels.extend([1 for i in range(len(vector_m))])

    return Vectors, Labels

def main():
    sensitive_apis_path = 'sensitive_apis.txt'
    sensitive_apis = obtain_sensitive_apis(sensitive_apis_path)

    args = parseargs()
    dataset_path = args.dir
    cetrality_type = args.centrality

    Vectors, Labels = obtain_dataset(dataset_path, cetrality_type, sensitive_apis)
    feature_csv = [[] for i in range(len(Labels)+1)]
    feature_csv[0].append('SHA256')
    feature_csv[0].extend(sensitive_apis)
    feature_csv[0].append('Label')

    for i in range(len(Labels)):
        (sha256, vector) = Vectors[i]
        feature_csv[i+1].append(sha256)
        feature_csv[i+1].extend(vector)
        feature_csv[i+1].append(Labels[i])

    if args.output[-1] == '/':
        csv_path = args.output + cetrality_type + '_features.csv'
    else:
        csv_path = args.output + '/' + cetrality_type + '_features.csv'

    with open(csv_path, 'w', newline='') as f:
        csvfile = csv.writer(f)
        csvfile.writerows(feature_csv)

if __name__ == '__main__':
    main()
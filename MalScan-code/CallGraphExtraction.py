import networkx as nx
from collections import defaultdict
import time
import os
from androguard.misc import AnalyzeAPK
#import matplotlib.pyplot as plt
import argparse
import glob
from multiprocessing import Pool as ThreadPool
from functools import partial

def parse_args():
    parser = argparse.ArgumentParser(description='To obtain the call graphs.')
    parser.add_argument('-f', '--file', help='The path of an APK file or a dir contains some APK files', required=True, type=str)
    parser.add_argument('-o', '--output', help='The path of output.', required=True, type=str)
    args = parser.parse_args()
    return args

def get_call_graph(dx):
    t0 = time.time()
    #CG = nx.MultiDiGraph()
    CG = nx.DiGraph()
    nodes = dx.find_methods('.*', '.*', '.*', '.*')
    for m in nodes:
        API = m.get_method()
        class_name = API.get_class_name()
        method_name = API.get_name()
        descriptor = API.get_descriptor()
        api_call = class_name + '->' + method_name + descriptor
        #api_call = class_name + '->' + method_name

        if len(m.get_xref_to()) == 0:
            continue
        CG.add_node(api_call)

        for other_class, callee, offset in m.get_xref_to():
            _callee = callee.get_class_name() + '->' + callee.get_name() + callee.get_descriptor()
            #_callee = callee.get_class_name() + '->' + callee.get_name()
            CG.add_node(_callee)
            if not CG.has_edge(API, callee):
                CG.add_edge(api_call, _callee)

    return CG

import zipfile
def apk_to_callgraph(app_path, exist_files, out_path):
    apk_name = app_path.split('/')[-1].split('.apk')[0]

    if apk_name in exist_files:
        return None
    elif not zipfile.is_zipfile(app_path):
        return None
    else:
        try:
            a, d, dx = AnalyzeAPK(app_path)
            call_graph = get_call_graph(dx=dx)
            cg = call_graph
            print(apk_name)
            
            file_cg = out_path + '/' + apk_name + '.gexf'
            nx.write_gexf(cg, file_cg)
            
        except:
            return None

def main():
    tic = time.time()
    args = parse_args()

    exist_files = os.listdir(args.output)
    exist_files = [f.split('.gexf')[0] for f in exist_files]
    if args.output[-1] == '/':
        out_path = args.output[:-1]
    else:
        out_path = args.output

    if os.path.isdir(args.file):
        if args.file[-1] == '/':
            path = args.file + '*.apk'
        else:
            path = args.file + '/*.apk'

        apks = glob.glob(path)
        pool = ThreadPool(15)
        pool.map(partial(apk_to_callgraph, exist_files=exist_files, out_path=out_path), apks)
    else:
        apk_to_callgraph(args.file, exist_files, out_path)

    print(time.time()-tic)

if __name__ == '__main__':
    main()


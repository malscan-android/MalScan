# MalScan
MalScan is an efficient Android malware detection system based on centrality analysis of sensitive API calls. Instead of traditional heavyweight static analysis, we treat function call graphs of apps as social networks and perform social-network-based centrality analysis to represent the semantic features of the graphs.
MalScan’s operation goes through three main phases: Static Analysis, Centrality Analysis and Classification. 
1) Static Analysis: This phase aims at extracting the function call graph of an app based on static analysis, where each node is a function that can be an API call or a user-defined function.
2) Centrality Analysis: After obtaining the call graph of an app, we then compute the centrality of sensitive API calls within the graph. The output of this phase is the feature vector.
3) Classification: In the final phase, given the feature vector, we can accurately and efficiently classify the app as either benign or malicious by using a machining learning classifier.

# Dataset
All the datasets are derived from a growing collection, AndroZoo (https://androzoo.uni.lu/), which currently contains over nine million different APKs, each of which has been (or will soon be) analysed by several different AntiVirus products in VirusTotal (https://www.virustotal.com/) to know which applications are detected as malware. The datasets used in our experiments can be obtained from AndroZoo through the given sha256 (https://androzoo.uni.lu/api_doc).

# Publication
MalScan: Fast Market-Wide Mobile Malware Scanning by Social-Network Centrality Analysis. Yueming Wu, XiaoDi Li, Deqing Zou, Wei Yang, Xin Zhang, Hai Jin. (ASE 2019)

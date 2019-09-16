# MalScan
MalScan is an efficient Android malware detetion system based on social-network-centrality analysis of sensitive API calls. Instead of traditional heavyweight static analysis, we treat function call graphs of apps as social networks and perform social-network-based centrality analysis to represent the semantic features of the graphs.
MalScan’s operation goes through three main phases: Static Analysis, Centrality Analysis and Classification. 
1) Static Analysis: This phase aims at extracting the function call graph of an app based on static analysis, where each node is a function that can be an API call or a user-defined function.
2) Centrality Analysis: After obtaining the call graph of an app, we then compute the centrality of sensitive API calls within the graph. The output of this phase is the feature vector.
3) Classification: In the final phase, given the feature vector, we can accurately and efficiently classify the app as either benign or malicious by using a machining learning classifier.


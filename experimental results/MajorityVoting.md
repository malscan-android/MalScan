Experimental Setup
====

A potential application of CenDroid is to use majority voting to decide among the four metrics. For example, 
an app we consider malicious when it’s detected by three or more of the four centrality metrics. For testing the
feasibility of majority voting, we conduct an experiment on 2011 dataset (1920 benign samples and 1916 malware samples), 
we first train an 1nn machine learning model by randomly selecting 1500 benign apps and 1500 
malicious apps from 2011 dataset, and then test on the remainder which contains 420 benign samples and 416 malware samples. 

Experimental Result
===
We select four centrality metrics, namlely degree centrality, closeness centrality, harmonic centrality and katz centrality. 
We conduct another four experiments according to the selection of the threshold to flag an app as malicious which are 
one (Vote_1), two (Vote_2), three (Vote_3) and all (Vote_4). When we select three as the threshold to flag an app
as malicious, the f1 is 97.72% which is higher than the other four individual experiments.


|           | F1     | Accuracy | TPR    |
| --------- | ------ | -------- | ------ |
| degree    | 0.9642 | 0.9641   | 0.9712 |
| closeness | 0.9623 | 0.9617   | 0.9808 |
| harmonic  | 0.9726 | 0.9725   | 0.9808 |
| katz      | 0.9575 | 0.9569   | 0.9760 |
| Vote_1    | 0.9397 | 0.9366   | 0.9928 |
| Vote_2    | 0.9716 | 0.9713   | 0.9856 |
| Vote_3    | 0.9772 | 0.9773   | 0.9784 |
| Vote_4    | 0.9694 | 0.9701   | 0.9519 |

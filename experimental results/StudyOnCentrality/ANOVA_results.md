# Preliminary Study on Degree Centrality
In Fig. 1 in the paper, we show the degree centrality distributions of the following four sensitive API calls which are the most frequently-invoked sensitive API calls in our randomly selected 1000 apps (500 benign apps and 500 malicious apps):

**API1: Landroid/net/ConnectivityManager;->getActiveNetworkInfo()Landroid/net/NetworkInfo;**

| ANOVA:   Single factor                |          |          |          |          |          |          |
| ------------------------------------- | -------- | -------- | -------- | -------- | -------- | -------- |
| SUMMARY                               |          |          |          |          |          |          |
| Groups                                | Count    | Sum      | Average  | Variance |          |          |
| Degree centrality in Benign   apps    | 500      | 0.237218 | 0.000474 | 1.08E-07 |          |          |
| Degree centrality in   malicious apps | 500      | 0.751806 | 0.001504 | 6.51E-07 |          |          |
| ANOVA                                 |          |          |          |          |          |          |
| Source of variance                    | SS       | df       | MS       | F        | P-value  | F crit   |
| Between groups                        | 0.000265 | 1        | 0.000265 | 697.6574 | 5.3E-117 | 3.850793 |
| Within groups                         | 0.000379 | 998      | 3.8E-07  |          |          |          |
| Total                                 | 0.000644 | 999      |          |          |          |          |

**API2: Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;)V**
  
| ANOVA:   Single factor                |          |          |          |          |          |          |
| ------------------------------------- | -------- | -------- | -------- | -------- | -------- | -------- |
| SUMMARY                               |          |          |          |          |          |          |
| Groups                                | Count    | Sum      | Average  | Variance |          |          |
| Degree centrality in Benign   apps    | 500      | 0.253237 | 0.000506 | 1.61E-07 |          |          |
| Degree centrality in   malicious apps | 500      | 0.911262 | 0.001823 | 1.68E-06 |          |          |
| ANOVA                                 |          |          |          |          |          |          |
| Source of variance                    | SS       | df       | MS       | F        | P-value  | F crit   |
| Between groups                        | 0.000433 | 1        | 0.000433 | 469.5736 | 1.21E-85 | 3.850793 |
| Within groups                         | 0.00092  | 998      | 9.22E-07 |          |          |          |
| Total                                 | 0.001353 | 999      |          |          |          |          |
  
**API3: Landroid/widget/TextView;-><init>(Landroid/content/Context;)V**
  
| ANOVA:   Single factor                |          |          |          |          |          |          |
| ------------------------------------- | -------- | -------- | -------- | -------- | -------- | -------- |
| SUMMARY                               |          |          |          |          |          |          |
| Groups                                | Count    | Sum      | Average  | Variance |          |          |
| Degree centrality in Benign   apps    | 500      | 0.214532 | 0.000429 | 1.08E-07 |          |          |
| Degree centrality in   malicious apps | 500      | 0.660615 | 0.001321 | 6.8E-07  |          |          |
| ANOVA                                 |          |          |          |          |          |          |
| Source of variance                    | SS       | df       | MS       | F        | P-value  | F crit   |
| Between groups                        | 0.000199 | 1        | 0.000199 | 504.9704 | 8.06E-91 | 3.850793 |
| Within groups                         | 0.000393 | 998      | 3.94E-07 |          |          |          |
| Total                                 | 0.000592 | 999      |          |          |          |          |
  
**API4: Landroid/app/Activity;->finish()V**

| ANOVA:   Single factor                |          |          |          |          |          |          |
| ------------------------------------- | -------- | -------- | -------- | -------- | -------- | -------- |
| SUMMARY                               |          |          |          |          |          |          |
| Groups                                | Count    | Sum      | Average  | Variance |          |          |
| Degree centrality in Benign   apps    | 500      | 0.174655 | 0.000349 | 7.35E-08 |          |          |
| Degree centrality in   malicious apps | 500      | 0.283085 | 0.000566 | 9.56E-08 |          |          |
| ANOVA                                 |          |          |          |          |          |          |
| Source of variance                    | SS       | df       | MS       | F        | P-value  | F crit   |
| Between groups                        | 1.18E-05 | 1        | 1.18E-05 | 139.0211 | 3.92E-30 | 3.850793 |
| Within groups                         | 8.44E-05 | 998      | 8.46E-08 |          |          |          |
| Total                                 | 9.62E-05 | 999      |          |          |          |          |


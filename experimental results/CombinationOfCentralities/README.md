# Combination of centrality measures

We also propose the combination of different
centralities on detecting Android malware. An app we consider as malware
when it's reported to be malicious by one or more of the six
centrality experiments. For testing the feasibility of majority-voting,
we conduct an experiment. We leverage a trained model by using 2011 dataset
and test on datasets from 2012 to 2014 respectively. And the
thresholds to flag an app as malicious in our experiment are
one (Vote_1), two (Vote_2), three (Vote_3), four (Vote_4). five
(Vote_5) and all (Vote_6).

<table border=0 cellpadding=0 cellspacing=0 width=770 style='border-collapse:
 collapse;table-layout:fixed;width:578pt'>
 <col width=122 style='mso-width-source:userset;mso-width-alt:3904;width:92pt'>
 <col width=72 span=9 style='width:54pt'>
 <tr class=xl67 height=18 style='height:13.5pt'>
  <td rowspan=2 height=36 class=xl65 width=122 style='height:27.0pt;width:92pt'>Testing
  Year</td>
  <td colspan=3 class=xl66 width=216 style='width:162pt'>2012</td>
  <td colspan=3 class=xl66 width=216 style='width:162pt'>2013</td>
  <td colspan=3 class=xl66 width=216 style='width:162pt'>2014</td>
 </tr>
 <tr class=xl67 height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>F1</td>
  <td class=xl66>A</td>
  <td class=xl66>TPR</td>
  <td class=xl66>F1</td>
  <td class=xl66>A</td>
  <td class=xl66>TPR</td>
  <td class=xl66>F1</td>
  <td class=xl66>A</td>
  <td class=xl66>TPR</td>
 </tr>
 <tr class=xl67 height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Degree</td>
  <td class=xl68>85.23 </td>
  <td class=xl68>85.60 </td>
  <td class=xl68>83.10 </td>
  <td class=xl68>83.07 </td>
  <td class=xl68>84.21 </td>
  <td class=xl68>75.45 </td>
  <td class=xl68>74.37 </td>
  <td class=xl68>78.28 </td>
  <td class=xl68>60.54 </td>
 </tr>
 <tr class=xl67 height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Closeness</td>
  <td class=xl68>82.93 </td>
  <td class=xl68>84.13 </td>
  <td class=xl68>74.70 </td>
  <td class=xl68>73.83 </td>
  <td class=xl68>77.05 </td>
  <td class=xl68>63.05 </td>
  <td class=xl68>68.96 </td>
  <td class=xl68>74.42 </td>
  <td class=xl68>54.59 </td>
 </tr>
 <tr class=xl67 height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Harmonic</td>
  <td class=xl68>89.73 </td>
  <td class=xl68>89.45 </td>
  <td class=xl68>89.35 </td>
  <td class=xl68>86.32 </td>
  <td class=xl68>86.47 </td>
  <td class=xl68>83.10 </td>
  <td class=xl68>76.54 </td>
  <td class=xl68>78.99 </td>
  <td class=xl68>65.84 </td>
 </tr>
 <tr class=xl67 height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Katz</td>
  <td class=xl68>86.25 </td>
  <td class=xl68>85.99 </td>
  <td class=xl68>85.15 </td>
  <td class=xl68>79.43 </td>
  <td class=xl68>80.24 </td>
  <td class=xl68>74.35 </td>
  <td class=xl68>76.66 </td>
  <td class=xl68>79.31 </td>
  <td class=xl68>65.29 </td>
 </tr>
 <tr class=xl67 height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Average</td>
  <td class=xl68>89.80 </td>
  <td class=xl68>89.52 </td>
  <td class=xl68>89.35 </td>
  <td class=xl68>86.70 </td>
  <td class=xl68>86.94 </td>
  <td class=xl68>82.95 </td>
  <td class=xl68>76.77 </td>
  <td class=xl68>79.31 </td>
  <td class=xl68>65.69 </td>
 </tr>
 <tr class=xl67 height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Concatenate</td>
  <td class=xl68>89.83 </td>
  <td class=xl68>89.55 </td>
  <td class=xl68>89.40 </td>
  <td class=xl68>86.88 </td>
  <td class=xl68>87.11 </td>
  <td class=xl68>83.10 </td>
  <td class=xl68>76.93 </td>
  <td class=xl68>79.41 </td>
  <td class=xl68>65.94 </td>
 </tr>
 <tr class=xl67 height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Vote_1</td>
  <td class=xl68>88.47 </td>
  <td class=xl68>86.97 </td>
  <td class=xl68>96.90 </td>
  <td class=xl68>85.20 </td>
  <td class=xl68>83.62 </td>
  <td class=xl68>92.00 </td>
  <td class=xl68>82.31 </td>
  <td class=xl68>81.99 </td>
  <td class=xl68>81.99 </td>
 </tr>
 <tr class=xl67 height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Vote_2</td>
  <td class=xl68>91.44 </td>
  <td class=xl68>91.05 </td>
  <td class=xl68>92.65 </td>
  <td class=xl68>88.80 </td>
  <td class=xl68>88.81 </td>
  <td class=xl68>86.45 </td>
  <td class=xl68>84.07 </td>
  <td class=xl68>85.22 </td>
  <td class=xl68>74.97 </td>
 </tr>
 <tr class=xl67 height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Vote_3</td>
  <td class=xl68>90.48 </td>
  <td class=xl68>90.40 </td>
  <td class=xl68>90.20 </td>
  <td class=xl68>87.30 </td>
  <td class=xl68>87.40 </td>
  <td class=xl68>84.40 </td>
  <td class=xl68>76.82 </td>
  <td class=xl68>79.23 </td>
  <td class=xl68>66.15 </td>
 </tr>
 <tr class=xl67 height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Vote_4</td>
  <td class=xl68>89.32 </td>
  <td class=xl68>89.42 </td>
  <td class=xl68>85.75 </td>
  <td class=xl68>81.98 </td>
  <td class=xl68>84.09 </td>
  <td class=xl68>72.80 </td>
  <td class=xl68>76.79 </td>
  <td class=xl68>79.81 </td>
  <td class=xl68>64.18 </td>
 </tr>
 <tr class=xl67 height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Vote_5</td>
  <td class=xl68>80.43 </td>
  <td class=xl68>82.81 </td>
  <td class=xl68>68.85 </td>
  <td class=xl68>73.76 </td>
  <td class=xl68>78.08 </td>
  <td class=xl68>60.00 </td>
  <td class=xl68>67.09 </td>
  <td class=xl68>73.90 </td>
  <td class=xl68>51.11 </td>
 </tr>
 <tr class=xl67 height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Vote_6</td>
  <td class=xl68>68.86 </td>
  <td class=xl68>75.30 </td>
  <td class=xl68>52.90 </td>
  <td class=xl68>66.64 </td>
  <td class=xl68>73.79 </td>
  <td class=xl68>51.00 </td>
  <td class=xl68>51.16 </td>
  <td class=xl68>65.76 </td>
  <td class=xl68>34.46 </td>
 </tr>
 <tr class=xl67 height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>MaMaDroid</td>
  <td class=xl68>81.94 </td>
  <td class=xl68>81.61 </td>
  <td class=xl68>80.18 </td>
  <td class=xl68>78.68 </td>
  <td class=xl68>77.68 </td>
  <td class=xl68>78.79 </td>
  <td class=xl68>71.90 </td>
  <td class=xl68>72.91 </td>
  <td class=xl68>68.33 </td>
 </tr>
 <tr class=xl67 height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Drebin</td>
  <td class=xl68>84.37 </td>
  <td class=xl68>84.59 </td>
  <td class=xl68>71.90 </td>
  <td class=xl68>80.37 </td>
  <td class=xl68>80.93 </td>
  <td class=xl68>63.60 </td>
  <td class=xl68>81.64 </td>
  <td class=xl68>82.09 </td>
  <td class=xl68>65.69 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 style='height:13.5pt'></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
 </tr>
 <![if supportMisalignedColumns]>
 <tr height=0 style='display:none'>
  <td width=122 style='width:92pt'></td>
  <td width=72 style='width:54pt'></td>
  <td width=72 style='width:54pt'></td>
  <td width=72 style='width:54pt'></td>
  <td width=72 style='width:54pt'></td>
  <td width=72 style='width:54pt'></td>
  <td width=72 style='width:54pt'></td>
  <td width=72 style='width:54pt'></td>
  <td width=72 style='width:54pt'></td>
  <td width=72 style='width:54pt'></td>
 </tr>
 <![endif]>
</table>

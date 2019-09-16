# Robustness against Android Evolution

We then evaluate the robustness of MalScan on detecting newer samples by training an old dataset. 

F-measure：
<table border=0 cellpadding=0 cellspacing=0 width=648 style='border-collapse:
 collapse;table-layout:fixed;width:486pt'>
 <col width=72 span=9 style='width:54pt'>
 <tr height=18 style='height:13.5pt'>
  <td colspan=2 rowspan=2 height=36 class=xl65 width=144 style='height:27.0pt;
  width:108pt'>Training</td>
  <td colspan=7 class=xl66 width=504 style='width:378pt'>Testing</td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>2012</td>
  <td class=xl66>2013</td>
  <td class=xl66>2014</td>
  <td class=xl66>2015</td>
  <td class=xl66>2016</td>
  <td class=xl66>2017</td>
  <td class=xl66>2018</td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td rowspan=8 height=144 class=xl65 style='height:108.0pt'>2011</td>
  <td class=xl66>Degree</td>
  <td class=xl67>85.23 </td>
  <td class=xl67>83.07 </td>
  <td class=xl67>74.37 </td>
  <td class=xl67>19.23 </td>
  <td class=xl67>19.11 </td>
  <td class=xl67>28.51 </td>
  <td class=xl67>24.43 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Closeness</td>
  <td class=xl67>82.93 </td>
  <td class=xl67>73.83 </td>
  <td class=xl67>68.96 </td>
  <td class=xl67>26.05 </td>
  <td class=xl67>32.58 </td>
  <td class=xl67>24.87 </td>
  <td class=xl67>27.36 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Harmonic</td>
  <td class=xl67>89.73 </td>
  <td class=xl67>86.32 </td>
  <td class=xl67>76.54 </td>
  <td class=xl67>30.31 </td>
  <td class=xl67>34.87 </td>
  <td class=xl67>21.95 </td>
  <td class=xl67>16.16 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Katz</td>
  <td class=xl67>86.25 </td>
  <td class=xl67>79.43 </td>
  <td class=xl67>76.66 </td>
  <td class=xl67>38.27 </td>
  <td class=xl67>28.03 </td>
  <td class=xl67>13.87 </td>
  <td class=xl67>9.08 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Average</td>
  <td class=xl67>89.80 </td>
  <td class=xl67>86.70 </td>
  <td class=xl67>76.77 </td>
  <td class=xl67>29.64 </td>
  <td class=xl67>34.20 </td>
  <td class=xl67>21.37 </td>
  <td class=xl67>16.09 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Concatenate</td>
  <td class=xl67>89.83 </td>
  <td class=xl67>86.88 </td>
  <td class=xl67>76.93 </td>
  <td class=xl67>30.34 </td>
  <td class=xl67>34.92 </td>
  <td class=xl67>21.98 </td>
  <td class=xl67>16.19 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl68 style='height:13.5pt'>MaMaDroid</td>
  <td class=xl69>81.94 </td>
  <td class=xl69>78.68 </td>
  <td class=xl69>71.90 </td>
  <td class=xl69>54.58 </td>
  <td class=xl69>50.28 </td>
  <td class=xl69>36.58 </td>
  <td class=xl69>17.23 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl68 style='height:13.5pt'>Drebin</td>
  <td class=xl69>84.37 </td>
  <td class=xl69>80.37 </td>
  <td class=xl69>81.64 </td>
  <td class=xl69>38.38 </td>
  <td class=xl69>37.40 </td>
  <td class=xl69>35.33 </td>
  <td class=xl69>35.46 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td rowspan=8 height=144 class=xl65 style='height:108.0pt'>1112</td>
  <td class=xl66>Degree</td>
  <td class=xl67></td>
  <td class=xl67>84.39 </td>
  <td class=xl67>76.66 </td>
  <td class=xl67>65.97 </td>
  <td class=xl67>56.41 </td>
  <td class=xl67>16.47 </td>
  <td class=xl67>13.55 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Closeness</td>
  <td class=xl67></td>
  <td class=xl67>88.67 </td>
  <td class=xl67>80.19 </td>
  <td class=xl67>68.47 </td>
  <td class=xl67>58.09 </td>
  <td class=xl67>30.98 </td>
  <td class=xl67>24.31 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Harmonic</td>
  <td class=xl67></td>
  <td class=xl67>89.67 </td>
  <td class=xl67>79.55 </td>
  <td class=xl67>64.17 </td>
  <td class=xl67>62.19 </td>
  <td class=xl67>43.76 </td>
  <td class=xl67>26.30 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Katz</td>
  <td class=xl67></td>
  <td class=xl67>85.49 </td>
  <td class=xl67>77.23 </td>
  <td class=xl67>72.18 </td>
  <td class=xl67>58.35 </td>
  <td class=xl67>23.70 </td>
  <td class=xl67>17.61 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Average</td>
  <td class=xl67></td>
  <td class=xl67>89.65 </td>
  <td class=xl67>79.55 </td>
  <td class=xl67>70.62 </td>
  <td class=xl67>64.85 </td>
  <td class=xl67>43.21 </td>
  <td class=xl67>26.29 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Concatenate</td>
  <td class=xl67></td>
  <td class=xl67>89.71 </td>
  <td class=xl67>79.65 </td>
  <td class=xl67>61.30 </td>
  <td class=xl67>55.21 </td>
  <td class=xl67>43.21 </td>
  <td class=xl67>26.30 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl68 style='height:13.5pt'>MaMaDroid</td>
  <td class=xl69>　</td>
  <td class=xl69>87.43 </td>
  <td class=xl69>78.39 </td>
  <td class=xl69>65.06 </td>
  <td class=xl69>66.49 </td>
  <td class=xl69>54.32 </td>
  <td class=xl69>40.39 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl68 style='height:13.5pt'>Drebin</td>
  <td class=xl69>　</td>
  <td class=xl69>91.02 </td>
  <td class=xl69>82.65 </td>
  <td class=xl69>77.62 </td>
  <td class=xl69>77.86 </td>
  <td class=xl69>50.94 </td>
  <td class=xl69>40.90 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td rowspan=8 height=144 class=xl65 style='height:108.0pt'>111213</td>
  <td class=xl66>Degree</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>86.94 </td>
  <td class=xl67>53.04 </td>
  <td class=xl67>46.32 </td>
  <td class=xl67>13.49 </td>
  <td class=xl67>13.73 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Closeness</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>86.32 </td>
  <td class=xl67>38.16 </td>
  <td class=xl67>44.29 </td>
  <td class=xl67>29.79 </td>
  <td class=xl67>25.60 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Harmonic</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>90.86 </td>
  <td class=xl67>51.57 </td>
  <td class=xl67>46.23 </td>
  <td class=xl67>41.37 </td>
  <td class=xl67>22.03 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Katz</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>84.95 </td>
  <td class=xl67>48.83 </td>
  <td class=xl67>51.27 </td>
  <td class=xl67>26.29 </td>
  <td class=xl67>22.03 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Average</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>90.86 </td>
  <td class=xl67>40.28 </td>
  <td class=xl67>41.29 </td>
  <td class=xl67>41.37 </td>
  <td class=xl67>22.02 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Concatenate</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>90.94 </td>
  <td class=xl67>38.17 </td>
  <td class=xl67>41.42 </td>
  <td class=xl67>41.37 </td>
  <td class=xl67>22.25 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl68 style='height:13.5pt'>MaMaDroid</td>
  <td class=xl69>　</td>
  <td class=xl69>　</td>
  <td class=xl69>86.04 </td>
  <td class=xl69>71.52 </td>
  <td class=xl69>70.60 </td>
  <td class=xl69>50.97 </td>
  <td class=xl69>22.52 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl68 style='height:13.5pt'>Drebin</td>
  <td class=xl69>　</td>
  <td class=xl69>　</td>
  <td class=xl69>91.16 </td>
  <td class=xl69>61.52 </td>
  <td class=xl69>62.36 </td>
  <td class=xl69>43.68 </td>
  <td class=xl69>38.06 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td rowspan=8 height=144 class=xl65 style='height:108.0pt'>11121314</td>
  <td class=xl66>Degree</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>71.57 </td>
  <td class=xl67>58.53 </td>
  <td class=xl67>41.36 </td>
  <td class=xl67>55.82 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Closeness</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>65.29 </td>
  <td class=xl67>59.73 </td>
  <td class=xl67>34.21 </td>
  <td class=xl67>34.21 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Harmonic</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>74.49 </td>
  <td class=xl67>67.90 </td>
  <td class=xl67>62.45 </td>
  <td class=xl67>60.04 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Katz</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>73.04 </td>
  <td class=xl67>57.11 </td>
  <td class=xl67>25.59 </td>
  <td class=xl67>19.02 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Average</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>76.22 </td>
  <td class=xl67>70.81 </td>
  <td class=xl67>64.38 </td>
  <td class=xl67>61.03 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Concatenate</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>82.32 </td>
  <td class=xl67>78.24 </td>
  <td class=xl67>67.08 </td>
  <td class=xl67>62.74 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl68 style='height:13.5pt'>MaMaDroid</td>
  <td class=xl69>　</td>
  <td class=xl69>　</td>
  <td class=xl69>　</td>
  <td class=xl69>81.77 </td>
  <td class=xl69>74.46 </td>
  <td class=xl69>64.12 </td>
  <td class=xl69>57.20 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl68 style='height:13.5pt'>Drebin</td>
  <td class=xl69>　</td>
  <td class=xl69>　</td>
  <td class=xl69>　</td>
  <td class=xl69>62.15 </td>
  <td class=xl69>62.36 </td>
  <td class=xl69>42.61 </td>
  <td class=xl69>37.79 </td>
 </tr>
 <![if supportMisalignedColumns]>
 <tr height=0 style='display:none'>
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

Accuracy：

<table border=0 cellpadding=0 cellspacing=0 width=648 style='border-collapse:
 collapse;table-layout:fixed;width:486pt'>
 <col width=72 span=9 style='width:54pt'>
 <tr height=18 style='height:13.5pt'>
  <td colspan=2 rowspan=2 height=36 class=xl65 width=144 style='height:27.0pt;
  width:108pt'>Training</td>
  <td colspan=7 class=xl66 width=504 style='width:378pt'>Testing</td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>2012</td>
  <td class=xl66>2013</td>
  <td class=xl66>2014</td>
  <td class=xl66>2015</td>
  <td class=xl66>2016</td>
  <td class=xl66>2017</td>
  <td class=xl66>2018</td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td rowspan=8 height=144 class=xl65 style='height:108.0pt'>2011</td>
  <td class=xl66>Degree</td>
  <td class=xl67>85.60 </td>
  <td class=xl67>84.21 </td>
  <td class=xl67>78.28 </td>
  <td class=xl67>53.75 </td>
  <td class=xl67>55.90 </td>
  <td class=xl67>58.58 </td>
  <td class=xl67>58.01 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Closeness</td>
  <td class=xl67>84.13 </td>
  <td class=xl67>77.05 </td>
  <td class=xl67>74.42 </td>
  <td class=xl67>56.30 </td>
  <td class=xl67>59.92 </td>
  <td class=xl67>56.94 </td>
  <td class=xl67>59.01 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Harmonic</td>
  <td class=xl67>89.45 </td>
  <td class=xl67>86.47 </td>
  <td class=xl67>78.99 </td>
  <td class=xl67>58.05 </td>
  <td class=xl67>61.09 </td>
  <td class=xl67>55.81 </td>
  <td class=xl67>54.59 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Katz</td>
  <td class=xl67>85.99 </td>
  <td class=xl67>80.24 </td>
  <td class=xl67>79.31 </td>
  <td class=xl67>59.70 </td>
  <td class=xl67>57.93 </td>
  <td class=xl67>53.55 </td>
  <td class=xl67>53.18 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Average</td>
  <td class=xl67>89.52 </td>
  <td class=xl67>86.94 </td>
  <td class=xl67>79.31 </td>
  <td class=xl67>57.86 </td>
  <td class=xl67>60.88 </td>
  <td class=xl67>55.68 </td>
  <td class=xl67>54.64 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Concatenate</td>
  <td class=xl67>89.55 </td>
  <td class=xl67>87.11 </td>
  <td class=xl67>79.41 </td>
  <td class=xl67>58.11 </td>
  <td class=xl67>61.16 </td>
  <td class=xl67>55.89 </td>
  <td class=xl67>54.69 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl68 style='height:13.5pt'>MaMaDroid</td>
  <td class=xl69>81.61 </td>
  <td class=xl69>77.68 </td>
  <td class=xl69>72.91 </td>
  <td class=xl69>63.89 </td>
  <td class=xl69>57.52 </td>
  <td class=xl69>49.37 </td>
  <td class=xl69>43.02 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl68 style='height:13.5pt'>Drebin</td>
  <td class=xl69>84.59 </td>
  <td class=xl69>80.93 </td>
  <td class=xl69>82.09 </td>
  <td class=xl69>52.19 </td>
  <td class=xl69>52.31 </td>
  <td class=xl69>51.24 </td>
  <td class=xl69>51.80 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td rowspan=8 height=144 class=xl65 style='height:108.0pt'>1112</td>
  <td class=xl66>Degree</td>
  <td></td>
  <td class=xl67>81.88 </td>
  <td class=xl67>75.47 </td>
  <td class=xl67>70.60 </td>
  <td class=xl67>67.84 </td>
  <td class=xl67>51.21 </td>
  <td class=xl67>51.27 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Closeness</td>
  <td></td>
  <td class=xl67>87.58 </td>
  <td class=xl67>80.07 </td>
  <td class=xl67>73.84 </td>
  <td class=xl67>70.01 </td>
  <td class=xl67>57.10 </td>
  <td class=xl67>55.37 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Harmonic</td>
  <td></td>
  <td class=xl67>88.73 </td>
  <td class=xl67>79.41 </td>
  <td class=xl67>69.51 </td>
  <td class=xl67>67.16 </td>
  <td class=xl67>61.48 </td>
  <td class=xl67>55.19 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Katz</td>
  <td></td>
  <td class=xl67>83.24 </td>
  <td class=xl67>76.44 </td>
  <td class=xl67>73.92 </td>
  <td class=xl67>68.52 </td>
  <td class=xl67>52.77 </td>
  <td class=xl67>51.77 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Average</td>
  <td></td>
  <td class=xl67>88.71 </td>
  <td class=xl67>79.41 </td>
  <td class=xl67>71.34 </td>
  <td class=xl67>67.71 </td>
  <td class=xl67>61.48 </td>
  <td class=xl67>55.17 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Concatenate</td>
  <td></td>
  <td class=xl67>88.78 </td>
  <td class=xl67>79.52 </td>
  <td class=xl67>69.59 </td>
  <td class=xl67>67.18 </td>
  <td class=xl67>61.48 </td>
  <td class=xl67>55.19 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl68 style='height:13.5pt'>MaMaDroid</td>
  <td class=xl69>　</td>
  <td class=xl69>85.82 </td>
  <td class=xl69>73.92 </td>
  <td class=xl69>60.61 </td>
  <td class=xl69>63.98 </td>
  <td class=xl69>52.36 </td>
  <td class=xl69>49.25 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl68 style='height:13.5pt'>Drebin</td>
  <td class=xl69>　</td>
  <td class=xl69>91.07 </td>
  <td class=xl69>82.64 </td>
  <td class=xl69>77.81 </td>
  <td class=xl69>78.41 </td>
  <td class=xl69>56.51 </td>
  <td class=xl69>49.81 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td rowspan=8 height=144 class=xl65 style='height:108.0pt'>111213</td>
  <td class=xl66>Degree</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>87.61 </td>
  <td class=xl67>66.14 </td>
  <td class=xl67>64.70 </td>
  <td class=xl67>51.91 </td>
  <td class=xl67>54.19 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Closeness</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>86.87 </td>
  <td class=xl67>60.58 </td>
  <td class=xl67>64.25 </td>
  <td class=xl67>57.91 </td>
  <td class=xl67>57.91 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Harmonic</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>90.91 </td>
  <td class=xl67>65.42 </td>
  <td class=xl67>63.94 </td>
  <td class=xl67>61.73 </td>
  <td class=xl67>54.04 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Katz</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>85.77 </td>
  <td class=xl67>63.59 </td>
  <td class=xl67>65.59 </td>
  <td class=xl67>55.97 </td>
  <td class=xl67>53.73 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Average</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>90.91 </td>
  <td class=xl67>60.93 </td>
  <td class=xl67>63.11 </td>
  <td class=xl67>61.73 </td>
  <td class=xl67>54.06 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Concatenate</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>90.99 </td>
  <td class=xl67>60.27 </td>
  <td class=xl67>63.16 </td>
  <td class=xl67>61.73 </td>
  <td class=xl67>54.06 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl68 style='height:13.5pt'>MaMaDroid</td>
  <td class=xl69>　</td>
  <td class=xl69>　</td>
  <td class=xl69>84.84 </td>
  <td class=xl69>73.66 </td>
  <td class=xl69>70.82 </td>
  <td class=xl69>55.84 </td>
  <td class=xl69>46.16 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl68 style='height:13.5pt'>Drebin</td>
  <td class=xl69>　</td>
  <td class=xl69>　</td>
  <td class=xl69>91.18 </td>
  <td class=xl69>65.70 </td>
  <td class=xl69>66.73 </td>
  <td class=xl69>55.06 </td>
  <td class=xl69>52.71 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td rowspan=8 height=144 class=xl65 style='height:108.0pt'>11121314</td>
  <td class=xl66>Degree</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>76.71 </td>
  <td class=xl67>70.19 </td>
  <td class=xl67>62.48 </td>
  <td class=xl67>69.07 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Closeness</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>72.82 </td>
  <td class=xl67>71.23 </td>
  <td class=xl67>59.44 </td>
  <td class=xl67>59.57 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Harmonic</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>78.55 </td>
  <td class=xl67>75.45 </td>
  <td class=xl67>71.44 </td>
  <td class=xl67>70.38 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Katz</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>77.67 </td>
  <td class=xl67>68.37 </td>
  <td class=xl67>55.27 </td>
  <td class=xl67>51.60 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Average</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>79.73 </td>
  <td class=xl67>77.17 </td>
  <td class=xl67>71.22 </td>
  <td class=xl67>70.91 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl66 style='height:13.5pt'>Concatenate</td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67></td>
  <td class=xl67>84.16 </td>
  <td class=xl67>81.95 </td>
  <td class=xl67>74.18 </td>
  <td class=xl67>71.86 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl68 style='height:13.5pt'>MaMaDroid</td>
  <td class=xl69>　</td>
  <td class=xl69>　</td>
  <td class=xl69>　</td>
  <td class=xl69>82.92 </td>
  <td class=xl69>77.87 </td>
  <td class=xl69>71.40 </td>
  <td class=xl69>65.81 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl68 style='height:13.5pt'>Drebin</td>
  <td class=xl69>　</td>
  <td class=xl69>　</td>
  <td class=xl69>　</td>
  <td class=xl69>65.97 </td>
  <td class=xl69>66.75 </td>
  <td class=xl69>54.63 </td>
  <td class=xl69>52.73 </td>
 </tr>
 <![if supportMisalignedColumns]>
 <tr height=0 style='display:none'>
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


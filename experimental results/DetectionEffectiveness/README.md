# Detction Effectiveness

We first evaluate how well MalScan on detecting malware
by training and testing using samples that are developed
in the same year. (F1: F-measure, A: Accuracy)

<table border=0 cellpadding=0 cellspacing=0 width=1302 style='border-collapse:
 collapse;table-layout:fixed;width:977pt'>
 <col class=xl65 width=150 style='mso-width-source:userset;mso-width-alt:4800;
 width:113pt'>
 <col class=xl65 width=72 span=16 style='width:54pt'>
 <tr class=xl65 height=18 style='height:13.5pt'>
  <td height=18 class=xl65 width=150 style='height:13.5pt;width:113pt'>Dataset</td>
  <td colspan=2 class=xl65 width=144 style='width:108pt'>2011</td>
  <td colspan=2 class=xl65 width=144 style='width:108pt'>2012</td>
  <td colspan=2 class=xl65 width=144 style='width:108pt'>2013</td>
  <td colspan=2 class=xl65 width=144 style='width:108pt'>2014</td>
  <td colspan=2 class=xl65 width=144 style='width:108pt'>2015</td>
  <td colspan=2 class=xl65 width=144 style='width:108pt'>2016</td>
  <td colspan=2 class=xl65 width=144 style='width:108pt'>2017</td>
  <td colspan=2 class=xl65 width=144 style='width:108pt'>2018</td>
 </tr>
 <tr class=xl65 height=18 style='height:13.5pt'>
  <td height=18 class=xl65 style='height:13.5pt'>Metrics</td>
  <td class=xl65>F1</td>
  <td class=xl65>A</td>
  <td class=xl65>F1</td>
  <td class=xl65>A</td>
  <td class=xl65>F1</td>
  <td class=xl65>A</td>
  <td class=xl65>F1</td>
  <td class=xl65>A</td>
  <td class=xl65>F1</td>
  <td class=xl65>A</td>
  <td class=xl65>F1</td>
  <td class=xl65>A</td>
  <td class=xl65>F1</td>
  <td class=xl65>A</td>
  <td class=xl65>F1</td>
  <td class=xl65>A</td>
 </tr>
 <tr class=xl65 height=18 style='height:13.5pt'>
  <td height=18 class=xl65 style='height:13.5pt'>Degree</td>
  <td class=xl65>95.54</td>
  <td class=xl65>95.44</td>
  <td class=xl65>96.67</td>
  <td class=xl65>96.49</td>
  <td class=xl65>96.38</td>
  <td class=xl65>96.23</td>
  <td class=xl65>95.62</td>
  <td class=xl65>96.43</td>
  <td class=xl65>98.06</td>
  <td class=xl65>98.08</td>
  <td class=xl65>98.49</td>
  <td class=xl65>98.51</td>
  <td class=xl65>97.04</td>
  <td class=xl65>97.04</td>
  <td class=xl65>97.92</td>
  <td class=xl65>97.99</td>
 </tr>
 <tr class=xl65 height=18 style='height:13.5pt'>
  <td height=18 class=xl65 style='height:13.5pt'>Closeness</td>
  <td class=xl65>96.18</td>
  <td class=xl65>96.12</td>
  <td class=xl65>96.5</td>
  <td class=xl65>96.31</td>
  <td class=xl65>96.68</td>
  <td class=xl65>96.54</td>
  <td class=xl65>96.69</td>
  <td class=xl65>96.54</td>
  <td class=xl65>97.59</td>
  <td class=xl65>97.56</td>
  <td class=xl65>97.28</td>
  <td class=xl65>97.32</td>
  <td class=xl65>97.68</td>
  <td class=xl65>97.69</td>
  <td class=xl65>98.76</td>
  <td class=xl65>98.79</td>
 </tr>
 <tr class=xl65 height=18 style='height:13.5pt'>
  <td height=18 class=xl65 style='height:13.5pt'>Harmonic</td>
  <td class=xl65>96.86</td>
  <td class=xl65>96.85</td>
  <td class=xl65>97.97</td>
  <td class=xl65>97.88</td>
  <td class=xl65>97.16</td>
  <td class=xl65>97.05</td>
  <td class=xl65>96.77</td>
  <td class=xl65>96.61</td>
  <td class=xl65>95.98</td>
  <td class=xl65>96.05</td>
  <td class=xl65>97.21</td>
  <td class=xl65>97.3</td>
  <td class=xl65>96.81</td>
  <td class=xl65>96.83</td>
  <td class=xl65>97.87</td>
  <td class=xl65>97.96</td>
 </tr>
 <tr class=xl65 height=18 style='height:13.5pt'>
  <td height=18 class=xl65 style='height:13.5pt'>Katz</td>
  <td class=xl65>95.59</td>
  <td class=xl65>95.78</td>
  <td class=xl65>96.38</td>
  <td class=xl65>96.15</td>
  <td class=xl65>96.93</td>
  <td class=xl65>96.82</td>
  <td class=xl65>96.61</td>
  <td class=xl65>96.48</td>
  <td class=xl65>97.4</td>
  <td class=xl65>97.37</td>
  <td class=xl65>98.03</td>
  <td class=xl65>98.05</td>
  <td class=xl65>98.43</td>
  <td class=xl65>98.44</td>
  <td class=xl65>98.03</td>
  <td class=xl65>98.09</td>
 </tr>
 <tr class=xl65 height=18 style='height:13.5pt'>
  <td height=18 class=xl65 style='height:13.5pt'>Average</td>
  <td class=xl65>97.18</td>
  <td class=xl65>97.19</td>
  <td class=xl65>97.92</td>
  <td class=xl65>97.86</td>
  <td class=xl65>97.16</td>
  <td class=xl65>97.05</td>
  <td class=xl65>96.62</td>
  <td class=xl65>96.46</td>
  <td class=xl65>96.69</td>
  <td class=xl65>96.66</td>
  <td class=xl65>97.7</td>
  <td class=xl65>97.72</td>
  <td class=xl65>96.94</td>
  <td class=xl65>96.96</td>
  <td class=xl65>98.28</td>
  <td class=xl65>98.34</td>
 </tr>
 <tr class=xl65 height=18 style='height:13.5pt'>
  <td height=18 class=xl65 style='height:13.5pt'>Concatenate</td>
  <td class=xl65>97.5</td>
  <td class=xl65>97.5</td>
  <td class=xl65>98.07</td>
  <td class=xl65>97.99</td>
  <td class=xl65>97.5</td>
  <td class=xl65>97.41</td>
  <td class=xl65>97.72</td>
  <td class=xl65>97.64</td>
  <td class=xl65>97.58</td>
  <td class=xl65>97.56</td>
  <td class=xl65>97.65</td>
  <td class=xl65>97.7</td>
  <td class=xl65>97.1</td>
  <td class=xl65>97.12</td>
  <td class=xl65>98.42</td>
  <td class=xl65>98.47</td>
 </tr>
 <tr class=xl65 height=18 style='height:13.5pt'>
  <td height=18 class=xl65 style='height:13.5pt'>MaMa</td>
  <td class=xl65>94.39</td>
  <td class=xl65>94.2</td>
  <td class=xl65>95.62</td>
  <td class=xl65>95.34</td>
  <td class=xl65>94.29</td>
  <td class=xl65>93.91</td>
  <td class=xl65>95.86</td>
  <td class=xl65>95.63</td>
  <td class=xl65>95.57</td>
  <td class=xl65>95.44</td>
  <td class=xl65>95.99</td>
  <td class=xl65>95.98</td>
  <td class=xl65>96.48</td>
  <td class=xl65>96.52</td>
  <td class=xl65>97.29</td>
  <td class=xl65>97.24</td>
 </tr>
 <tr class=xl65 height=18 style='height:13.5pt'>
  <td height=18 class=xl65 style='height:13.5pt'>Drebin</td>
  <td class=xl65>96.35</td>
  <td class=xl65>96.35</td>
  <td class=xl65>96.44</td>
  <td class=xl65>96.44</td>
  <td class=xl65>97.36</td>
  <td class=xl65>97.36</td>
  <td class=xl65>94.75</td>
  <td class=xl65>94.75</td>
  <td class=xl65>94.74</td>
  <td class=xl65>94.74</td>
  <td class=xl65>95.27</td>
  <td class=xl65>95.27</td>
  <td class=xl65>91.02</td>
  <td class=xl65>91.01</td>
  <td class=xl65>91.2</td>
  <td class=xl65>91.19</td>
 </tr>
 <tr class=xl65 height=18 style='height:13.5pt'>
  <td height=18 class=xl67 style='height:13.5pt'></td>
  <td class=xl68></td>
  <td class=xl68></td>
  <td class=xl68></td>
  <td class=xl68></td>
  <td class=xl66></td>
  <td class=xl66></td>
  <td class=xl66></td>
  <td class=xl66></td>
  <td class=xl66></td>
  <td class=xl66></td>
  <td class=xl66></td>
  <td class=xl66></td>
  <td class=xl66></td>
  <td class=xl66></td>
  <td class=xl66></td>
  <td class=xl66></td>
 </tr>
 <![if supportMisalignedColumns]>
 <tr height=0 style='display:none'>
  <td width=150 style='width:113pt'></td>
  <td width=72 style='width:54pt'></td>
  <td width=72 style='width:54pt'></td>
  <td width=72 style='width:54pt'></td>
  <td width=72 style='width:54pt'></td>
  <td width=72 style='width:54pt'></td>
  <td width=72 style='width:54pt'></td>
  <td width=72 style='width:54pt'></td>
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



# RunTime Overhead

We alseo estimate the runtime overhead of
MalScan, MaMaDroid and Drebin by using a dataset randomly
selected from our 30,715 samples, which consists of 3,000
benign apps and 3,000 malicious apps. The average number
of nodes in these 3,000 benign samples and 3,000 malicious
samples are 17,669 and 12,991 respectively. The following table shows the runtime overhead (seconds) of MalScan, MaMaDroid and
Drebin in different phases.

<table border=0 cellpadding=0 cellspacing=0 width=724 style='border-collapse:
 collapse;table-layout:fixed;width:543pt'>
 <col width=99 style='mso-width-source:userset;mso-width-alt:3168;width:74pt'>
 <col width=166 style='mso-width-source:userset;mso-width-alt:5312;width:125pt'>
 <col width=171 style='mso-width-source:userset;mso-width-alt:5472;width:128pt'>
 <col width=72 span=4 style='width:54pt'>
 <tr height=18 style='height:13.5pt'>
  <td rowspan=2 height=36 class=xl65 width=99 style='height:27.0pt;width:74pt'>Phases</td>
  <td rowspan=2 class=xl65 width=166 style='width:125pt'>Graph Construction</td>
  <td rowspan=2 class=xl65 width=171 style='width:128pt'>Feature Extraction</td>
  <td colspan=4 class=xl65 width=288 style='width:216pt'>Classification</td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl65 style='height:13.5pt'>1nn</td>
  <td class=xl65>3nn</td>
  <td class=xl65>RF</td>
  <td class=xl65>SVM</td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl65 style='height:13.5pt'>Degree</td>
  <td rowspan=6 class=xl66>0.6654 </td>
  <td class=xl66>0.0293 </td>
  <td class=xl66>0.0093 </td>
  <td class=xl66>0.0766 </td>
  <td class=xl66>0.0015 </td>
  <td rowspan=7 class=xl66>None</td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl65 style='height:13.5pt'>Closeness</td>
  <td class=xl66>1.1007 </td>
  <td class=xl66>0.0093 </td>
  <td class=xl66>0.0886 </td>
  <td class=xl66>0.0014 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl65 style='height:13.5pt'>Harmonic</td>
  <td class=xl66>1.6275 </td>
  <td class=xl66>0.0139 </td>
  <td class=xl66>0.0697 </td>
  <td class=xl66>0.0015 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl65 style='height:13.5pt'>Katz</td>
  <td class=xl66>1.4984 </td>
  <td class=xl66>0.0110 </td>
  <td class=xl66>0.1102 </td>
  <td class=xl66>0.0014 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl65 style='height:13.5pt'>Average<span
  style='mso-spacerun:yes'>&nbsp;</span></td>
  <td class=xl66>4.2560 </td>
  <td class=xl66>0.0139 </td>
  <td class=xl66>0.0731 </td>
  <td class=xl66>0.0014 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl65 style='height:13.5pt'>Concatenate</td>
  <td class=xl66>4.2556 </td>
  <td class=xl66>0.0456 </td>
  <td class=xl66>0.2478 </td>
  <td class=xl66>0.0016 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl65 style='height:13.5pt'>MaMaDroid</td>
  <td class=xl66>163.1773 </td>
  <td class=xl66>2.4562 </td>
  <td class=xl66>0.4867 </td>
  <td class=xl66>1.4501 </td>
  <td class=xl66>0.0007 </td>
 </tr>
 <tr height=18 style='height:13.5pt'>
  <td height=18 class=xl65 style='height:13.5pt'>Drebin</td>
  <td class=xl66>None</td>
  <td class=xl66>82.3846 </td>
  <td colspan=3 class=xl66>None</td>
  <td class=xl66>0.3090 </td>
 </tr>
 <![if supportMisalignedColumns]>
 <tr height=0 style='display:none'>
  <td width=99 style='width:74pt'></td>
  <td width=166 style='width:125pt'></td>
  <td width=171 style='width:128pt'></td>
  <td width=72 style='width:54pt'></td>
  <td width=72 style='width:54pt'></td>
  <td width=72 style='width:54pt'></td>
  <td width=72 style='width:54pt'></td>
 </tr>
 <![endif]>
</table>

Experimental Setup
=======
For testing the resilience of CenDroid on the evolution of Android apps. We created four scenarios and conducted experiments
on each scenario, the f-measure of CenDroid, MaMaDroid and Drebin is presented in the following table. In the first scenario, each system was trained by using the 2011 dataset,
and then classified the samples from 2012 to 2018. In the second scenario, we used the samples randomly selected from datasets before 2012 (i.e., 2011 and 2012 datasets) as the
training data and tested the samples from 2013 to 2018. Similar to the before scenarios, the training samples in the third scenario was randomly selected from datasets before
2013, and the testing samples are from 2014 to 2018. Our final scenario includes randomly-chosen training samples from datasets before 2014, and conducted classification on the samples in 2015, 2016, 2017 and 2018.

Experimental Results
===

In order to verify the effectiveness of
different centrality measures on detecting Android malware,
we first conduct four experiments according to the four selected
centrality measures which are degree centrality, closeness
centrality, katz centrality and harmonic centrality. Additionally,
it is generally to measure the importance of a vertex
in a social network by combining multiple centrality metrics.
Therefor, we add another experiment by calculating the
average value of the former four centrality measures. In a
word, we evaluate CenDroid by conducting five experiments
on each scenario. And the CenDroid_AVE is the average value of the five experimental results, CenDroid_MAX is the max value of
the five experimental results. The following table shows the f-measure of our experimental results.
<table>

 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r0'>
<td colspan='2' rowspan='2' height='36' class='x25' width='180' style='height:27pt;'>Training</td>
<td colspan='7' class='x26' width='504'>Testing</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r1'>
<td class='x22'>2012</td>
<td class='x22'>2013</td>
<td class='x22'>2014</td>
<td class='x22'>2015</td>
<td class='x22'>2016</td>
<td class='x22'>2017</td>
<td class='x22'>2018</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r2'>
<td rowspan='9' height='162' class='x25' style='height:121.5pt;'>2011</td>
<td class='x22'>Degree</td>
<td class='x21' x:num="85.23">85.23</td>
<td class='x21' x:num="83.07">83.07</td>
<td class='x21' x:num="74.37">74.37</td>
<td class='x21' x:num="19.23">19.23</td>
<td class='x21' x:num="19.11">19.11</td>
<td class='x21' x:num="28.51">28.51</td>
<td class='x21' x:num="24.43">24.43</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r3'>
<td class='x22'>Closeness</td>
<td class='x21' x:num="82.93">82.93</td>
<td class='x21' x:num="73.83">73.83</td>
<td class='x21' x:num="68.959999999999994">68.96</td>
<td class='x21' x:num="26.05">26.05</td>
<td class='x21' x:num="32.58">32.58</td>
<td class='x21' x:num="24.87">24.87</td>
<td class='x21' x:num="27.36">27.36</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r4'>
<td class='x22'>Harmonic</td>
<td class='x21' x:num="89.73">89.73</td>
<td class='x21' x:num="86.32">86.32</td>
<td class='x21' x:num="76.540000000000006">76.54</td>
<td class='x21' x:num="30.31">30.31</td>
<td class='x21' x:num="34.869999999999997">34.87</td>
<td class='x21' x:num="21.95">21.95</td>
<td class='x21' x:num="16.16">16.16</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r5'>
<td class='x22'>Katz</td>
<td class='x21' x:num="86.25">86.25</td>
<td class='x21' x:num="79.430000000000007">79.43</td>
<td class='x21' x:num="76.66">76.66</td>
<td class='x21' x:num="38.270000000000003">38.27</td>
<td class='x21' x:num="28.03">28.03</td>
<td class='x21' x:num="13.87">13.87</td>
<td class='x21' x:num="9.08">9.08</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r6'>
<td class='x22'>Average</td>
<td class='x21' x:num="89.80">89.80</td>
<td class='x21' x:num="86.70">86.70</td>
<td class='x21' x:num="76.77">76.77</td>
<td class='x21' x:num="29.64">29.64</td>
<td class='x21' x:num="34.200000000000003">34.20</td>
<td class='x21' x:num="21.37">21.37</td>
<td class='x21' x:num="16.09">16.09</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r7'>
<td class='x23'>CenDroid_AVE</td>
<td class='x24' x:num="87.515" x:fmla="=AVERAGE(C3,C7)">87.52</td>
<td class='x24' x:num="84.885" x:fmla="=AVERAGE(D3,D7)">84.89</td>
<td class='x24' x:num="75.569999999999993" x:fmla="=AVERAGE(E3,E7)">75.57</td>
<td class='x24' x:num="24.435" x:fmla="=AVERAGE(F3,F7)">24.44</td>
<td class='x24' x:num="26.655" x:fmla="=AVERAGE(G3,G7)">26.66</td>
<td class='x24' x:num="24.94" x:fmla="=AVERAGE(H3,H7)">24.94</td>
<td class='x24' x:num="20.259999999999998" x:fmla="=AVERAGE(I3,I7)">20.26</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r8'>
<td class='x23'>CenDroid_MAX</td>
<td class='x24' x:num="89.80" x:fmla="=MAX(C3:C7)">89.80</td>
<td class='x24' x:num="86.70" x:fmla="=MAX(D3:D7)">86.70</td>
<td class='x24' x:num="76.77" x:fmla="=MAX(E3:E7)">76.77</td>
<td class='x24' x:num="38.270000000000003" x:fmla="=MAX(F3:F7)">38.27</td>
<td class='x24' x:num="34.869999999999997" x:fmla="=MAX(G3:G7)">34.87</td>
<td class='x24' x:num="28.51" x:fmla="=MAX(H3:H7)">28.51</td>
<td class='x24' x:num="27.36" x:fmla="=MAX(I3:I7)">27.36</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r9'>
<td class='x23'>MaMaDroid</td>
<td class='x24' x:num="81.94">81.94</td>
<td class='x24' x:num="78.680000000000007">78.68</td>
<td class='x24' x:num="71.900000000000006">71.90</td>
<td class='x24' x:num="54.58">54.58</td>
<td class='x24' x:num="50.28">50.28</td>
<td class='x24' x:num="36.58">36.58</td>
<td class='x24' x:num="17.23">17.23</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r10'>
<td class='x23'>Drebin</td>
<td class='x24' x:num="84.37">84.37</td>
<td class='x24' x:num="80.37">80.37</td>
<td class='x24' x:num="81.64">81.64</td>
<td class='x24' x:num="38.380000000000003">38.38</td>
<td class='x24' x:num="37.40">37.40</td>
<td class='x24' x:num="35.33">35.33</td>
<td class='x24' x:num="35.46">35.46</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r11'>
<td rowspan='9' height='162' class='x25' style='height:121.5pt;'>1112</td>
<td class='x22'>Degree</td>
<td class='x21'></td>
<td class='x21' x:num="84.39">84.39</td>
<td class='x21' x:num="76.66">76.66</td>
<td class='x21' x:num="65.97">65.97</td>
<td class='x21' x:num="56.41">56.41</td>
<td class='x21' x:num="16.47">16.47</td>
<td class='x21' x:num="13.55">13.55</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r12'>
<td class='x22'>Closeness</td>
<td class='x21'></td>
<td class='x21' x:num="88.67">88.67</td>
<td class='x21' x:num="80.19">80.19</td>
<td class='x21' x:num="68.47">68.47</td>
<td class='x21' x:num="58.09">58.09</td>
<td class='x21' x:num="30.98">30.98</td>
<td class='x21' x:num="24.31">24.31</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r13'>
<td class='x22'>Harmonic</td>
<td class='x21'></td>
<td class='x21' x:num="89.67">89.67</td>
<td class='x21' x:num="79.55">79.55</td>
<td class='x21' x:num="64.17">64.17</td>
<td class='x21' x:num="62.19">62.19</td>
<td class='x21' x:num="43.76">43.76</td>
<td class='x21' x:num="26.30">26.30</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r14'>
<td class='x22'>Katz</td>
<td class='x21'></td>
<td class='x21' x:num="85.49">85.49</td>
<td class='x21' x:num="77.23">77.23</td>
<td class='x21' x:num="72.180000000000007">72.18</td>
<td class='x21' x:num="58.35">58.35</td>
<td class='x21' x:num="23.70">23.70</td>
<td class='x21' x:num="17.61">17.61</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r15'>
<td class='x22'>Average</td>
<td class='x21'></td>
<td class='x21' x:num="89.65">89.65</td>
<td class='x21' x:num="79.55">79.55</td>
<td class='x21' x:num="70.62">70.62</td>
<td class='x21' x:num="64.849999999999994">64.85</td>
<td class='x21' x:num="43.21">43.21</td>
<td class='x21' x:num="26.29">26.29</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r16'>
<td class='x23'>CenDroid_AVE</td>
<td class='x24'></td>
<td class='x24' x:num="87.573999999999998" x:fmla="=AVERAGE(D12:D16)">87.57</td>
<td class='x24' x:num="78.635999999999996" x:fmla="=AVERAGE(E12:E16)">78.64</td>
<td class='x24' x:num="68.282000000000011" x:fmla="=AVERAGE(F12:F16)">68.28</td>
<td class='x24' x:num="59.977999999999994" x:fmla="=AVERAGE(G12:G16)">59.98</td>
<td class='x24' x:num="31.624000000000002" x:fmla="=AVERAGE(H12:H16)">31.62</td>
<td class='x24' x:num="21.612000000000002" x:fmla="=AVERAGE(I12:I16)">21.61</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r17'>
<td class='x23'>CenDroid_MAX</td>
<td class='x24'></td>
<td class='x24' x:num="89.67" x:fmla="=MAX(D12:D16)">89.67</td>
<td class='x24' x:num="80.19" x:fmla="=MAX(E12:E16)">80.19</td>
<td class='x24' x:num="72.180000000000007" x:fmla="=MAX(F12:F16)">72.18</td>
<td class='x24' x:num="64.849999999999994" x:fmla="=MAX(G12:G16)">64.85</td>
<td class='x24' x:num="43.76" x:fmla="=MAX(H12:H16)">43.76</td>
<td class='x24' x:num="26.30" x:fmla="=MAX(I12:I16)">26.30</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r18'>
<td class='x23'>MaMaDroid</td>
<td class='x24'></td>
<td class='x24' x:num="87.43">87.43</td>
<td class='x24' x:num="78.39">78.39</td>
<td class='x24' x:num="65.06">65.06</td>
<td class='x24' x:num="66.489999999999995">66.49</td>
<td class='x24' x:num="54.32">54.32</td>
<td class='x24' x:num="40.39">40.39</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r19'>
<td class='x23'>Drebin</td>
<td class='x24'></td>
<td class='x24' x:num="91.02">91.02</td>
<td class='x24' x:num="82.65">82.65</td>
<td class='x24' x:num="77.62">77.62</td>
<td class='x24' x:num="77.86">77.86</td>
<td class='x24' x:num="50.94">50.94</td>
<td class='x24' x:num="40.90">40.90</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r20'>
<td rowspan='9' height='162' class='x25' style='height:121.5pt;'>111213</td>
<td class='x22'>Degree</td>
<td class='x21'></td>
<td class='x21'></td>
<td class='x21' x:num="86.94">86.94</td>
<td class='x21' x:num="53.04">53.04</td>
<td class='x21' x:num="46.32">46.32</td>
<td class='x21' x:num="13.49">13.49</td>
<td class='x21' x:num="13.73">13.73</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r21'>
<td class='x22'>Closeness</td>
<td class='x21'></td>
<td class='x21'></td>
<td class='x21' x:num="86.32">86.32</td>
<td class='x21' x:num="38.159999999999997">38.16</td>
<td class='x21' x:num="44.29">44.29</td>
<td class='x21' x:num="29.79">29.79</td>
<td class='x21' x:num="25.60">25.60</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r22'>
<td class='x22'>Harmonic</td>
<td class='x21'></td>
<td class='x21'></td>
<td class='x21' x:num="90.86">90.86</td>
<td class='x21' x:num="51.57">51.57</td>
<td class='x21' x:num="46.23">46.23</td>
<td class='x21' x:num="41.37">41.37</td>
<td class='x21' x:num="22.03">22.03</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r23'>
<td class='x22'>Katz</td>
<td class='x21'></td>
<td class='x21'></td>
<td class='x21' x:num="84.95">84.95</td>
<td class='x21' x:num="48.83">48.83</td>
<td class='x21' x:num="51.27">51.27</td>
<td class='x21' x:num="26.29">26.29</td>
<td class='x21' x:num="22.03">22.03</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r24'>
<td class='x22'>Average</td>
<td class='x21'></td>
<td class='x21'></td>
<td class='x21' x:num="90.86">90.86</td>
<td class='x21' x:num="40.28">40.28</td>
<td class='x21' x:num="41.29">41.29</td>
<td class='x21' x:num="41.37">41.37</td>
<td class='x21' x:num="22.02">22.02</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r25'>
<td class='x23'>CenDroid_AVE</td>
<td class='x24'></td>
<td class='x24'></td>
<td class='x24' x:num="87.986000000000004" x:fmla="=AVERAGE(E21:E25)">87.99</td>
<td class='x24' x:num="46.375999999999991" x:fmla="=AVERAGE(F21:F25)">46.38</td>
<td class='x24' x:num="45.88" x:fmla="=AVERAGE(G21:G25)">45.88</td>
<td class='x24' x:num="30.462" x:fmla="=AVERAGE(H21:H25)">30.46</td>
<td class='x24' x:num="21.082000000000001" x:fmla="=AVERAGE(I21:I25)">21.08</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r26'>
<td class='x23'>CenDroid_MAX</td>
<td class='x24'></td>
<td class='x24'></td>
<td class='x24' x:num="90.86" x:fmla="=MAX(E21:E25)">90.86</td>
<td class='x24' x:num="53.04" x:fmla="=MAX(F21:F25)">53.04</td>
<td class='x24' x:num="51.27" x:fmla="=MAX(G21:G25)">51.27</td>
<td class='x24' x:num="41.37" x:fmla="=MAX(H21:H25)">41.37</td>
<td class='x24' x:num="25.60" x:fmla="=MAX(I21:I25)">25.60</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r27'>
<td class='x23'>MaMaDroid</td>
<td class='x24'></td>
<td class='x24'></td>
<td class='x24' x:num="86.04">86.04</td>
<td class='x24' x:num="71.52">71.52</td>
<td class='x24' x:num="70.599999999999994">70.60</td>
<td class='x24' x:num="50.97">50.97</td>
<td class='x24' x:num="22.52">22.52</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r28'>
<td class='x23'>Drebin</td>
<td class='x24'></td>
<td class='x24'></td>
<td class='x24' x:num="91.16">91.16</td>
<td class='x24' x:num="61.52">61.52</td>
<td class='x24' x:num="62.36">62.36</td>
<td class='x24' x:num="43.68">43.68</td>
<td class='x24' x:num="38.06">38.06</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r29'>
<td rowspan='9' height='162' class='x25' style='height:121.5pt;'>11121314</td>
<td class='x22'>Degree</td>
<td class='x21'></td>
<td class='x21'></td>
<td class='x21'></td>
<td class='x21' x:num="71.569999999999993">71.57</td>
<td class='x21' x:num="58.53">58.53</td>
<td class='x21' x:num="41.36">41.36</td>
<td class='x21' x:num="55.82">55.82</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r30'>
<td class='x22'>Closeness</td>
<td class='x21'></td>
<td class='x21'></td>
<td class='x21'></td>
<td class='x21' x:num="65.290000000000006">65.29</td>
<td class='x21' x:num="59.73">59.73</td>
<td class='x21' x:num="34.21">34.21</td>
<td class='x21' x:num="34.21">34.21</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r31'>
<td class='x22'>Harmonic</td>
<td class='x21'></td>
<td class='x21'></td>
<td class='x21'></td>
<td class='x21' x:num="74.489999999999995">74.49</td>
<td class='x21' x:num="67.900000000000006">67.90</td>
<td class='x21' x:num="62.45">62.45</td>
<td class='x21' x:num="60.04">60.04</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r32'>
<td class='x22'>Katz</td>
<td class='x21'></td>
<td class='x21'></td>
<td class='x21'></td>
<td class='x21' x:num="73.040000000000006">73.04</td>
<td class='x21' x:num="57.11">57.11</td>
<td class='x21' x:num="25.59">25.59</td>
<td class='x21' x:num="19.02">19.02</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r33'>
<td class='x22'>Average</td>
<td class='x21'></td>
<td class='x21'></td>
<td class='x21'></td>
<td class='x21' x:num="76.22">76.22</td>
<td class='x21' x:num="70.81">70.81</td>
<td class='x21' x:num="64.38">64.38</td>
<td class='x21' x:num="61.03">61.03</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r34'>
<td class='x23'>CenDroid_AVE</td>
<td class='x24'></td>
<td class='x24'></td>
<td class='x24'></td>
<td class='x24' x:num="72.122" x:fmla="=AVERAGE(F30:F34)">72.12</td>
<td class='x24' x:num="62.815999999999995" x:fmla="=AVERAGE(G30:G34)">62.82</td>
<td class='x24' x:num="45.597999999999999" x:fmla="=AVERAGE(H30:H34)">45.60</td>
<td class='x24' x:num="46.024000000000001" x:fmla="=AVERAGE(I30:I34)">46.02</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r35'>
<td class='x23'>CenDroid_MAX</td>
<td class='x24'></td>
<td class='x24'></td>
<td class='x24'></td>
<td class='x24' x:num="76.22" x:fmla="=MAX(F30:F34)">76.22</td>
<td class='x24' x:num="70.81" x:fmla="=MAX(G30:G34)">70.81</td>
<td class='x24' x:num="64.38" x:fmla="=MAX(H30:H34)">64.38</td>
<td class='x24' x:num="61.03" x:fmla="=MAX(I30:I34)">61.03</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r36'>
<td class='x23'>MaMaDroid</td>
<td class='x24'></td>
<td class='x24'></td>
<td class='x24'></td>
<td class='x24' x:num="81.77">81.77</td>
<td class='x24' x:num="74.459999999999994">74.46</td>
<td class='x24' x:num="64.12">64.12</td>
<td class='x24' x:num="57.20">57.20</td>
 </tr>
 <tr height='18' style='mso-height-source:userset;height:13.5pt' id='r37'>
<td class='x23'>Drebin</td>
<td class='x24'></td>
<td class='x24'></td>
<td class='x24'></td>
<td class='x24' x:num="62.15">62.15</td>
<td class='x24' x:num="62.36">62.36</td>
<td class='x24' x:num="42.61">42.61</td>
<td class='x24' x:num="37.79">37.79</td>
 </tr>

</table>

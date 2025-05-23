# [Gold III] Reverse a Road - 22666 

[문제 링크](https://www.acmicpc.net/problem/22666) 

### 성능 요약

메모리: 35004 KB, 시간: 164 ms

### 분류

데이크스트라, 그래프 이론, 최단 경로

### 제출 일자

2025년 5월 2일 09:54:14

### 문제 설명

<p>Andrew R. Klein resides in the city of Yanwoe, and goes to his working place in this city every weekday. He has been totally annoyed with the road traffic of this city. All the roads in this city are one-way, so he has to drive a longer way than he thinks he need.</p>

<p>One day, the following thought has come up to Andrew’s mind: “How about making the sign of one road indicate the opposite direction? I think my act won’t be out as long as I change just one sign. Well, of course I want to make my route to the working place shorter as much as possible. Which road should I alter the direction of?” What a clever guy he is.</p>

<p>You are asked by Andrew to write a program that finds the shortest route when the direction of up to one road is allowed to be altered. You don’t have to worry about the penalty for complicity, because you resides in a different country from Andrew and cannot be punished by the law of his country. So just help him!</p>

### 입력 

 <p>The input consists of a series of datasets, each of which is formatted as follows:</p>

<pre><i>N</i>
<i>S T</i>
<i>M</i>
<i>A</i><sub>1</sub> <i>B</i><sub>1</sub>
<i>A</i><sub>2</sub> <i>B</i><sub>2</sub>
...
<i>A<sub>M</sub></i> <i>B<sub>M</sub></i>
</pre>

<p><i>N</i> denotes the number of points. <i>S</i> and <i>T</i> indicate the points where Andrew’s home and working place are located respectively. <i>M</i> denotes the number of roads. Finally, <i>A<sub>i</sub></i> and <i>B<sub>i</sub></i> indicate the starting and ending points of the <i>i</i>-th road respectively. Each point is identified by a unique number from 1 to <i>N</i>. Some roads may start and end at the same point. Also, there may be more than one road connecting the same pair of starting and ending points.</p>

<p>You may assume all the following: 1 ≤ <i>N</i> ≤ 1000, 1 ≤ <i>M</i> ≤ 10000, and <i>S</i> ≠ <i>T</i>.</p>

<p>The input is terminated by a line that contains a single zero. This is not part of any dataset, and hence should not be processed.</p>

### 출력 

 <p>For each dataset, print a line that contains the shortest distance (counted by the number of passed roads) and the road number whose direction should be altered. If there are multiple ways to obtain the shortest distance, choose one with the smallest road number. If no direction change results in a shorter route, print 0 as the road number.</p>

<p>Separate the distance and the road number by a single space. No extra characters are allowed.</p>


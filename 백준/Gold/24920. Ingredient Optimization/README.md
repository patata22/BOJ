# [Gold IV] Ingredient Optimization - 24920 

[문제 링크](https://www.acmicpc.net/problem/24920) 

### 성능 요약

메모리: 35508 KB, 시간: 52 ms

### 분류

자료 구조, 구현, 우선순위 큐, 시뮬레이션, 정렬

### 제출 일자

2025년 3월 19일 14:41:14

### 문제 설명

<p>Hathai is proud that her catering service provides the freshest food in town. To accomplish that, she gets fresh ingredients with no preservatives delivered constantly. This brings about the challenge of preventing the ingredients from spoiling. Her current special uses exactly $U$ leaves of Thai basil, that need special care.</p>

<p>Hathai has the schedule of the deliveries of Thai basil. The $i$-th delivery comes at the beginning of time $M_i$ (in minutes since opening time), and brings exactly $L_i$ leaves of Thai basil that can be stored for at most $E_i$ minutes since arriving. Hathai has orders to prepare her specialty dish at times $O_1,O_2, \dots ,O_N$. Order $i$ can only be fulfilled if she has $U$ unspoiled leaves of Thai basil at time $O_i$. Note that if leaves would spoil at the same time an order comes in, those leaves cannot be used to fulfill that order. If an order is fulfilled, $U$ of the leaves available have to be used and cannot be used for future orders. Once Hathai gets an order that she cannot fulfill, all of the remaining orders will also be canceled because she needs to close her kitchen and think about how to improve the fulfillment schedule.</p>

<p>For example, suppose Hathai's schedule has the following $4$ deliveries:</p>

<ul>
	<li>Delivery time: $1$. Amount: $10$. Time remaining until spoiled: $2$.</li>
	<li>Delivery time: $3$. Amount: $4$. Time remaining until spoiled: $2$.</li>
	<li>Delivery time: $5$. Amount: $1$. Time remaining until spoiled: $4$.</li>
	<li>Delivery time: $10$. Amount: $6$. Time remaining until spoiled: $3$.</li>
</ul>

<p>And also suppose she has $4$ orders placed at times $3$, $4$, $6$ and $10$. Each order requires using $U=2$ leaves in this example.</p>

<p>The first delivery become spoiled at time $3$, so it cannot be used on any order. Then the first order and the second order at time $3$ and time $4$ can be fulfilled and use up the $4$ leaves from the second delivery. For the third order at time $6$, there is only $1$ leaf in the storage, so Hathai cannot fulfill this order. Note that although there is a delivery at time $10$, she still cannot fulfill the fourth order at time $10$ because she has already closed her kitchen. In this example, Hathai managed to fulfill $2$ orders in total.</p>

<p>Given the delivery and order schedules, find out the maximum number of orders Hathai can fulfill if she optimizes the use of the Thai basil leaves.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, $T$. $T$ test cases follow. Each test case starts with a line containing three integers $D$, $N$, and $U$: the number of deliveries, the number of orders and the amount of leaves needed for each order, respectively. Then, $D$ lines follow. The $i$-th of these lines contains three integers $M_i$, $L_i$, and $E_i$: the time of the delivery in minutes since opening time, the amount of Thai basil leaves delivered, and the number of minutes those leaves can be stored and remain fresh, respectively, of the $i$-th delivery. Then, the last line contains $N$ integers $O_1,O_2, \dots ,O_N$, where $O_j$ is the time, in minutes since opening time, at which the $j$-th order must be prepared.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where $x$ is the test case number (starting from 1) and $y$ is an integer representing the maximum number of orders Hathai can fulfill.</p>


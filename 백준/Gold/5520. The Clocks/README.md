# [Gold IV] The Clocks - 5520 

[문제 링크](https://www.acmicpc.net/problem/5520) 

### 성능 요약

메모리: 55844 KB, 시간: 1956 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2025년 4월 7일 10:27:11

### 문제 설명

<pre>|-------|    |-------|    |-------|    
|       |    |       |    |   |   |    
|---O   |    |---O   |    |   O   |          
|       |    |       |    |       |           
|-------|    |-------|    |-------|    
    A            B            C

|-------|    |-------|    |-------|
|       |    |       |    |       |
|   O   |    |   O   |    |   O   |
|   |   |    |   |   |    |   |   |
|-------|    |-------|    |-------|
    D            E            F

|-------|    |-------|    |-------|
|       |    |       |    |       |
|   O   |    |   O---|    |   O   |
|   |   |    |       |    |   |   |
|-------|    |-------|    |-------|  (Figure 1)
    G            H            I</pre>

<p>There are nine clocks in a 3*3 array (figure 1). The goal is to return all the dials to 12 o'clock with as few moves as possible. There are nine different allowed ways to turn the dials on the clocks. Each such way is called a move. Select for each move a number 1 to 9. That number will turn the dials 90' (degrees) clockwise on those clocks which are affected according to figure 2 below.</p>

<pre>Move   Affected clocks
 
 1         ABDE
 2         ABC
 3         BCEF
 4         ADG
 5         BDEFH
 6         CFI
 7         DEGH
 8         GHI
 9         EFHI    (Figure 2)</pre>

<p> </p>

### 입력 

 <p>Read nine numbers from the standard input. These numbers give the start positions of the dials. 0=12 o'clock, 1=3 o'clock, 2=6 o'clock, 3=9 o'clock. The example in figure 1 gives the following input data file:</p>

### 출력 

 <p>Write to the standard output a shortest sequence of moves (numbers) in increasing order, which returns all the dials to 12 o'clock. In case there are many solutions, only one is required.</p>


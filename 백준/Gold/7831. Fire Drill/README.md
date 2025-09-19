# [Gold I] Fire Drill - 7831 

[문제 링크](https://www.acmicpc.net/problem/7831) 

### 성능 요약

메모리: 222068 KB, 시간: 1420 ms

### 분류

너비 우선 탐색, 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색, 구현, 배낭 문제

### 제출 일자

2025년 9월 19일 13:27:10

### 문제 설명

<p>Joko is taking part in a fire drill which is held by the Jakarta Fire Department to recruit new firemen. The drill is about rescuing volunteers (who act as unconscious people) trapped in a building in a limited time. The building has several floors, and the volunteers are scattered throughout the building. Each volunteer has points assigned to her. The fireman candidate should rescue volunteers through carrying them to the exit. The candidate will earn the assigned points for each volunteer he rescued.</p>

<p>Each floor of a building can be seen as a grid of cells. Each cell can be an obstacle, an empty space, a stair or an entry/exit point.</p>

<p>A candidate starts at the entry point which exists only at one single cell of the first floor of the building. The candidate can move to any adjacent non-obstacle cells (north, south, west or east) or climb up or down a stair in 1 second. The movement slows down to 2 seconds when the candidate carries a volunteer. When a candidate finds a volunteer, he may decide to rescue her or not, but if he decides to rescue her, he has to carry her back to the exit without stopping. He can only carry at most one volunteer at a time.</p>

<p>Joko has the floor plan of the test building. Help him plan his moves, so he can get the highest possible score.</p>

### 입력 

 <p>The first line of input contains an integer T (T ≤ 100) denoting the number of case. Each case has five integers L (1 ≤ L ≤ 10), H (1 ≤ H ≤ 100), W (1 ≤ W ≤ 100), N (1 ≤ N ≤ 100) and S (1 ≤ S ≤ 10,000) denoting the number of floors, height and weight of each floor, the number of unconscious people, and the given time respectively.</p>

<p>The next L blocks describe the map of each floor from the 1st floor to the Lth floor respectively. Each floor consists of H lines each contains W characters. Characters that may appear in each floor are:</p>

<ul>
	<li>"S" : The starting point, also serves as the exit point. There will be only one starting/exit point and it will appear in the first floor.</li>
	<li>"X" : Obstacle, cell that cannot be visited (wall, fire, etc.).</li>
	<li>"U" : Stair that connect to the upper floor. There will be a "D" character at the same place in the upper level. This character will not appear in the highest level of the building.</li>
	<li>"D" : Stair that connect to the lower floor. There will be a "U" character at the same place in the lower level. This character will not appear in the lowest level of the building.</li>
	<li>"." : Empty space, cell that can be visited.</li>
</ul>

<p>The next N lines each contains four integers f<sub>i</sub> (1 ≤ f<sub>i</sub> ≤ L), r<sub>i</sub> (1 ≤ r<sub>i</sub> ≤ H), c<sub>i</sub> (1 ≤ c<sub>i</sub> ≤ W), p<sub>i</sub> (1 ≤ p<sub>i</sub> ≤ 1,000) denoting the location of each volunteer (floor, row, column) and the point assigned to this volunteer respectively. You can assume that each volunteer will be located in empty space and no two volunteer occupy the same location.</p>

### 출력 

 <p>For each case, output in a line a single integer the highest point that he can earn by rescuing unconscious people within the given time.</p>


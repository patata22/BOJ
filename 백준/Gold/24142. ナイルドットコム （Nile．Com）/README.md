# [Gold IV] ナイルドットコム (Nile.Com) - 24142 

[문제 링크](https://www.acmicpc.net/problem/24142) 

### 성능 요약

메모리: 293912 KB, 시간: 728 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2025년 3월 24일 14:58:42

### 문제 설명

<p>あなたの配偶者は D 日間毎日インターネットで一種類の商品を購入する．彼女（彼）が使っ ているナイルドットコムのマーケットプレイスには N 店舗が出店している．彼女は毎日そのう ちの 1 店舗を選んでショッピングをする．各店舗の価格は毎日変化するので予定価格が提示さ れている．また，このマーケットプレイスでは同じ店舗で 2 日続けて購入すると 1 割引に，3 日 続けて購入すると 3 割引になる．ただし，それ以降は何日続けて購入しても 3 割引である．</p>

<p>節約家の彼女のために予定価格を基にショッピングの計画を作成することにした．D 日間に 支払う合計金額が最小になるように買い物したときの合計金額を求めよ．</p>

<p>ただし，ナイルドットコムのマーケットプレイスの店舗には識別のため 1 から N までの店舗 番号が付けられていて，各店舗の予定価格は 10 の倍数である．</p>

### 입력 

 <p>入力は (D+1)行のファイルであり，最初の行には店舗数 N とショッ ピングをする日数 D が空白で区切って書かれている．ただし， 2 ≤ N ≤ 3, 000, 2 ≤ D ≤ 365 である．</p>

<p>続く D 行にはそれぞれ N 個の 10 以上 100, 000 以下の 10 の倍数が書かれている．これらの 数は金額を表わしていて各行に，1 日分ずつ日を追って，店舗番号の順に各店舗の割引き前の予 定価格が書かれている．つまり, 1 ≤ d ≤ D, 1 ≤ n ≤ N のとき, (d + 1) 行目の n 番目の数は第 d 日に店舗番号 n の店舗の金額で割引き無しで購入した場合の予定価格である．</p>

### 출력 

 <p>出力は，標準出力に行うこと．出力は 1 行からなる．最小の合計金額を出力せよ．</p>


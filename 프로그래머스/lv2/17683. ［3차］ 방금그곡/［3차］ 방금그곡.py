def solution(m, musicinfos):
    m=parseMelody(m)
    answer = '(None)'
    answerLength=0
    for info in musicinfos:
        startTime, endTime, musicName, melody= info.split(',')
        songLength= timeToMinute(endTime) - timeToMinute(startTime)
        melody=parseMelody(melody)
        if m in getFullSong(melody, songLength) and songLength>answerLength:
            answer=musicName
            answerLength=songLength
    return answer

def timeToMinute(time):
    h,m=map(int,time.split(':'))
    return 60*h+m

def getFullSong(melody, length):
    temp=""
    while len(temp)<length: temp+=melody
    return temp[:length]

def parseMelody(melody):
    return melody.replace('C#','H').replace('D#','I').replace("F#",'J').replace('A#','K').replace('G#','L')
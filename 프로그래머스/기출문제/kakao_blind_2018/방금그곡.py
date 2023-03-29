def solution(m, musicinfos):
    answer = ''

    for music in musicinfos:
        start, end, title, melody = music.split(',')
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        time = (end_h - start_h) * 60 + (end_m - start_m)
        print('time', time)
        melody = melody.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        melody = list(melody)
        melody = melody * (time // len(melody)) + melody[:time % len(melody)]
        melody = ''.join(melody)
        print('melody', melody)

        m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        print('m', m)
        if m in melody:
            answer += title

    if answer == '':
        answer = '(None)'


    return answer


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))

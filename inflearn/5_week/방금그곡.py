def get_music_time(music_start, music_end):
    music_start_split = music_start.split(':')
    music_end_split = music_end.split(':')
    if music_start_split[0] == music_end_split[0]:
        return int(music_end_split[1]) - int(music_start_split[1])
    else:
        return (60 * music_end_split[0] + music_end_split[1]) - (60 * music_start_split[0] + music_start_split[1])

def get_melody_replaced(m):
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    return m

def solution(m, musicinfos):
    result_list = []
    for music in musicinfos:
        music_split = music.split(',')

        music_start = music_split[0]
        music_end = music_split[1]
        music_title = music_split[2]
        music_melody = music_split[3]

        music_time = get_music_time(music_start, music_end)
        print("music_time: ", music_time)

        music_melody = get_melody_replaced(music_melody)
        music_melody = music_melody * (music_time // len(music_melody)) + music_melody[:music_time % len(music_melody)]
        print(music_melody)

        m = get_melody_replaced(m)
        if m in music_melody:
            result_list.append(music_title)

    print("result_list", result_list)
    result_list.sort(key=lambda x: (len(x), x))
    if len(result_list) != 0:
        answer = result_list[0]
    else:
        answer = '(None)'


    return answer

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print("----------")
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print("----------")
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))

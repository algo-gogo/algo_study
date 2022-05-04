def solution(S):
    S += "\n"
    replace = S.replace("\n", ",")
    split = replace.split(",")
    print(split)
    photo_list = []
    photo = []
    for index, value in enumerate(split):
        if index % 3 == 0 and index != 0:
            photo_list.append(photo)
            photo = []
        remove_blank_value = value.strip()
        photo.append(remove_blank_value)

    print(photo_list)
    photo_dic = {}
    for index, photo in enumerate(photo_list):
        photo.append(index)
        photo_dic[photo[1]] = 0
        # print(photo)

    photo_list.sort(key=lambda x: x[2])

    for index, photo in enumerate(photo_list):
        photo_dic[photo[1]] += 1
        photo.append(photo_dic[photo[1]])

    print(photo_list)
    print(photo_dic)

    result_list = ["" for _ in range(len(photo_list))]

    for index, photo in enumerate(photo_list):
        result_index = photo[3]
        photo__split = photo[0].split(".")
        extension = photo__split[1]

        # if photo_dic[photo[1]] >= 10:
        #     if photo[4] != 10:
        #         photo[4] = '0' + str(photo[4])
        # if len(str(photo[4])) != len(str(photo_dic[photo[1]])):
        #     photo[4] = '0' * (len(str(photo_dic[photo[1]])) - 1) + str(photo[4])
        # else:
        #     photo[4] = str(photo[4])
        if len(str(photo[4])) != len(str(photo_dic[photo[1]])):
            length = len(str(photo_dic[photo[1]])) - len(str(photo[4]))
            photo[4] = '0' * length + str(photo[4])
        else:
            photo[4] = str(photo[4])

        new_photo_name = photo[1] + str(photo[4]) + "." + extension
        result_list[result_index] = new_photo_name

    # print("result_list", result_list)

    result = ''
    for index, value in enumerate(result_list):
        if index != len(result_list) - 1:
            result += value + "\n"
        else:
            result += value

    return result.strip()


print(solution("photo.jpg, Warsaw, 2013-09-05 14:08:15\n"
               "john.png, London, 2015-06-20 15:13:22\n"
               "myFriends.png, Warsaw, 2013-09-05 14:07:13\n"
               "Eiffel.jpg, Paris, 2015-07-23 08:03:02\n"
               "pisatower.jpg, Paris, 2015-07-22 23:59:59\n"
               "BOB.jpg, London, 2015-08-05 00:02:03\n"
               "notredame.png, Paris, 2015-09-01 12:00:00\n"
               "me.jpg, Warsaw, 2013-09-06 15:40:22\n"
               "a.png, Warsaw, 2016-02-13 13:33:50\n"
               "b.jpg, Warsaw, 2016-01-02 15:12:22\n"
               "c.jpg, Warsaw, 2016-01-02 14:34:30\n"
               "d.jpg, Warsaw, 2016-01-02 15:15:01\n"
               "e.png, Warsaw, 2016-01-02 09:49:09\n"
               "f.png, Warsaw, 2016-01-02 10:55:32\n"
               "g.jpg, Warsaw, 2016-02-29 22:13:11\n""photo.jpg, Warsaw, 2013-09-05 14:08:15\n"
               "john.png, London, 2015-06-20 15:13:22\n"
               "myFriends.png, Warsaw, 2013-09-05 14:07:13\n"
               "Eiffel.jpg, Paris, 2015-07-23 08:03:02\n"
               "pisatower.jpg, Paris, 2015-07-22 23:59:59\n"
               "BOB.jpg, London, 2015-08-05 00:02:03\n"
               "notredame.png, Paris, 2015-09-01 12:00:00\n"
               "me.jpg, Warsaw, 2013-09-06 15:40:22\n"
               "a.png, Warsaw, 2016-02-13 13:33:50\n"
               "b.jpg, Warsaw, 2016-01-02 15:12:22\n"
               "c.jpg, Warsaw, 2016-01-02 14:34:30\n"
               "d.jpg, Warsaw, 2016-01-02 15:15:01\n"
               "e.png, Warsaw, 2016-01-02 09:49:09\n"
               "f.png, Warsaw, 2016-01-02 10:55:32\n"
               "g.jpg, Warsaw, 2016-02-29 22:13:11\n""photo.jpg, Warsaw, 2013-09-05 14:08:15\n"
               "john.png, London, 2015-06-20 15:13:22\n"
               "myFriends.png, Warsaw, 2013-09-05 14:07:13\n"
               "Eiffel.jpg, Paris, 2015-07-23 08:03:02\n"
               "pisatower.jpg, Paris, 2015-07-22 23:59:59\n"
               "BOB.jpg, London, 2015-08-05 00:02:03\n"
               "notredame.png, Paris, 2015-09-01 12:00:00\n"
               "me.jpg, Warsaw, 2013-09-06 15:40:22\n"
               "a.png, Warsaw, 2016-02-13 13:33:50\n"
               "b.jpg, Warsaw, 2016-01-02 15:12:22\n"
               "c.jpg, Warsaw, 2016-01-02 14:34:30\n"
               "d.jpg, Warsaw, 2016-01-02 15:15:01\n"
               "e.png, Warsaw, 2016-01-02 09:49:09\n"
               "f.png, Warsaw, 2016-01-02 10:55:32\n"
               "g.jpg, Warsaw, 2016-02-29 22:13:11\n""photo.jpg, Warsaw, 2013-09-05 14:08:15\n"
               "john.png, London, 2015-06-20 15:13:22\n"
               "myFriends.png, Warsaw, 2013-09-05 14:07:13\n"
               "Eiffel.jpg, Paris, 2015-07-23 08:03:02\n"
               "pisatower.jpg, Paris, 2015-07-22 23:59:59\n"
               "BOB.jpg, London, 2015-08-05 00:02:03\n"
               "notredame.png, Paris, 2015-09-01 12:00:00\n"
               "me.jpg, Warsaw, 2013-09-06 15:40:22\n"
               "a.png, Warsaw, 2016-02-13 13:33:50\n"
               "b.jpg, Warsaw, 2016-01-02 15:12:22\n"
               "c.jpg, Warsaw, 2016-01-02 14:34:30\n"
               "d.jpg, Warsaw, 2016-01-02 15:15:01\n"
               "e.png, Warsaw, 2016-01-02 09:49:09\n"
               "f.png, Warsaw, 2016-01-02 10:55:32\n"
               "g.jpg, Warsaw, 2016-02-29 22:13:11\n""photo.jpg, Warsaw, 2013-09-05 14:08:15\n"
               "john.png, London, 2015-06-20 15:13:22\n"
               "myFriends.png, Warsaw, 2013-09-05 14:07:13\n"
               "Eiffel.jpg, Paris, 2015-07-23 08:03:02\n"
               "pisatower.jpg, Paris, 2015-07-22 23:59:59\n"
               "BOB.jpg, London, 2015-08-05 00:02:03\n"
               "notredame.png, Paris, 2015-09-01 12:00:00\n"
               "me.jpg, Warsaw, 2013-09-06 15:40:22\n"
               "a.png, Warsaw, 2016-02-13 13:33:50\n"
               "b.jpg, Warsaw, 2016-01-02 15:12:22\n"
               "c.jpg, Warsaw, 2016-01-02 14:34:30\n"
               "d.jpg, Warsaw, 2016-01-02 15:15:01\n"
               "e.png, Warsaw, 2016-01-02 09:49:09\n"
               "f.png, Warsaw, 2016-01-02 10:55:32\n"
               "g.jpg, Warsaw, 2016-02-29 22:13:11\n""photo.jpg, Warsaw, 2013-09-05 14:08:15\n"
               "john.png, London, 2015-06-20 15:13:22\n"
               "myFriends.png, Warsaw, 2013-09-05 14:07:13\n"
               "Eiffel.jpg, Paris, 2015-07-23 08:03:02\n"
               "pisatower.jpg, Paris, 2015-07-22 23:59:59\n"
               "BOB.jpg, London, 2015-08-05 00:02:03\n"
               "notredame.png, Paris, 2015-09-01 12:00:00\n"
               "me.jpg, Warsaw, 2013-09-06 15:40:22\n"
               "a.png, Warsaw, 2016-02-13 13:33:50\n"
               "b.jpg, Warsaw, 2016-01-02 15:12:22\n"
               "c.jpg, Warsaw, 2016-01-02 14:34:30\n"
               "d.jpg, Warsaw, 2016-01-02 15:15:01\n"
               "e.png, Warsaw, 2016-01-02 09:49:09\n"
               "f.png, Warsaw, 2016-01-02 10:55:32\n"
               "g.jpg, Warsaw, 2016-02-29 22:13:11\n""photo.jpg, Warsaw, 2013-09-05 14:08:15\n"
               "john.png, London, 2015-06-20 15:13:22\n"
               "myFriends.png, Warsaw, 2013-09-05 14:07:13\n"
               "Eiffel.jpg, Paris, 2015-07-23 08:03:02\n"
               "pisatower.jpg, Paris, 2015-07-22 23:59:59\n"
               "BOB.jpg, London, 2015-08-05 00:02:03\n"
               "notredame.png, Paris, 2015-09-01 12:00:00\n"
               "me.jpg, Warsaw, 2013-09-06 15:40:22\n"
               "a.png, Warsaw, 2016-02-13 13:33:50\n"
               "b.jpg, Warsaw, 2016-01-02 15:12:22\n"
               "c.jpg, Warsaw, 2016-01-02 14:34:30\n"
               "d.jpg, Warsaw, 2016-01-02 15:15:01\n"
               "e.png, Warsaw, 2016-01-02 09:49:09\n"
               "f.png, Warsaw, 2016-01-02 10:55:32\n"
               "g.jpg, Warsaw, 2016-02-29 22:13:11\n""photo.jpg, Warsaw, 2013-09-05 14:08:15\n"
               "john.png, London, 2015-06-20 15:13:22\n"
               "myFriends.png, Warsaw, 2013-09-05 14:07:13\n"
               "Eiffel.jpg, Paris, 2015-07-23 08:03:02\n"
               "pisatower.jpg, Paris, 2015-07-22 23:59:59\n"
               "BOB.jpg, London, 2015-08-05 00:02:03\n"
               "notredame.png, Paris, 2015-09-01 12:00:00\n"
               "me.jpg, Warsaw, 2013-09-06 15:40:22\n"
               "a.png, Warsaw, 2016-02-13 13:33:50\n"
               "b.jpg, Warsaw, 2016-01-02 15:12:22\n"
               "c.jpg, Warsaw, 2016-01-02 14:34:30\n"
               "d.jpg, Warsaw, 2016-01-02 15:15:01\n"
               "e.png, Warsaw, 2016-01-02 09:49:09\n"
               "f.png, Warsaw, 2016-01-02 10:55:32\n"
               "g.jpg, Warsaw, 2016-02-29 22:13:11\n""photo.jpg, Warsaw, 2013-09-05 14:08:15\n"
               "john.png, London, 2015-06-20 15:13:22\n"
               "myFriends.png, Warsaw, 2013-09-05 14:07:13\n"
               "Eiffel.jpg, Paris, 2015-07-23 08:03:02\n"
               "pisatower.jpg, Paris, 2015-07-22 23:59:59\n"
               "BOB.jpg, London, 2015-08-05 00:02:03\n"
               "notredame.png, Paris, 2015-09-01 12:00:00\n"
               "me.jpg, Warsaw, 2013-09-06 15:40:22\n"
               "a.png, Warsaw, 2016-02-13 13:33:50\n"
               "b.jpg, Warsaw, 2016-01-02 15:12:22\n"
               "c.jpg, Warsaw, 2016-01-02 14:34:30\n"
               "d.jpg, Warsaw, 2016-01-02 15:15:01\n"
               "e.png, Warsaw, 2016-01-02 09:49:09\n"
               "f.png, Warsaw, 2016-01-02 10:55:32\n"
               "g.jpg, Warsaw, 2016-02-29 22:13:11\n""photo.jpg, Warsaw, 2013-09-05 14:08:15\n"
               "john.png, London, 2015-06-20 15:13:22\n"
               "myFriends.png, Warsaw, 2013-09-05 14:07:13\n"
               "Eiffel.jpg, Paris, 2015-07-23 08:03:02\n"
               "pisatower.jpg, Paris, 2015-07-22 23:59:59\n"
               "BOB.jpg, London, 2015-08-05 00:02:03\n"
               "notredame.png, Paris, 2015-09-01 12:00:00\n"
               "me.jpg, Warsaw, 2013-09-06 15:40:22\n"
               "a.png, Warsaw, 2016-02-13 13:33:50\n"
               "b.jpg, Warsaw, 2016-01-02 15:12:22\n"
               "c.jpg, Warsaw, 2016-01-02 14:34:30\n"
               "d.jpg, Warsaw, 2016-01-02 15:15:01\n"
               "e.png, Warsaw, 2016-01-02 09:49:09\n"
               "f.png, Warsaw, 2016-01-02 10:55:32\n"
               "g.jpg, Warsaw, 2016-02-29 22:13:11\n""photo.jpg, Warsaw, 2013-09-05 14:08:15\n"
               "john.png, London, 2015-06-20 15:13:22\n"
               "myFriends.png, Warsaw, 2013-09-05 14:07:13\n"
               "Eiffel.jpg, Paris, 2015-07-23 08:03:02\n"
               "pisatower.jpg, Paris, 2015-07-22 23:59:59\n"
               "BOB.jpg, London, 2015-08-05 00:02:03\n"
               "notredame.png, Paris, 2015-09-01 12:00:00\n"
               "me.jpg, Warsaw, 2013-09-06 15:40:22\n"
               "a.png, Warsaw, 2016-02-13 13:33:50\n"
               "b.jpg, Warsaw, 2016-01-02 15:12:22\n"
               "c.jpg, Warsaw, 2016-01-02 14:34:30\n"
               "d.jpg, Warsaw, 2016-01-02 15:15:01\n"
               "e.png, Warsaw, 2016-01-02 09:49:09\n"
               "f.png, Warsaw, 2016-01-02 10:55:32\n"
               "g.jpg, Warsaw, 2016-02-29 22:13:11\n""photo.jpg, Warsaw, 2013-09-05 14:08:15\n"
               "john.png, London, 2015-06-20 15:13:22\n"
               "myFriends.png, Warsaw, 2013-09-05 14:07:13\n"
               "Eiffel.jpg, Paris, 2015-07-23 08:03:02\n"
               "pisatower.jpg, Paris, 2015-07-22 23:59:59\n"
               "BOB.jpg, London, 2015-08-05 00:02:03\n"
               "notredame.png, Paris, 2015-09-01 12:00:00\n"
               "me.jpg, Warsaw, 2013-09-06 15:40:22\n"
               "a.png, Warsaw, 2016-02-13 13:33:50\n"
               "b.jpg, Warsaw, 2016-01-02 15:12:22\n"
               "c.jpg, Warsaw, 2016-01-02 14:34:30\n"
               "d.jpg, Warsaw, 2016-01-02 15:15:01\n"
               "e.png, Warsaw, 2016-01-02 09:49:09\n"
               "f.png, Warsaw, 2016-01-02 10:55:32\n"
               "g.jpg, Warsaw, 2016-02-29 22:13:11\n""photo.jpg, Warsaw, 2013-09-05 14:08:15\n"
               "john.png, London, 2015-06-20 15:13:22\n"
               "myFriends.png, Warsaw, 2013-09-05 14:07:13\n"
               "Eiffel.jpg, Paris, 2015-07-23 08:03:02\n"
               "pisatower.jpg, Paris, 2015-07-22 23:59:59\n"
               "BOB.jpg, London, 2015-08-05 00:02:03\n"
               "notredame.png, Paris, 2015-09-01 12:00:00\n"
               "me.jpg, Warsaw, 2013-09-06 15:40:22\n"
               "a.png, Warsaw, 2016-02-13 13:33:50\n"
               "b.jpg, Warsaw, 2016-01-02 15:12:22\n"
               "c.jpg, Warsaw, 2016-01-02 14:34:30\n"
               "d.jpg, Warsaw, 2016-01-02 15:15:01\n"
               "e.png, Warsaw, 2016-01-02 09:49:09\n"
               "f.png, Warsaw, 2016-01-02 10:55:32\n"
               "g.jpg, Warsaw, 2016-02-29 22:13:11"))
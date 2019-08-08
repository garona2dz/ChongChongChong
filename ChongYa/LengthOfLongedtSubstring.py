def length_of_longest_substring(s):  # 时间和空间都很差，只是个粗暴的解法
    count = 1
    length = len(s)

    if length == 0:
        print(0)
        return 0

    for i in range(length):
        string = s[i]
        for j in range(i + 1, length):
            check = string.find(s[j])
            if check >= 0:
                break
            else:
                string += s[j]
                str_len = len(string)
                if str_len > count:
                    count = str_len
                    # print(string)

    print(count)
    return count
    # return count


ss = 'pwwkew'
length_of_longest_substring(ss)

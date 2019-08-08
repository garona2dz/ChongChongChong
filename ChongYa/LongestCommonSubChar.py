def longestcommonprefix(strs):  # 这是再找字符串里最长的共有子字符串，和leetcode上的共有前缀不一样

    list_str = []
    com_str = ''
    count = 0
    min_len = len(strs[0]) if len(strs) > 0 else -1
    min_str = ''
    for string in strs:
        str_len = len(string)
        if str_len <= min_len:
            min_len = str_len
            min_str = string

    if min_len == -1 or min_len == 0:
        return ''

    for start in range(min_len):
        for i in range(start + 1, min_len + 1):
            for strings in strs:
                if min_str[start:i:1] not in strings:
                    count += 1
                    break
            if count == 0:
                if len(min_str[start:i:1]) > len(com_str):
                    com_str = min_str[start:i:1]
                    list_str = [com_str]
                if len(min_str[start:i:1]) == len(com_str) and min_str[start:i:1] != com_str:
                    com_str = min_str[start:i:1]
                    list_str.append(com_str)
            count = 0
        if start == min_len:
            break

    print(com_str)
    print(list_str)
    return com_str


longestcommonprefix(['sssadffffaaa', 'aaadffffsdqsssjkljl', 'aaasgffffhfsssjlkjk'])

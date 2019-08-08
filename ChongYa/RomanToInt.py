# 使用字典
# 很厉害的解法

# d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
#
# def romanToInt(self, s):
#     res, p = 0, 'I'
#     for c in s[::-1]:
#         res, p = res - d[c] if d[c] < d[p] else res + d[c], c
#     return res


def romantoint(s):  # 很low的解发
    result = 0
    in_list = list(s)
    while True:
        if 'M' in in_list:
            m_pos = in_list.index('M')
            if m_pos == 0:
                result += 1000
                del in_list[m_pos]
            else:
                if in_list[m_pos - 1] == 'C':
                    result += 900
                    del in_list[m_pos]
                    del in_list[m_pos - 1]
                else:
                    result += 1000
        else:
            break

    while True:
        if 'D' in in_list:
            m_pos = in_list.index('D')
            if m_pos == 0:
                result += 500
                del in_list[m_pos]
            else:
                if in_list[m_pos - 1] == 'C':
                    result += 400
                    del in_list[m_pos]
                    del in_list[m_pos - 1]
                else:
                    result += 500
        else:
            break

    while True:
        if 'C' in in_list:
            m_pos = in_list.index('C')
            if m_pos == 0:
                result += 100
                del in_list[m_pos]
            else:
                if in_list[m_pos - 1] == 'X':
                    result += 90
                    del in_list[m_pos]
                    del in_list[m_pos - 1]
                else:
                    result += 100
        else:
            break

    while True:
        if 'L' in in_list:
            m_pos = in_list.index('L')
            if m_pos == 0:
                result += 50
                del in_list[m_pos]
            else:
                if in_list[m_pos - 1] == 'X':
                    result += 40
                    del in_list[m_pos]
                    del in_list[m_pos - 1]
                else:
                    result += 50
        else:
            break

    while True:
        if 'X' in in_list:
            m_pos = in_list.index('X')
            if m_pos == 0:
                result += 10
                del in_list[m_pos]
            else:
                if in_list[m_pos - 1] == 'I':
                    result += 9
                    del in_list[m_pos]
                    del in_list[m_pos - 1]
                else:
                    result += 10
        else:
            break

    while True:
        if 'V' in in_list:
            m_pos = in_list.index('V')
            if m_pos == 0:
                result += 5
                del in_list[m_pos]
            else:
                if in_list[m_pos - 1] == 'I':
                    result += 4
                    del in_list[m_pos]
                    del in_list[m_pos - 1]
                else:
                    result += 5
        else:
            break

    while True:
        if 'I' in in_list:
            m_pos = in_list.index('I')
            result += 1
            del in_list[m_pos]
        else:
            break

    print(result)
    return result

romantoint('MCMXCVII')
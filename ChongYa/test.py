global count


def plusone(digits):
    count = 0

    if len(digits) == 0:
        result = [1]
        result.extend([0] * count)
        print(result)
        return result

    if digits[len(digits) - 1] < 9:
        digits[len(digits) - 1] += 1
        if count > 0:
            detail = [0] * count
            digits.extend(detail)
            print(digits)
            return digits
        else:
            print(digits)
            return digits
    else:
        # new_digits = [0]*(len(digits) + 1)
        del digits[len(digits) - 1]
        count += 1
        print(digits)
        plusone(digits)


x = [1, 2, 9]
plusone(x)
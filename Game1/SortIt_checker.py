def check(pos, num):
    ''' check if player`s answer was correct'''
    if(0 <= pos <= 150):
        return prime_check(num)
    elif (151 <= pos <= 303):
        return happy_check(num)
    elif (304 <= pos <= 456):
        return ulam_check(num)
    else:
        if (prime_check(num) or happy_check(num) or ulam_check(num)):
            return False
        else:
            return True


def prime_check(num):
    """(int) -> bool
    Returns True, if number is prime, else False
    """
    if (num % 2 == 0 and num != 2) or num == 1:
        return False
    for i in range(3, num, 2):
        if num % i == 0:
            return False
    return True

def happy_check(num):
    """(int) -> bool
    Returns True, if number is happy, else False
    """
    def list_of_digits(number):
        """(int) -> list
        Returns digit on <i> position
        <0> positions is first digit on the left  
        """
        leng = len(str(sum))
        res = []
        for i in range(leng):
            if i == 0:
                res.append((number % 10))
            else:
                res.append((number % (10**(i + 1))) // 10**(i))
        return res

    summ = num
    iterations = []

    while True:
        sum1 = 0
        digits = list_of_digits(summ)
        for i in range(len(digits)):
            sum1 += digits[i]**2
        
        iterations.append(sum1)
        summ = sum1

        if len(iterations) != len(set(iterations)):
            return False
        if sum1 == 1:
            return True

def ulam_check(num):
    '''check if number is ulam`s one'''
    ulam_list = [0]*2
    ulam_list[0] = 1
    ulam_list[1] = 2
    number_of_numbers = 2
    if num == 1 or num == 2:
        return True
    for i in range(3, 100):
        k = 0
        for j in range(number_of_numbers):
            q = j+1
            while q < number_of_numbers:
                if ulam_list[j] + ulam_list[q] == i:
                    k+=1
                if k ==2:
                    break
                q+=1
        if k == 1:
            ulam_list.append(i)
            number_of_numbers+=1
            if (i == num):
                return True
    return False
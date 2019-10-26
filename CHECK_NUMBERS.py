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
     
        
            
 



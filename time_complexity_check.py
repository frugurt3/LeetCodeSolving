# -*- coding: utf-8 -*-
import timeit
import statistics

other = '''
    num = "1000000000000"
    def toHexspeak(num: str) -> str:
        valid_digits = {0: "O", 1:"I", 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
        num_in_int = int(num)
        res = ""
        while num_in_int:
            q, r = divmod(num_in_int, 16)
            if r not in valid_digits:
                return "ERROR"
            else:
                res = valid_digits[r] + res
            num_in_int = q
        return res
    toHexspeak(num)
    '''

my = '''
num = "1000000000000"
def toHexspeak(num):
    """
    :type num: str
    :rtype: str
    """

    check = {'a':"A", 'b':"B", 'c':"C", 'd':"D", 'e':"E", 'f':"F", '1':"I", '0':"O"}
    result = ''

    for char in hex(int(num))[2:]: 
        try:
            result = ''.join((result,check[char]))
        except:
            return 'ERROR'
    return result
toHexspeak(num)
'''

my_results = []
other_result = []
iterations = 50

for i in range(iterations):
    solution_my, solution_other = timeit.timeit(my, number=100000), timeit.timeit(other, number=100000)
    my_results.append(solution_my)
    other_result.append(solution_other)
    iterations -= 1
    print(iterations)

solution_my = statistics.mean(my_results)
solution_other = statistics.mean(other_result)

print('my')
print(solution_my)
print('other')
print(solution_other)

if solution_my < solution_other:
    print('my solution faster than other solution on (%):')
    print(100.0 - (solution_my * 100.0) / solution_other)
else:
    print('other faster than my solution on (%):')
    print(100.0 - (solution_other * 100.0) / solution_my)

#
# # def mul_nums(num_1, num_2, num_3):
# def mul_nums(num_1, num_2, num_3=10, results=[]):
#     print(f'num_1={num_1}')
#     print(f'num_2={num_2}')
#     print(f'num_3={num_3}')
#     result = num_1 * num_2 * num_3
#     results.append(result)
#     return results
#
#
# # res = mul_nums(num_1=1, num_3=2, num_2=3)
# # res = mul_nums(1, 2)
# # print(res)
# results = [0, 0, 0, 0]
# print(mul_nums(1, 2, num_3=3, results=results))
# print(mul_nums(1, 2))
# print(mul_nums(1, 2, num_3=3))

# my_lambda = lambda num_1, num_2, num_3: num_1 * num_2 * num_3
# print(my_lambda(1, 2, 3))
#num_1 = int(input('Write a number of copy: '))
# for el in range(15, 5, -1):
#     print(el)

# def mul_nums(num_1, num_2, num_3):
# def mul_nums(num_1, num_2, num_3):
#
#     def _inner():
#         nonlocal result
#         pass
#
#     global number_1
#     result = num_1 * num_2 * num_3
#     print(f'global number_1={number_1}')
#     return result
#
# number_1 = 10
# print(mul_nums(1, 2, 3))
# print(number_1)


def mul_nums(num_1, num_2, num_3):
    """Multiply 3 numbers

    :param num_1: int, float
    :param num_2: int, float
    :param num_3: int, float
    :return: int, float
    """
    result = num_1 * num_2 * num_3
    return result

mul_nums(1, 2, 3)
print(mul_nums.__doc__)
print(mul_nums(1, 2, 3))
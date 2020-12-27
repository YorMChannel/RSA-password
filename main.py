import random
import math

class SameNumError(Exception): 
    def __init__(self):
        pass

def is_prime_number(n): 
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def make_prime_list(n):
    prime_list = []
    for i in range(2, n):
        if math.gcd(n, i) == 1: 
            prime_list.append(i)
    return prime_list

def input_prime_number(i): 
    n = input("소수를 입력해주세요. : ")
    try:
        n = int(n)
        if n < 3 or not is_prime_number(n):
            raise ValueError
        elif n == i:
            raise SameNumError
    except ValueError:
        print("입력된 값이 소수가 아닙니다.")
        n = input_prime_number(i)
    except SameNumError:
        print("입력된 값이 이전 수와 같습니다.")
        n = input_prime_number(i)
    return n

def get_d(e, oil):
    for d in range(0, oil):
        if (e * d) % oil == 1:
            break
    return d

def input_number(max_num):
    n = input("정수를 입력해주세요.( 단, 처음 두 소수의 곱보다 작은 수여야 합니다. ) : ")
    try:
        n = int(n)
        if n >= max_num:
            raise ValueError
    except Exception:
        print("입력한 값이 잘못되었습니다.")
        n = input_number(max_num)
    return n

p = input_prime_number(0)
q = input_prime_number(p)
n = p * q
oil = (p - 1) * (q - 1)
prime_list = make_prime_list(oil)
random.shuffle(prime_list)
e = prime_list[0]
d = get_d(e, oil)
# print(p, q, n, oil, prime_list, e, d)
contents = input_number(n)
password = (contents ** e) % n
print("==============================")
print("공개키 : (n = {}, d = {})".format(n, d))
print("개인키 : (n = {}, e = {})".format(n, e))
print("암호화 된 값 : {}".format(password))
print("==============================")
while True:
    text = input()
    if text == "next":
        answer = (password ** d) % n
        print("==============================")
        print("복호화 된 값 : {}".format(answer))
        print("==============================")
        break
input()
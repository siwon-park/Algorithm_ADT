# 최대 공약수, 최소 공배수 구하기(유클리드 호재법)
# math모듈로 최대 공약수(math.gcd), 최소 공배수(math.lcm)을 구할 순 있으나, 해당 방법을 알아두기 위해 기록함
# 참고) math모듈의 lcm메서드는 3.9버전부터 추가되었음

# 최대 공약수
# a에는 b값을 대입하고, b에는 a%b(나머지)를 대입하면서 나머지가 0이 되는 순간의 b값(a가 됨)이 최소 공배수가 됨
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소 공배수
# 두 수를 곱한 값을 두 수의 최소 공약수로 나눈 몫이 두 수의 최소 공배수임(가끔 블로그 찾다보면 a*b/gcd(a, b)로 표현한 사람들이 있는데 이는 틀렸음)
def lcm(a, b):
    return a * b // gcd(a, b)

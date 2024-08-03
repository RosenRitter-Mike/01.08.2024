import random as rnd
import statistics as st

numbers: list[int] = [rnd.randint(-50, 50) for _ in range(20)];
print(numbers);
# a
print('map x ** 3', list(map(lambda x: x ** 3, numbers)));
# b
print('map x % 10', list(map(lambda x: x % 10, numbers)));
# c
print('map fahrenheit', list(map(lambda x: x * 9/5 + 32, numbers)));
# d
print('map positive/negative', list(map(lambda x: "negative" if x < 0 else "positive", numbers)));
# e
print('map min/max', list(map(lambda x: "max" if x == max(numbers) else "min" if x == min(numbers) else x, numbers)));


# f
def reverse_dig(num: int) -> int:
    if -10 < num < 10:
        return num;
    else:
        sign: int = 1;
        if num < 0:
            num = -num;
            sign = -1;
        num = num//10 + 10*(num%10);
        return sign*num;


print('map reverse digits', list(map(lambda x: reverse_dig(x), numbers)));


# g
print('map absolute value', list(map(lambda x: abs(x), numbers)));

# h
inc_exp: list[list] = [[rnd.randint(100, 1000), rnd.randint(100, 1000)] for _ in range(10)];
print(inc_exp);
print('map profit expenditure', list(map(lambda x: x[1] - x[0], inc_exp)));

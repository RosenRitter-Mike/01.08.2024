import random as rnd
import statistics as st

numbers: list[int] = [rnd.randint(1, 100) for _ in range(50)];
print(numbers);
# a
print("filter > 50", list(filter(lambda x: x > 50, numbers)));
# b
print("filter 7 boom", list(filter(lambda x: x % 7 == 0, numbers)));
# c
print("filter 10 < x < 99", list(filter(lambda x: 10 < x < 99, numbers)));
# d
print("filter same digit", list(filter(lambda x: x // 10 == x % 10, numbers)));
# e
print("filter sum of digits  = 9", list(filter(lambda x: x // 10 + x % 10 == 9, numbers)));
# f
print("filter larger then mean value", list(filter(lambda x: x > st.mean(numbers), numbers)));
# g
print("filter over the half max", list(filter(lambda x: x > max(numbers), numbers)));
# h
print("filter larger then median value", list(filter(lambda x: x > st.median(numbers), numbers)));

# i
num_in: list[int] = [];
while len(num_in) < 5:
    try:
        num_in.append(int(input("input an integer: ")));

    except:
        print("invalid input");
        continue;

print("filter not in input list", list(filter(lambda x: x not in num_in, numbers)));


# j
def is_primary(a: int) -> bool:
    for i in range(2, a):
        if not a % i:
            return False;
    return True;


print("filter only primary", list(filter(lambda x: is_primary(x), numbers)));

fruit: list[str] = ["Apple", "Banana", "Orange", "Mango","Strawberry", "Pineapple", "Grapes", "Watermelon"];
# a
print('map fruit reverse', list(map(lambda x: x[::-1], fruit)));
# b
print('map fruit first letter', list(map(lambda x: x[0], fruit)));
# c
print('map fruit upper', list(map(lambda x: x.upper(), fruit)));
# d
print('map fruit len', list(map(lambda x: len(x), fruit)));
# e
print('map fruit reverse', list(map(lambda x: x+"!" if x[len(x)-1] == "s" else x, fruit)));
# f
fruit_cal: list[list] = [["Banana", 89], ["Orange", 47], ["Mango", 60], ["Strawberry", 32],["Pineapple", 50], ["Grapes", 69]
    , ["Watermelon", 30]];
cal: list[int] = list(map(lambda x: x[1], fruit_cal));
print(cal);

fru_c: list[str] = list(map(lambda x: x[0]+str(x[1]), fruit_cal));
print(fru_c);

fruit_cal1: list[list] = list(map(lambda x: [x[0]+"!", x[1]] if x[1] > 50 else x, fruit_cal));
print(fruit_cal1);


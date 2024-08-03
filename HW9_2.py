game_list: list[str] = ["Grand Theft Auto V","Fortnite", "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"];
# a
print("filter len > 8", list(filter(lambda x: len(x) > 8, game_list)));
# b
print("filter starts with F", list(filter(lambda x: x[0] == "F", game_list)));
# c
print("filter two words", list(filter(lambda x: len(x.split()) == 2, game_list)));
# d
print("filter has a V in its name", list(filter(lambda x: "V" in x, game_list)));


# e
def has_special(s: str) -> bool:
    for c in s:
        if c in "!*&;:^%$#@":
            return True;

    return False;


print("filter has special character in its name", list(filter(lambda x: has_special(x), game_list)));
# print("filter has special character in its name", list(filter(lambda x: not(x.isdigit() or x.isalpha()), game_list)));

# f
game_list_f: list[list] = [["Grand Theft Auto V", 2013],["Fortnite", 2017], ["The Elder Scrolls V: Skyrim", 2011],
                           ["Dark Souls", 2011], ["Overwatch", 2016]];
print("filter made after 2014", list(filter(lambda x: x[1] > 2014, game_list_f)));
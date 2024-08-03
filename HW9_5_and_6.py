cities: list[str] = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"];
# a
print("sorted by name length", sorted(cities, key=lambda city: len(city)));
# b
print("sorted by last letter", sorted(cities, key=lambda city: city[len(city) - 1]));
# c
print("sorted in reverse", sorted(cities, key=lambda city: city, reverse=True));
# d
dist_c: list[list] = [["Tokyo", 5760, "Asia"], ["New York", 5690, "North America"], ["Paris", 2050,"Europe"],
                      ["London", 2240, "Europe"], ["Sydney", 8780, "Australia"], ["Dubai", 1300, "Asia"],
                      ["Shanghai", 4920, "Asia"]];

print("sorted by distance from israel", sorted(dist_c, key=lambda city: city[1]));
print("sorted in reverse by distance from israel", sorted(dist_c, key=lambda city: city[1], reverse=True));
print("sorted by continent", sorted(dist_c, key=lambda city: city[2]));
print("sorted by continent, then distance", sorted(dist_c, key= lambda city: (city[2], city[1])));

# Ex 6

# מה המשמעות שלהמילהglobalבתוך פונקציה?
"""Global variables can be accessed both inside a function and outside, so making somthing global gives accesses to it to
 all regardless of scope. When we create a variable inside a function, it is local by default.
When we define a variable outside of a function, it is global by default. """

# מההחסרון בשימוש ב-globalכחלק מפונקציה? מה זהידרוש בעתיד...
"""
You need to watch the scope as a change can occur in the function that changes the results of your main via the value 
of the global var. So the global x can be changed due to a func gone un noticed, its bad practice.
"""

# מדוע כאן נקבל שגיאה-
# x: int = 1
# def foo():
# print(x)
# x = 4
# foo()

"""
Redefinition of existing var, also you cant modify global vars without the global keyword, the line should be:

global x = 4;

then it should work, any ay global is bad practice and should NEVER be used (NEVER!)
"""


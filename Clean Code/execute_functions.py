from mathfunctions.functions_with_cleancode import (
    lists_to_df,
    my_add,
    my_multiply,
    my_scale,
)

print(my_add(2, 3))
print(my_multiply(3, 4))
#print(my_add("abc", 2.3)) zum testen mit mypy
print(my_scale(2.0, [1,2,3]))
print(lists_to_df([1,2,3], [4,5,6]))
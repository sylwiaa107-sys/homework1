# 1.1. IC3.1 -- Default Argument Pitfall
#
# def add_to(value, target = None):
#     if target is None:
#         target = []
#
#     target.append(value)
#     return target
# print(add_to(1))
# print(add_to(2))
# print(add_to(3))

# None - przy kazdym wywolaniu funkcje tworzy niezalezna liste

# 1.2. IC3.2 -- Function That Returns Another Function (closures)
# def make_multiplier(n):
#     def multiplier(x):
#         return x * n
#     return multiplier
# double = make_multiplier(2)
# triple = make_multiplier(3)
#
# print(double(5))
# print(triple(5))
# print(double(10))
#
#
# def make_validator(min_val, max_val):
#     def is_valid(x):
#         return x >= min_val and x<= max_val
#     return is_valid
#
# is_valid = make_validator(min_val=5, max_val=10)
# print(is_valid(5))
# print(is_valid(10))
# print(is_valid(20))
#

#1.3. IC3.3 -- Variable Args With Type Filtering
# def sum_numerics(*args):
#    total = 0
#    for value in args:
#        if isinstance(value, (int, float)) and not isinstance(value, bool):
#            total += value
#
#    return total
#
# print(sum_numerics(1, 2, 3))
# print(sum_numerics(1, "two", 3.0, None))
# print(sum_numerics())
# print(sum_numerics("a", "b"))


#1.4. IC3.4 -- Function Composition
def compose(*funcs):
    if len(funcs) == 1:
        def identity(x):
            return x
        return identity

    if len(funcs) == 1:
        return funcs[0]


    def composed(x):
        result = x

        for func in reversed(funcs):
            result = func(result)

        return result

    return composed

inc = lambda x: x + 1
double = lambda x: x * 2
square = lambda x: x ** 2
f =compose(inc, double, square)

print(f(55))


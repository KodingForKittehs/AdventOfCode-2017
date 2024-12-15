# pylint: disable=trailing-whitespace, missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import
import kittehs_funkollection as kf

inp = "input"
lines = kf.eat(inp)
s = 0
s2 = 0
for line in lines:
    nums = kf.find_ints(line)
    print(nums)
    s += max(nums) - min(nums)

    for i, n in enumerate(nums):
        for j, m in enumerate(nums):
            if i != j and n % m == 0:
                s2 += n // m

print(f"P1: {s}")
print(f"P2: {s2}")


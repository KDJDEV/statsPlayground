from itertools import permutations, product

# solution output here:
# https://docs.google.com/document/d/1aHuxMp4ZOHi-scfST_xaqA4iz6BFLSLEiuRpNt4ZNl8/edit?tab=t.0

# Given numbers and basic operations
numbers = [1, 2, 4]
operations = ['+', '-', '*', '/']
results = {}
power_range = list(range(0, 6)) + [1/2, 1/3, 2/3, 1/4, 3/4, 1/5, 2/5, 3/5, 4/5, 1/6]  # Include square root, cube root, 4th root, etc.

# Try all permutations of the numbers
for perm in permutations(numbers):
    a, b, c = perm

    # Try all power combinations for individual numbers
    for p1, p2, p3 in product(power_range, repeat=3):
        try:
            a_p, b_p, c_p = f"{a}**{p1}", f"{b}**{p2}", f"{c}**{p3}"

            # Try all possible operations between the three numbers
            for op1, op2 in product(operations, repeat=2):
                expr1 = f"{a_p} {op1} {b_p} {op2} {c_p}"
                expr2 = f"({a_p} {op1} {b_p}) {op2} {c_p}"
                expr3 = f"{a_p} {op1} ({b_p} {op2} {c_p})"

                for expr in [expr1, expr2, expr3]:
                    try:
                        result = eval(expr)
                        if isinstance(result, (int, float)) and (isinstance(result, int) or result.is_integer()):
                            if (int(result) not in results):
                                results[int(result)] = expr
                    except:
                        continue
        except:
            continue

    # Now consider powers of sums (e.g., (a + b)^p) including fractional powers
    for p in power_range:
        for op1, op2 in product(operations, repeat=2):
            try:
                sum1_p = f"({a} {op1} {b}) ** {p}"
                sum2_p = f"({b} {op1} {c}) ** {p}"
                sum3_p = f"({a} {op1} {c}) ** {p}"
                full_sum_p = f"({a} {op1} {b} {op2} {c}) ** {p}"

                # Apply operations to powered sums
                for p2 in power_range:
                    for op in operations:
                        for expr in [
                            f"{sum1_p} {op} ({c} ** {p2})",
                            f"{sum2_p} {op} ({a} ** {p2})",
                            f"{sum3_p} {op} ({b} ** {p2})",
                            f"{full_sum_p}"
                        ]:
                            try:
                                result = eval(expr)
                                if isinstance(result, (int, float)) and (isinstance(result, int) or result.is_integer()):
                                    if (int(result) not in results):
                                        results[int(result)] = expr
                            except:
                                continue
            except:
                continue

# Sort and display results
sorted_results = sorted(results.keys())
for i in range(234256):
    if i + 1 in sorted_results:
        print(f"{i + 1}: {results[i + 1]}")
    else:
        print(f"{i + 1}: No solution")

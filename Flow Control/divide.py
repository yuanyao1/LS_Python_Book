def short_circuit_divide(dividend, divisor):
    result = divisor and (dividend / divisor)

    return result if result else "Division by zero is not allowed"

result1 = short_circuit_divide(10, 2)   # True
result2 = short_circuit_divide(10, 0)   # "Division by zero is not allowed"

print(result1)
print(result2)

result3 = short_circuit_divide(0, 2)   # "Division by zero is not allowed"
print(result3)
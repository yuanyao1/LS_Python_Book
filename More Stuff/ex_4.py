def increment_counter():
    global counter
    counter += 1

counter = 0
print(counter)                # 0
print()

print(increment_counter())
print(counter)                # 1
print()

print(increment_counter())
print(counter)                # 2
print()

counter = 100
print(increment_counter())
print(counter)                # 101

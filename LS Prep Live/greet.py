def greet(name: str = 'Default Name') -> str:
    greeting = "Hello"
    return (f"{greeting}, {name}")

greet()
print(greet())
print(greet("Alice"))


# def greet(name):
#     greeting = "Hello"
#     print(f"{greeting}, {name}")

# greet("Alice")
# print(greeting)
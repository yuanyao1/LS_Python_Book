# integer representing age
# boolean representing if they have permission
# adults aged 18 and older may join otherwise they must have Permission

def can_sign_up(age: int, permission: bool) -> bool:
    if type(age) != int:
        raise TypeError(f'age {age} is not an int type')
    elif type(permission) != bool:
        raise TypeError(f'permission {permission} is not a bool type')
    
    if age < 12:
        return False
    elif age >= 18:
        return True
    else:
        return permission

person1 = can_sign_up(17, False)
print(f"person1 permission status is {person1}")

person2 = can_sign_up(18, False)
print(f"person2 permission status is {person2}")

person4 = can_sign_up(11, True)
print(f"person4 permission status is {person4}")

person3 = can_sign_up('dog', 'cat')
print(f"person3 permission status is {person3}")
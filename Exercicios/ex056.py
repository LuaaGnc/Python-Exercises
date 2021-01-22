count_minor_woman = 0
average_age = 0

for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')

    name = str(input('Name: '))
    age = int(input('Age: '))
    sex = str(input('Sex [M/F]: '))

    average_age += age/4

    # Break if User types a ""Sex"" different than M and F.
    if  sex != 'M' and sex != 'F':
        print('Select one of the above :D ')
        break

    # Saves Man's name and his age.
    elif sex == 'M':
        name_man = name
        age_man = age

        # If his Age now is bigger than the Age saved before, Computer saves this one.
        if age_man < age:
            name_man = name
            age_man = age

    # It counts how many women under 20 years old.
    elif sex == 'F' or age < 20:
        count_minor_woman += 1

print(f'The average age of the group is {average_age} years old!')
print(f'The Oldest man of this group has {age_man} years old and his name is {name_man}!')
print(f'And it has {count_minor_woman} women with less than 20 years old!')

rating = [7, 5, 3, 3, 2]
user_input = ''
while user_input != 'q':
    user_input = input("Input positive integer or q for exit:")
    if user_input == 'q':
        break
    i = 0
    user_num = int(user_input)
    if user_num > max(rating):
        rating.insert(0, user_num)
    elif user_num < min(rating):
        rating.append(user_num)
    elif rating.count(user_num) == 0:
        while user_num < rating[i]:
            i += 1
            if user_num > rating[i]:
                rating.insert(i, user_num)
    else:
        i = rating.index(user_num) + rating.count(user_num)
        rating.insert(i, user_num)
    print(rating)

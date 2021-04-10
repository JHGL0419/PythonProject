import random
users = range(1, 21)
print(users)
listUsers = list(users)
random.shuffle(listUsers)
userSample = random.sample(listUsers, 4)

print(' -- 당첨자 발표 --')
print('치킨 당첨자 : ' + str(userSample[0]))
print('커피 당첨자 : ' + str(userSample[1:]))
print('-- 축하합니다 --')

import random
customer = 0
for i in range(1, 51):
    time = random.randint(5, 50)
    
    if time <= 15:
        a = '[O]'
        customer += 1
    else:
        a = '[ ]'
    print('{0} {1}번쨰 손님 (소요시간 : {2}분)'.format(a,i,time))
print('총 탑승 승객 : {0}'.format(customer))
def std_weight(height, gender):
    if gender == '남자' or '남성':
        return height/100 * height/100 * 22

    if gender == '여자' or '여성':
        return height/100 * height/100 * 21
        
height = int(input())
gender = input()

print("키 %dcm %s의 표준 체중은 %.2fkg 입니다."%(height, gender, std_weight(height, gender)))

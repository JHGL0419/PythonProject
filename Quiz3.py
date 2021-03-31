# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

url = input('url : ')
rule1 = url.replace('http://', '') # or url[:7]

rule2 = rule1[:rule1.index('.')]

rule3 = rule2[:3] + str(len(rule2)) + str(rule2.count('e')) + '!'


print(f'{url}의 비밀번호는 {rule3}입니다.') # or print('생성된 비밀번호 : ' + rule3)
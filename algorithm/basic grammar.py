# print(abs(-5)) # 5 절대값
# print(pow(4,2)) #->16  제곱
# print(max(5,12)) #12 최댓값
# round(3.14)  #반올림
#
# from math import *
# floor(4.99) #4 - 내림
# ceil(3.14) # 4 - 올림
# sqrt(16) # 4 - 루트
#
# #랜덤함수
# from random import *
#
# print(random())  # 0.0~1.0 미만의 임의의 값 생성
# print(random()*10) #0.0~ 10.0 미만의 임의의 값 생성
# print(int(random()*10)) #0~10 미만의 임의의 값
# print(int(random()*45)+1) #0~45 이하의 임의의 값 생성
#
# print(randrange(1, 46)) # 1~ 46 미만의 임의의 값 생성
#
# print(randint(1, 45)) # 1~45 이하의 임의의 값 생성
#
#
#
# python = " Python is Amazing"
#
# print(python.lower()) # 소문자로
# print(python.upper()) # 대문자로
# print(python[0].isupper())  # 첫번째 글자가 대문자인지 확인
# print(len(python))  #python 변수의  전체 문자열 길이
# print(python.replace("Python", "Java"))  #python 이란변수에서 Python 을 찾아 Java 로 변경
#
# index = python.index("n") #python 이라는 변수에서 n 이 어디에 있는지
# index = python.index("n", index+1)  # 그 다음에 존재하는 n 의 위치
#
# python.find("java")  #원하는 값이 없을 때에는 -1 반환
# python.index("java")  # 없을 시 에러
#
# python.couont("n") #python 에서 n 이 몇번 존재하는지
#
# #문자열 포맷팅
# #방법 1
#
# print("나는 %d 살입니다." %20) # %  정수
# print("나는 %s 을 좋아해요" %"프로그래밍")  # %s 문자열
# print("Apple 은 %c 로 시작해요 " % "A") # %c  character 문자
#
# print("나는 %s 색과 %s 색을 좋아해요 " %("빨간", "파란"))
#
# #방법 2
# print("나는 {}살 입니다.".format(20))
# print("나는 {} 색과 {} 색을 좋아해요 ".format("파란","빨간"))
# print("나는 {0} 색과 {1} 색을 좋아해요 ".format("파란","빨간"))
# print("나는 {1} 색과 {0} 색을 좋아해요 ".format("파란","빨간"))
#
# #밥법 3
# print("나는 {age} 색과 {color} 색을 좋아해요 ".format(age = 20, color="빨간"))
# print("나는 {age} 색과 {color} 색을 좋아해요 ".format(color="빨간", age = 20))
#
# #방법4 (v3.6 이상~)
# age = 20
# color = '빨간'
# print(f"나는 {age} 색과 {color} 색을 좋아해요")
#
# #탈출문자
#
# #  \n : 줄바꿈
# #  \" , \'  -> 따옴표 작음ㄴ 따옴표
# # \\ : 문장 내에서 하나의 \
# # \r : 커서를 맨앞으로 이동  print("Red Apple\rPine")
# # \b : 백스페이스 (한 글자 삭제)  print("Redd\bApple")
# # \t : tab
#
# #dictionary
#
# # cabinet = {3 : "유재석", 100: "김태호"}
# # print(cabinet[3])
# # print(cabinet[100]) # 해당 키값이 없으면 에러 / 종료됨
# #
# # print(cabinet.get(3)) # 해당 키값이 없어도 none 으로 반환 후 이후 과정 진행
# # print(cabinet.get(5,"사용가능"))
# #
# # print(3 in cabinet) #true
# # print(5 in cabinet)#False
#
# cabinet = {"A-3":"유재석", "B-100" : " 김태호"}
#
# print(cabinet["A-3"])
# print(cabinet["B-100"])
#
# #새손님
# print(cabinet)
# cabinet["C-20"] ="조세호"
# cabinet["A-3"] = "김종국"
# print(cabinet)
#
# #간 손님
# del cabinet["A-3"]
# print(cabinet)
#
# #key 들만 출력
# print(cabinet.keys())
#
# #value 만 출력
# print(cabinet.values())
#
# #key value
# print(cabinet.items())
#
# #모두 삭제
# cabinet.clear()
# print(cabinet)
#
# #set 집합
# #중복 안됨, 순서없음
#
# my_set = {1,2,3,3,3}
# print(my_set)
#
# java = {"유재석", "김태호","양세형"}
# python = set(["유재석", "박명수"])
#
# #교집합 (java 와 python 모두 가능)
# print(java & python)
# print(java.intersection((python)))
#
# #합집합 (java 할 수 잇거나 python 할 수 있는 개발자)
# print(java|python)
# print(java.union(python))
#
# #차집합 (java를 하지만 python은 할줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))
#
# #추가
# python.add("김태호")
#
# #제거
# java.remove("김태호")
#
#
# #자료구조의 변경
# #커피숍
#
# menu = {"커피","우유","쥬스"}
# print(menu,type(menu))
#
# menu = list(menu)
# print(menu, type(menu))
#
# menu = tuple(menu)
# print(menu, type(menu))
#
# menu = set(menu)
# print(menu, type(menu))
#
# #continue , break
# absent = [2,5]
# no_book = [7]
# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책 읽어봐".format(student))
#
# #한줄 for 문
# #출석 번호 1,2,3,4, 앞에 100을 붙이기로 함, 101 ,102 ,103 ,
# students = [1,2,3,4,5]
# print(students)
#
# students = [i+100 for i in students]
# print(students)
#
# #학생이름 길이로 변환
# std = ["Iron Man", "Thor", "I am groot"]
# std = [len(i) for i in std]
# print(std)
#
# #학생이름을 대문자로 변환
# stds = ["Iron Man", "Thor", "I am groot"]
# stds = [i.upper for i in stds]
# print(stds)


#기본값
# def profile(name, age=17, main_lang='python'): #같은 반 같은 수업 듣는다고 가정하면 age, main_lan 을 입력하지 않아도 기본값으로 설정됨
#     print("나이:{0}\t 나이:{1}\t 주 언어:{2}\t".format(name, age, main_lang))

#키워드 값
#profile(age = 14, name="유재석") //이런식으로 뒤죽박죽이어도 키워드 설정을 통해 함수 호출 가능

# #가변인자 . 제한 없이 넣을 수 있는 것.
# def profile(name, age, *lang): #lang1 lang2 lang3 --- 할 필요 없이 * 표시로 사용 가능
#     print("이름:{0}\t 나이:{1}".format(name,age),end =" ")
#     for i in lang:
#         print(i, end=" ")
#     print()
#
# profile("유재석",20,"python","C++")

#지역 변수 , 전역변수
# 함수 내에서 전역 변수를 사용 하려면 , global 변수 를 통해 호출 가능

#print("python","java", sep="vs")  sep를 통해 출력 시 구분되는 것 설정 가능
#print("python","java", sep="vs", end="?") end 처리를 해주면 줄바꿈이 안되고 한줄로 출력됨

# import sys
# print("Python","java",file=sys.stdout) #stdout 표준 출력으로 처리
# print("Python","java",file=sys.stderr) #stderr 표준 에러로 처리

# scores = {"수학":0,"영어":50,"코딩":100}
# for subject, score in scores.items():
#     # print(subject,score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") #ljust(8) 왼쪽 정렬 ,8칸확보 #rjust(4) 오른쪽 네칸확보

# for i in range(1,21):
#     print("대기번호 :" + str(num).zfill(3)) # 3자리로 맞추고 빈공간은 0으로 채우기

# answer = input("아무 값이나 입력하세요 :") #input 은 항상 문자열로 받음
# print("입력하신 값은" + answer +"입니다.")

#빈 자리는 빈공간으로 두고, 오른쪽 정렬하되 총 10자리 공간 확보
# print("{0: >10}".format(500))
# #양수일 땐 + 표시 , 음수일 땐 - 표시
# print("{0: >+10}".format(500))
# print("{0: >-10}".format(500))
# #왼쪽 정렬하고, 빈칸으로 _사용
# print("{0:_<10}".format(500))
# #3자리 마다 콤마 찎기
# print("{0:,}".format(10000000))
# #3자리 마다 콤마찍고 , + - 부호 붙이기
# print("{0:+,}".format(10000000000))
# print("{0:-,}".format(-10000000000))
# #3 마다 콤마 찍어주기 ,부호도 붙이고 ,자릿 수 확보하기
# #빈자리 ^로 채워주기
# print("{0:^<+30,}".format(10000000000))
# #소수점 출령
# print("{0:f}".format(5/3))
# #소숫점 둘째 자리
# print("{0:.2f}".format(5/3))

# #파일 입출력
# score_file = open("score.txt","w",encoding="utf8") # w 는 wirte
# print("수학:0",file=score_file)
# print("양아:50",file=score_file)
# score_file.close()
#
# score_file = open("score.txt",'a',encoding="utf8") # a 는 추가
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt",'r',encoding="utf8")
# print(score_file.read()) #한번에 읽어오기
# score_file.close()

# score_file = open("score.txt",'r',encoding="utf8")
# print(score_file.readline(), end='') # 줄별로 읽기, 한 줄읽고 커서는 다음 줄로
# print(score_file.readline(),end='')
# print(score_file.readline(),end='')
# print(score_file.readline(),end='')
# score_file.close()

# #몇줄인지 모를 때,
# score_file = open("score.txt",'r',encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()
#
# score_file = open("score.txt",'r',encoding="utf8")
# lines = score_file.readlines() #리스트 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()

#pickle
import pickle
# # profile_file = open("profile.pickle","wb") # write binary
# # profile = {"이름":"박명수","나이":30, '취미':["축구","골프","코딩"]}
# # print(profile)
# # pickle.dump(profile,profile_file)#profile 에 있는 정보를 file 에 저장
# # profile_file.close()
#
# profile_file = open("profile.pickle","wb") #read binary
# profile = pickle.load(profile_file) # file 에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()
#
# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))
# #with 는 close 할 필요가 없음
#
# with open("study.txt","w",encoding="utf8") as study_file:
#     study_file.write("파이써능ㄹ 열심히 공부중입니다.")
#
# with open("study.txt","r",encoding="utf8") as study_file:
#     print(study_file.read())

# # 마린 : 공격 유닛, 군인 , 총을 쏠 수 있음.
# name = "마린"
# hp = 40
# damage = 5
#
# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 : {0}, 공격력 : {1}\n.".format(hp, damage))
#유닛이 굉장히 많이 생산됨 -> class 로 간단하게 (금형 느낌)


# marine1 = Unit("마린", 40,5) # - 클래스로 부터 만들어지는 것 객체
# marine2 = Unit("마린", 40,5)
# tank1 = Unit("탱크", 150,35)
#
# # __init__ 생성자!
#
# wraith1 = Unit("레이스",80, 5)
# print("유닛이름 : {0}, 공격력 :{1}".format(wraith1.name, wraith1.damage))
#
# #마컨 한 레이스
# wraith2 = Unit("빼앗은 레이스", 80,5)
# wraith2.clocking = True #외부에서 clocking 이라는 변수를 추가로 할당 가능
# #확장된 변수는 확장한 변수에 대해서만 적용됨.
# if wraith2.clocking ==True:
#     print("{0}는 클로킹 상태입니다.".format(wraith2.name))
class Unit:
    def __init__(self,name,hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))



class AttackUnit(Unit):
    def __init__(self, name, hp,speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 공격 합니다. [공격력 {2}]".format(self.name,location,self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었씁니다.".format(self.name, self.damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))

        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name))


#다중 상속 : 자식 class 가 여러 부모 class 를 상속 받는 것

class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name,location)
# #발키리
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# method overriding
# vulture = AttackUnit("벌쳐",80,10,20)
#
# battlecruiser = FlyableAttackUnit("배틀크루저",500, 25,3)
#
#
# ##지상 유닛인지 공중 유닛인지 매번 확인하지 않기 위해 method overiding을 통해 move라는 함수로 통일
#
# vulture.move("11시")
# battlecruiser.move("9시")

#건물
class Buildingunit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) #super 할 때는 괄호 붙히고, self 없이 사용
        self.location = location

        #문제는 다중상속 시,,
        # 다중 상속시는 super가 아니고 Unit.__init__()요것 사용


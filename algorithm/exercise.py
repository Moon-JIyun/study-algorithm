# # quiz3 ) 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하시오
#
# website = str(input())
# website = website.replace("http://","")
# print(website)
# n = website.index(".")
# website = website[:n]
#
# psw = website[0:3]+str(len(website))+str(website.count('e'))+"!"
#
# print(f"생성된 비밀번호 : {psw}")
#
#
# #추첨
#
# from random import *
#
# users = list(range(1,21))
# shuffle(users)
#
# winners = sample(users,4)

#
# from random import *
#
# count = 0
# for i in range(1, 51):
#     time = randrange(5,51)
#     if 5<= time <=15:
#         print("[O] {0}번째 손님 (소요시간 : {1})".format(i,time))
#         count+=1
#     else:
#         print("[] {0}번째 손님 (소요시간 : {1})".format(i, time))
#
# print("총 탑승 승객 : {0}".format(count))



#
# # def solution(stones):
# stones = [2,5,1,3,2,1]
# cnt = 0
# current = 0
# n = len(stones)
#     while current < n:
#         print(stones[current])
#         current += stones[current]
#         print(current)
#         cnt += 1
#         print(cnt)


# name_list = ['james', 'luke', 'oliver', 'jack']
# answer = 0
# for name in name_list:
#     print(name)
#     for n in name:
#         print(n)
#         if n == 'j' and n == 'k':
#             answer += 1
#             print(answer)
#             continue
# arr = [[5,12,4,31],[24,13,11,2],[43,44,19,26],[33,65,20,21]]
# a = []
# for i in arr:
#     a += i
#     print(a)
#
# b= sorted(a)
# print(b)
# print(b[4])

#Quiz 표준 체중을 구하는 프로그램
#
# def std_Weight(height, gender):
#     if gender == "남자":
#         st_Weight =round((height/100*height/100)*22,2)
#     else:
#         st_weight = round((height/100*height/100)*21,2)
#     print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,st_Weight))
#
# std_Weight(175,"남자")
# from random import *
#
# class Unit:
#     def __init__(self,name,hp,speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
#
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었씁니다.".format(self.name, self.damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <=0:
#             print("{0} : 파괴되었습니다.".format(self.name))
#
#
# class AttackUnit(Unit):
#     def __init__(self, name, hp,speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 공격 합니다. [공격력 {2}]".format(self.name,location,self.damage))
#
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self,'마린',40,1,5)
#
#     #스팀팩 : 체력 10 감소 후, 이동 및 공격속도 증가
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -=10
#             print("{0} : 스팀팩 사용합니다ㅣ. (HP 10감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩 사용하지 못합니다.".format(self.name))
#
# class Tank(AttackUnit):
#     seize_developed = False
#
#     def __init__(self):
#         AttackUnit.__init__(self,'탱크',150,1,35)
#         self.seize_mode = False
#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return
#
#         if self.seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True
#         else:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /=2
#             self.seize_mode = False
#
#
# class Flyable:
#     def __init__(self,flying_speed):
#         self.flying_speed = flying_speed
#
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))
#
#
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) #지상 speed 0
#         Flyable.__init__(self, flying_speed)
#
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name,location)
#
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self,"레이스", 80,20,5)
#         self.clocked = False
#
#     def clocking(self):
#         if self.clocked == True:
#             print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
#             self.clocked == False
#         else :
#             print("{0} : 클로킹 모드로 전환합니다.".format(self.name))
#             self.clocked == True
#
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
#
# def game_over():
#     print("Player : gg")
#     print("게임이 종료되었습니다.")
#
# game_start()
#
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()
#
# t1 = Tank()
# t2 = Tank()
#
# w1 = Wraith()
#
# attack_units =[]
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)
#
# for unit in attack_units:
#     unit.move("1시")
#
# Tank.seize_developed = True
# print("[알림] 탱크 시즈모드 개발이 완료되었씁니다.")
#
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()
# for unit in attack_units:
#     unit.attack("1시")
#
# for unit in attack_units:
#     unit.damaged(randint(5,21)) #공격은 랜덤으로.
#
# game_over()


#Quiz) 총 3대의 매물
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
#송파 빌라 월세 500/50 2000년
#
# class House :
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
#
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)
#

#프로젝트 outline

import matplotlib.pyplot as plt

#import running_game as rg
#import quiz as qz

#순위 매기기

name = str(input('이름을 입력하세요 : '))
   
print("두근두근 기말 축제에 오신 걸 환영합니다!")
print("다음 부스 중 원하는 부스를 선택하세요")
print("1번 - 달리기 게임" +"\n" + "2번 - 숫자 맞추기(up & down) " )
print("3번 - 뉴턴의 사과 피하기" + "\n" + "4번 - 숫자맞추기2(야구게임)") 
move = str(input("원하시는 부스의 번호를 입력하세요 : "))

score = 0

def ranking_1():
        rank = []
        rank.append(name)    
        score = []
        score.append(score1)
        clr = ["r", "g", "b"]
        plt.bar(rank, score, color= clr)
        plt.show()
    
def ranking_2():
        rank = []
        rank.append(name)    
        score = []
        score.append(score2)
        clr = ["r", "g", "b"]
        plt.bar(rank, score, color= clr)
        plt.show()

def ranking_3():
        rank = []
        rank.append(name)    
        score = []
        score.append(score3)
        clr = ["r", "g", "b"]
        plt.bar(rank, score, color= clr)
        plt.show()

def ranking_4():
        rank = []
        rank.append(name)    
        score = []
        score.append(socre4)
        clr = ["r", "g", "b"]
        plt.bar(rank, score, color= clr)
        plt.show()
            
if move == "1" :
    import running_game as rg  
    score1 = rg.points  
    ranking_1() 
    plt.show()
elif move == "2" :
    print("숫자 맞추기 게임을 시작합니다!")
    print(f"1부터 100까지의 숫자 중 맞춰주세요. 기회는 10번 주어집니다.")   
    import quiz as qz
    score2 =  qz.get_score()
    plt.show()
elif move == "3" :
    import apple 
    score3 = apple.start(score)
    print(f'{score=}')
    plt.show()
elif move == "4" :
    import baseball_game as bg
    socre4 = bg.get_score
else :
    plt.show()

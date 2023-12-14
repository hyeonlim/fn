#프로젝트 outline

import matplotlib.pyplot as plt
from random import randint

#import running_game as rg
#import quiz as qz

#순위 매기기

name = input('이름을 입력하세요 : ')

while True:
    score = 0
    print("두근두근 기말 축제에 오신 걸 환영합니다!")
    print("다음 부스 중 원하는 부스를 선택하세요")
    print("1번 - 달리기 게임")
    print("2번 - 숫자 맞추기(up & down) " )
    print("3번 - 뉴턴의 사과 피하기")
    print("4번 - 숫자맞추기2(야구게임)")
    print("5번 - 나가기") 
    try:
        move = int(input("원하시는 부스의 번호를 입력하세요 : "))
    except:
        continue
    def ranking(score):
            
            user=["LHJ","JMS","JHG"]
            score_list =[randint(0, 150) for _ in range(len(user))]
            user.append(name)  
            score_list.append(score)
            color = ["r", "g", "b"]
            plt.bar(user, score_list, color=color)
            plt.xlabel("Users")
            plt.ylabel("Score")
            plt.show()
                
    if move == 1 :
        import running_game as rg 
        ranking(rg.menu(death_count=0))
        
    elif move == 2 :
        import quiz
        ranking(quiz.get_score())

    elif move == 3 :
        import apple 
        ranking(apple.start(score))
        
    elif move == 4 :
        import baseball_game as bg
        ranking(bg.get_score())
        
    elif move == 5:
        break
  
    else:
        continue
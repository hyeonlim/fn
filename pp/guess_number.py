import random

name = str(input('이름을 입력하세요 : '))
    
def guess_num(answer,chance):
    print("숫자 맞추기 게임을 시작합니다!")
    print(f"1부터 100까지의 숫자 중 맞춰주세요. 기회는 {chance}번 주어집니다.")
class guess_game():
    if __name__=="__main__":
        answer = random.randint(1,100)
        chance = 5
        guess_number(answer, chance) 
    
    for attempt in range(1, chance+1):
        guess = int(input(f"{attempt}번째 시도 - 추측한 숫자를 입력하세요:"))  
        if guess < answer:
            print("up")
        elif guess > answer:
            print("down")
        else:
            print("정답입니다!")
    else:
        print(f"아쉽게도 기회를 모두 사용하셨습니다. 정답은 {answer}입니다")
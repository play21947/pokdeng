import random

#pokdeng

def ai():
    ai_score = random.randint(1,9)
    return ai_score

def users():
    result_user = 0
    print('If you want to play [p] or not [n]')
    choose = input()
    if(choose == 'p'):
        user_score = random.randint(1,9)
        result_user = result_user + user_score
        ai_score = ai()
        print("My score : ",user_score)
        print('Do you want to draw more ? if yes [y] no [n]')
        choose2 = input()
        if(choose2 == 'y'):
            user_score_two = random.randint(1,9) #user_draw round 2
            print("draw round 2 : ",user_score_two)
            while(user_score_two != 0):
                result_user = result_user + 1
                user_score_two = user_score_two - 1
                if(result_user == 10):
                    result_user = 1
                    continue
            print("My Score : ",result_user)
            print("AI Score : ", ai_score)
            if(result_user == ai_score):
                print("Draw")
            elif(result_user > ai_score):
                print("USER WIN!!")
            elif(result_user < ai_score):
                print("USER LOSE!!")
                    
        elif(choose2 == 'n'):
            if(result_user == ai_score):
                print("Draw")
            elif(result_user > ai_score):
                print("USER WIN!!")
            elif(result_user < ai_score):
                print("USER LOSE!!")
    elif(choose == 'n'):
        print("OKAY")

def main():
    users()

main()
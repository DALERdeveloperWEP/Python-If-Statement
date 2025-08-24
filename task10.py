user_ball = int(input('ball: '))
if user_ball <= 100 and user_ball >= 90:
    print('A')
else:
    if user_ball <= 89 and user_ball >= 80:
        print('B')
    else:
        if user_ball <= 79 and user_ball >= 70:
            print('C')
        else:
            if user_ball <= 69 and user_ball >= 60:
                print('D')
            else:
                if user_ball <= 59 and user_ball >= 0:
                    print('F')
                else:
                    print('Noto‘g‘ri ball kiritildi!')
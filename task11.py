user_season = int(input('Enter season: '))
if user_season == 12 or user_season == 1 or user_season == 2:
    print('Qish')
else:
    if user_season >= 3 and user_season <= 5:
        print('Bahor')
    else:
        if user_season >= 6 and user_season <= 8:
            print('Yoz')
        else:
            if user_season >= 9 and user_season <= 11:
                print('Kuz')
            else:
                print('Error: wrong moth number')
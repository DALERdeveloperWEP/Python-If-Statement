tel_num = input('tel: ')
slice_num = int(tel_num[0:2])

if slice_num == 90 or slice_num == 91:
    print('Ucell')
else:
    if slice_num == 93 or slice_num == 94:
        print('Beeline')
    else:
        if slice_num == 95 or slice_num == 97:
            print('Uzmobile')
        else:
            if slice_num == 88 or slice_num == 99:
                print('Mobiuz')
            else:
                print("noma'lum operator")
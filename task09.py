num1 = int(input('uchburchak tomonlari1: '))
num2 = int(input('uchburchak tomonlari2: '))
num3 = int(input('uchburchak tomonlari3: '))
if num1 == num2 and num2 == num3:
    print('Teng tomonli')
else:
    if num1 == num2 or num2 == num3 or num1 == num3:
        print('Teng yonli')
    else:
        print('Turli tomonli')

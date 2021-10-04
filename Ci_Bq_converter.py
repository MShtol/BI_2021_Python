def Ci_Beq(x):
    print(x * 3700000000, 'Becqerels')


def Beq_Ci(x):
    print(x / 3700000000, 'Curie')


while True:
    number = int(input('Number: '))
    unit1_unit2 = input('print units for conversion (Ci_Beq or Beq_Ci): ')
    if unit1_unit2 == 'Ci_Beq':
        Ci_Bq(number)
    elif unit1_unit2 == 'Beq_Ci':
        Bq_Ci(number)
    else:
        print('Sorry, unknown units')
    if input('Type "stop" to stop it') == 'stop':
        print("stopped")
        break

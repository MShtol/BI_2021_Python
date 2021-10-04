def Ci_Bq(x):
    print(x * 3700000000, 'Becqerels')


def Bq_Ci(x):
    print(x / 3700000000, 'Curie')


while True:
    number = int(input('Number: '))
    unit1_unit2 = input('print units for conversion (Ci_Bq or Bq_Ci): ')
    if unit1_unit2 == 'Ci_Bq':
        Ci_Bq(number)
    elif unit1_unit2 == 'Bq_Ci':
        Bq_Ci(number)
    else:
        print('Sorry, unknown units')
    if input('Type "stop" to stop it') == 'stop':
        print("stopped")
        break

#!/usr/bin/env python
# coding: utf-8

# In[2]:


def Ci_Becq(x):
    print(x * 3700000000, 'Becqerels')


def Becq_Ci(x):
    print(x / 3700000000, 'Curie')


while True:
    number = float(input('Number: '))
    if number < 0:
        print('There are no "negative" radiation. Absolute value is used instead')
        number = abs(number)
    unit1_unit2 = input('print units for conversion (Ci_Becq or Becq_Ci): ')
    if unit1_unit2 == 'Ci_Becq':
        Ci_Becq(number)
    elif unit1_unit2 == 'Becq_Ci':
        Becq_Ci(number)
    else:
        print('Sorry, unknown units')
    if input('Type "stop" to stop it') == 'stop':
        print("stopped")
        break

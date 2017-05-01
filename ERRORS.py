LEX_ERRORS = ('ХЗ че за символ "{}". Символ номер  ',
              'Непредвиденный символ "{}" при определении вещественного числа. Символ номер ',
              'Очень много точек в вещественном числе "{}". Символ номер ',
              r'При обработки вещественного числа, пришел символ новой строки "\n". '
              r'Скорее всего пропущен символ конца строки ";" Символ номер ',
              )

PARS_ERRORS = {"RANGE": ['Пропущен оператор определения интервала "Range". ',
                         'Ожидался открывающий символ "[" при определении "Range", а пришел "{}". ',
                         'Ожидался закрывающий символ "]" при определении "Range", а пришел "{}". ',
                         'Непредвиденный символ "{}" при определении "Range". ',
                         'Лишний символ "{}"  при определении "Range". '
                         ],
               'METHOD': ['Пропущен оператор определения шага "Method". ',
                          'Неизвестный метод интегрирования {}. '
                          ],
               "STEP": ['Пропущен оператор определения шага "Step". '],
               "COEFF":['Пропущен оператор определения коффициентов "Coeff". '],
               "Vars0":['Пропущен оператор определения начальных условий "Vars0". '],
               }
# time = input('enter time: ').lower()
#
# if time == 'morning' or time == 'утро':
#     print('good morning')
# elif time == 'day' or time == 'день':
#     print('good afternoon')
# elif time == 'evening' or time == 'вечер':
#     print('good evening')
# else:
#     print('время неизвестно, просто здраствуйте.')
attempts = int(input('how many rounds? '))
while attempts > 0:
    print(f'попыток осталось: {attempts}')
    temperature: str = input('ведите температуру:')
     if temperature.lower() == 'выход':
        break
     elif temperature.isnumeric():
         temperature = int(temperature)
         if -40 <= temperature <= 0:
              print('ХОЛОДНО')
         elif temperature >= 1 and temperature <= 15:
              print('ПРОХЛАДНО')
         elif temperature >= 16 and temperature <= 25:
              print('ТЕПЛО')
         elif temperature >= 26 and temperature <= 40:
              print('ЖАРА')
         else:
            print(f"несовместимая с жизнью {temperature} градусов")
         attempts -= 1
    else:
        print('ведите "выход" правильно!')
        continue


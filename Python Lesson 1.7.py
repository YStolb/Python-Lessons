
# 7. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего. Требуется определить номер дня, на который результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
#Например: a = 2, b = 3.
#Результат:
#1-й день: 2
#2-й день: 2,2
#3-й день: 2,42
#4-й день: 2,66
#5-й день: 2,93
#6-й день: 3,22
#Ответ: на шестой день спортсмен достиг результата — не менее 3 км.#

while True:
        result_days = 1
        first_result_km = float (input("first result:"))
        last_result_km = float (input("final result:"))
        if first_result_km <= 0 or last_result_km <0:
                print("Results are to be more than 0. Start !=0")
        else:
                while first_result_km < last_result_km:
                        first_result_km += first_result_km * 0.1
                        result_days += 1

                print(f"You will reach the result in {result_days} days")
                break
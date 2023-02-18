age = []
n = int(input("Введите количество билетов, которые собираетесь купить: "))
deti_cena = 0
junior_cena = 990
old_cena = 1390

for i in range(n):
    new_element = int(input("Введите возраст участника: "))
    age.append(new_element)
    deti = 0
    junior = 0
    old = 0
a = 0
for J in age:
    if age[a] < 18:
        deti = deti + 1
    elif 18 <= age[a] < 25:
        junior = junior +1
    else:
        old = old + 1
    a = a + 1
if n <= 3:
    summa_oplati = deti * deti_cena + junior * junior_cena + old * old_cena
    print("Сумма к оплате: ", summa_oplati, 'руб.')
else:
    summa_oplati = (deti * deti_cena + junior * junior_cena + old * old_cena) * 0.9
    print("Сумма к оплате (с учетом скидки 10%) : ", summa_oplati, 'руб.')
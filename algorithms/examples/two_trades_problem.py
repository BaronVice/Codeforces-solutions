

def main():
    # Количество дней доступных для торговли на бирже
    n = 5
    # Цена акции в каждый день торгов
    stock = [10, 5, 5, 7, 6]

    # Находить лучшую точку входа будем следующим образом: на каждый из дней, кроме первого (его мы посчитаем - он
    # будет стартовым значением) у нас есть выбор - взять текущий день как точку входа, либо оставить прошлый день.
    # Это зависит от того, больше ли мы купим в текущий день или же больше могли купить до этого.

    first_buy = [1 / stock[0]]
    # Таким образом значение на позиции i в first_buy - какое наибольшее количество бумаг мы могли купить
    # от первого до i дня включительно
    for i in range(1, n):
        # Соответственно на текущую позицию ставим максимум между количеством бумаг с предыдущего дня, либо с текущего
        first_buy.append(max(first_buy[i-1], 1 / stock[i]))

    # Нашли точку входа - хорошо. Теперь купленные бумаги надо продать, стартовое значение будет равно 1
    # (попробуйте самостоятельно понять почему 1, ниже будет объяснение)
    first_sell = [1.0]
    # Если для покупки мы делили бюджет на стоимость бумаги, то логично, что при продаже будем умножать имеющееся
    # количество бумаг на стоимость бумаги
    for i in range(1, n):
        # В продажи добавляем либо предыдущее значение с продаж,
        # либо наибольшее количество купленных бумаг до i дня умноженное на стоимость бумаги в i день
        # (смотря, что больше)
        first_sell.append(max(first_sell[i-1], first_buy[i] * stock[i]))

    # А теперь ответ на вопрос, почему стартовое значение равно 1:
    # Если в первый день купить и в первый день продать акции, то получим ту же сумму, с которой начали торговать
    # (в нашем случае - это 1 рубль). Поэтому ставить туда first_buy[0] * stock[0] как-то глупо - оно всегда равно 1.
    print(first_sell)

    # В задаче сказано, что можно совершить 0 сделок, 2 сделки или 4 сделки
    # Вопрос: где будет лежать ответ на задачу, при условии, что мы пока что умеем совершать только 2 сделки?
    # Вопрос: в каком случае совершать какие-либо сделки не прибыльно (подсказка - ответ лежит в first_sell)?

    # А теперь скажем, что на можно совершить еще одну пару сделок: попробуйте дописать решение (принцип тот же самый,
    # с добавлением второй покупки и второй продажи - second_buy, second_sell)

    second_buy = [...]
    ...

    second_sell = [...]
    ...


if __name__ == "__main__":
    main()

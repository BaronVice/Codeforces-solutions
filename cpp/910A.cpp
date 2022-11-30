/* Задача весьма похожа на платную лестницу (у каждой ступеньки есть стоимость, пройти от земли до последней
ступеньки заплатив минимальное количество монет). Отличие в том, что не на каждую клетку можно попасть и стоимость
перехода на другую клетку = значение откуда прыгаем + 1 
   Да, наверняка можно решить аналитически, но перебором ответ найдется всегда 
   Здесь у нас динамика. Подзадача - найти минимальное количество прыжков для каждой кувшинки от 1 до n*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
using ll = long long;

int main(){
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    int n, d;
    cin >> n >> d;

    string swamp;
    cin >> swamp;

    // Буду искать минимум, поэтому начальные значения - максимум, до которого по условию не дотянусь
    // Беру на d клеток больше, чтобы начать со второй кувшинки и не выйти за пределы. Таким образом болото
    // Начинается с индекса d
    vector<int> jumps(n+d, 1000);
    // Вообще должно быть 1, но для ленивой динамики пока что 0
    jumps[d] = 0;

    // Решение подзадачи: ищу для кувшинки минимальное значение откуда могу прыгнуть (для d значение знаю, оно
    // Равно 1, поэтому начну со следующей)
    for (int i = d+1; i < n+d; i++){
        // Если на клетке есть кувшинка, то на нее можно прыгнуть
        if (swamp[i-d] != '0'){
            // Смотрю на предыдущие ячейки, откуда можно было прыгнуть
            for (int j = i-d; j < i; j++){
                // Берем минимальное значение между текущим и откуда прыгаем +1
                jumps[i] = min(jumps[i], jumps[j] + 1);
            }
        }
    } 
    // Вот теперь 1
    jumps[d] = 1;

    // Если не достигли конца (значение недостигаемого максимума), то -1, иначе что-то получили
    cout << (jumps[n+d-1] == 1000 ? -1 : jumps[n+d-1]) << '\n';

    return 0;
}
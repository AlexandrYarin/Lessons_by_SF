import numpy as np


def guess_the_number(number:int=1) -> int:
    """Алгоритм который угадывавет число

    Args:
        number (int, optional): Загаданное число. По умолчанию равно 1.

    Returns:
        int: Количество попыток
    """
    predict_number = np.random.randint(1, 101)
    up_border, down_border = 100 , 0
    count = 0
    
    while True:
        count += 1
        if predict_number > number:
            up_border = predict_number
            predict_number //= 2
        elif predict_number < number:
            if up_border - down_border == 1:
                predict_number = down_border + 1
            else:
                down_border = predict_number
                different_borders = up_border - down_border
                different_borders //= 2
                predict_number = down_border + different_borders 
        else:
            break
    return count
                
            
 
def score_game(guess_the_number) -> int:
    """Узнаем за какое количество попыток в среднем за 1000 подходов угадывает 
    число наш алгоритм

    Args:
        guess_the_number (function): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = [] 
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(guess_the_number(number))
    score = int(np.mean(count_ls))
    print(f'Данный алгоритм угадывает число за {score} попыток')
    return score

    
#RUN
if __name__ == '__main__':
    score_game(guess_the_number)

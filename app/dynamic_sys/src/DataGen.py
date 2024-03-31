import numpy as np
import random as r

# Класс для генерации данных
class DataGen:
    @staticmethod
    def voltages_float(steps, crop: int):
        """
        Создать массив со случайными напряжениями

        steps: количество напряжений в одном массиве
        crop: длина участка, где все значения напряжения должны быть одинаковы
        return: массив со случайными напряжениями
        """
        return np.array([[r.randint(0, 5)] * crop for _ in range(steps // crop)]).flatten()
import unittest
import logging
import traceback
from time import asctime

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner_1 = r.Runner('Данил')
            for _ in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 50)
            logging.info('test_walk выполнен успешно')
        except ValueError as e:
            logging.warning('Неверная скорость для Runner')

    def test_run(self):
        try:
            runner_2 = r.Runner('Миша')
            for _ in range(10):
                runner_2.run()
            self.assertEqual(runner_2.distance, 100)
            logging.info('test_run выполнен успешно')
        except TypeError as TE:
            logging.warning('Неверный тип данных для объекта Runner')


    def test_challenge(self):
        runner_3 = r.Runner("Лёша")
        runner_4 = r.Runner("Вася")
        for _ in range(10):
            runner_3.run()
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)


if __name__ == "__main__":
    unittest.main()
    logging.basicConfig(level=logging.INFO, filemode='w', encoding='utf-8', filename='runner_tests.log',
                        format='%(asctime)s, | %(levelname)s, | %(message)s')

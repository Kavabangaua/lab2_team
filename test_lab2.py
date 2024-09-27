import unittest
import grades_management as gm

class TestGradesManagement(unittest.TestCase):

    def setUp(self):
        # Тестові дані для всіх тестів
        self.data = {
            ('8-A', 'Soroka I.I.'): {
                'Math': [12, 10, 8, 9],
                'Ukr literature': [9, 7],
                'Chemistry': [6, 8, 7],
                'Physics': [11, 12, 11, 12],
                'PE': [10, 10, 10, 10]
            },
            ('8-A', 'Nikson A.V.'): {
                'Math': [12, 11, 10, 7],
                'Ukr literature': [10, 11],
                'Chemistry': [9, 8, 10],
                'Physics': [10, 10, 7, 6],
                'PE': [7, 8, 9, 10]
            }
        }

    # Окремі тести для calcucale_avg
    def test_calcucale_avg_valid_student(self):
        # Тест обчислення середнього для учня Soroka I.I. з математики
        self.assertEqual(gm.calcucale_avg(self.data, ('8-A', 'Soroka I.I.'), 'Math'), 9.75)

    def test_calcucale_avg_invalid_student(self):
        # Учень не знайдений (виняток TypeError)
        with self.assertRaises(TypeError):
            gm.calcucale_avg(self.data, ('9-A', 'Petrenko P.P.'), 'Math')

    def test_calcucale_avg_invalid_subject(self):
        # Предмет не знайдений (повертає -1)
        self.assertEqual(gm.calcucale_avg(self.data, ('8-A', 'Soroka I.I.'), 'Biology'), -1)

    # Окремі тести для class_by_name
    def test_class_by_name_valid(self):
        # Повернення класу для Soroka I.I.
        self.assertEqual(gm.class_by_name(self.data, 'Soroka I.I.'), '8-A')

    def test_class_by_name_invalid(self):
        # Учень не знайдений (виняток TypeError)
        with self.assertRaises(TypeError):
            gm.class_by_name(self.data, 'Petrenko P.P.')

    # Окремі тести для calcucale_avg_all
    def test_calcucale_avg_all_valid(self):
        # Обчислення середніх по всім предметам для Soroka I.I.
        expected = {
            'Math': 9.75,
            'Ukr literature': 8.0,
            'Chemistry': 7.0,
            'Physics': 11.5,
            'PE': 10.0
        }
        self.assertEqual(gm.calcucale_avg_all(self.data, ('8-A', 'Soroka I.I.')), expected)

    def test_calcucale_avg_all_invalid_student(self):
        # Учня немає в базі даних (виняток TypeError)
        with self.assertRaises(TypeError):
            gm.calcucale_avg_all(self.data, ('9-A', 'Petrenko P.P.'))

    def test_calcucale_avg_all_empty_subject(self):
        # Предмет без оцінок (повертає -1 для предмету)
        self.data[('8-A', 'Nikson A.V.')]['Biology'] = []
        expected_with_empty = {
            'Math': 10.0,
            'Ukr literature': 10.5,
            'Chemistry': 9.0,
            'Physics': 8.25,
            'PE': 8.5,
            'Biology': -1
        }
        self.assertEqual(gm.calcucale_avg_all(self.data, ('8-A', 'Nikson A.V.')), expected_with_empty)

if __name__ == '__main__':
    unittest.main()

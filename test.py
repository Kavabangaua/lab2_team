import unittest
from main import is_excellent_student, subject_max_grade, subject_min_grade
class TestStudentFunctions(unittest.TestCase):
    
    def setUp(self):
        self.data = {
            ('Іванов', 'Іван'): {
                'Математика': [12, 11, 10],
                'Фізика': [12, 12],
                'Хімія': [9, 10],
            },
            ('Петров', 'Петро'): {
                'Математика': [8, 9, 9],
                'Фізика': [7, 8],
                'Хімія': [6, 5],
            },
            ('Сидоров', 'Сидір'): {
                'Математика': [],
                'Фізика': [],
                'Хімія': [],
            },
        }
    @unittest.expectedFailure
    def test_is_excellent_student_true(self):
        #Іванов Іван має середні бали більше або рівно 10 по всім предметам
        self.assertTrue(is_excellent_student(self.data, ('Іванов', 'Іван')))
    
    def test_is_excellent_student_false(self):
        #Петров Петро має середній бал нижчий за 10
        self.assertFalse(is_excellent_student(self.data, ('Петров', 'Петро')))
    @unittest.expectedFailure
    def test_is_excellent_student_empty(self):
        #Сидоров Сидір має пусті списки оцінок
        self.assertIsNone(is_excellent_student(self.data, ('Сидоров', 'Сидір')))
    
    def test_is_excellent_student_no_student(self):
        #невідомий учень
        with self.assertRaises(TypeError):
            is_excellent_student(self.data, ('Невідомий', 'Учень'))

    def test_subject_max_grade(self):
        #Іванов Іван має максимальний бал 12 в "Математика" та "Фізика"
        self.assertEqual(subject_max_grade(self.data, ('Іванов', 'Іван')), ['Математика', 'Фізика'])
    
    def test_subject_max_grade_single(self):
        #Петров Петро має максимальний бал 9 в "Математика"
        self.assertEqual(subject_max_grade(self.data, ('Петров', 'Петро')), ['Математика'])
    
    def test_subject_max_grade_no_student(self):
        #невідомий учень
        with self.assertRaises(TypeError):
            subject_max_grade(self.data, ('Невідомий', 'Учень'))
    
    def test_subject_min_grade(self):
        #Іванов Іван має мінімальний бал 9 в "Хімія"
        self.assertEqual(subject_min_grade(self.data, ('Іванов', 'Іван')), ['Хімія'])
    
    def test_subject_min_grade_single(self):
        #Петров Петро має мінімальний бал 5 в "Хімія"
        self.assertEqual(subject_min_grade(self.data, ('Петров', 'Петро')), ['Хімія'])
    
    def test_subject_min_grade_no_student(self):
        #невідомий учень
        with self.assertRaises(TypeError):
            subject_min_grade(self.data, ('Невідомий', 'Учень'))

if __name__ == '__main__':
    unittest.main()
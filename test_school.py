import unittest

from Test import subject_avg, children_list, subject_best_children

class TestSchoolFunctions(unittest.TestCase):
    
    def setUp(self):
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
            },
            ('5-C', 'Kozak A.S.'): {
                'Math': [9, 10, 10, 10],
                'Ukr literature': [9, 10],
                'History': [6, 10, 11, 8],
                'English': [5, 12, 10, 11],
                'PE': [9, 8, 6, 4]
            },
            ('5-B', 'Moliga T.P.'): {
                'Math': [11, 11, 11, 10],
                'Ukr literature': [12, 10, 11],
                'History': [10, 10, 11, 12],
                'English': [11, 10, 12, 10, 11],
                'PE': [10, 10, 10, 10]
            },
            ('5-C', 'Vinnichenko D.R.'): {
                'Math': [10, 10, 10, 10],
                'Ukr literature': [11, 10],
                'History': [9, 10, 11, 12],
                'English': [11, 12, 7, 9, 10],
                'PE': [5, 5, 8, 9]
            }
        }

    def test_subject_avg_math(self):
        result = subject_avg(self.data, 'Math')
        expected = ['8-A: 10.25', '5-C: 9.75', '5-B: 10.75']
        self.assertEqual(result, expected)

    def test_subject_avg_no_subject(self):
        result = subject_avg(self.data, 'Geography')
        expected = []
        self.assertEqual(result, expected)

    def test_children_list_8A(self):
        result = children_list(self.data, '8-A')
        expected = ['Soroka I.I.', 'Nikson A.V.']
        self.assertEqual(result, expected)

    def test_children_list_nonexistent_class(self):
        result = children_list(self.data, '10-B')
        expected = []
        self.assertEqual(result, expected)

    def test_subject_best_children_math(self):
        result = subject_best_children(self.data, 'Math')
        expected = {'8': ['Soroka I.I.', 'Nikson A.V.'], '5': ['Moliga T.P.', 'Vinnichenko D.R.']}
        self.assertEqual(result, expected)

    def test_subject_best_children_no_subject(self):
        result = subject_best_children(self.data, 'Geography')
        expected = {}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

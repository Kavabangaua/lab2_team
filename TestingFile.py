import unittest

from main import add_child, add_child_subjects, add_child_grades

data ={ ('8-A','Soroka I.I.'):{'Math':[12, 10, 8, 9],
                         'Ukr literature':[9, 7],
                         'Chemistry':[6, 8, 7],
                         'Physics':[11, 12, 11, 12],
                         'PE':[10, 10, 10, 10]
                         },
        ('8-A','Nikson A.V.'):{'Math':[12, 11, 10, 7],
                         'Ukr literature':[10, 11],
                         'Chemistry':[9, 8, 10],
                         'Physics':[10, 10, 7, 6],
                         'PE':[7, 8, 9, 10]
                         },
       ('5-C','Kozak A.S.'):{'Math':[9, 10, 10, 10],
                         'Ukr literature':[9, 10],
                         'History':[6, 10, 11, 8],
                         'English':[5, 12, 10, 11],
                         'PE':[9, 8, 6, 4]
                         },
       ('5-B','Moliga T.P.'):{'Math':[11, 11, 11, 10],
                         'Ukr literature':[12, 10, 11],
                         'History':[10, 10, 11, 12],
                         'English':[11, 10, 12, 10, 11],
                         'PE':[10, 10, 10, 10]
                         },
       ('5-C','Vinnichenko D.R.'):{'Math':[10, 10, 10, 10],
                         'Ukr literature':[11, 10],
                         'History':[9, 10, 11, 12],
                         'English':[11, 12, 7, 9, 10],
                         'PE':[5, 5, 8, 9]
                         }
}

class MyTestCase(unittest.TestCase):

    def setUp(self):

        self.data = data.copy()

    def test_add_child(self):
        new_child = ('7-B', 'Ivanov I.I.')
        result = add_child(self.data, new_child)
        self.assertEqual(result, len(self.data))
        self.assertIn(new_child, self.data)

    def test_add_existing_child(self):
        existing_child = ('5-C', 'Kozak A.S.')
        with self.assertRaises(ValueError):
            add_child(self.data, existing_child)

    def test_add_child_subjects(self):
        new_child = ('7-B', 'Ivanov I.I.')
        subjects = ['Math', 'English']
        result = add_child_subjects(self.data, new_child, subjects)
        self.assertEqual(result, len(subjects))
        self.assertEqual(self.data[new_child]['Math'], [])
        self.assertEqual(self.data[new_child]['English'], [])

    def test_add_subject_to_existing_child(self):
        existing_child = ('8-A', 'Soroka I.I.')
        subjects = ['Biology']
        result = add_child_subjects(self.data, existing_child, subjects)
        self.assertEqual(result, len(self.data[existing_child]))
        self.assertIn('Biology', self.data[existing_child])
        self.assertEqual(self.data[existing_child]['Biology'], [])

    def test_add_child_grades(self):
        child = ('5-C', 'Vinnichenko D.R.')
        subject = 'Math'
        grades = [12, 12]
        result = add_child_grades(self.data, child, subject, grades)
        self.assertEqual(result, len(self.data[child][subject]))
        self.assertListEqual(self.data[child][subject], [10, 10, 10, 10, 12, 12])

    def test_add_new_subject_with_grades(self):
        child = ('5-C', 'Vinnichenko D.R.')
        new_subject = 'Geography'
        grades = [9, 10]
        result = add_child_grades(self.data, child, new_subject, grades)
        self.assertEqual(result, len(grades))
        self.assertIn(new_subject, self.data[child])
        self.assertListEqual(self.data[child][new_subject], grades)

    def test_add_grades_to_new_child(self):
        new_child = ('7-B', 'Ivanov I.I.')
        subject = 'Math'
        grades = [11, 12]
        result = add_child_grades(self.data, new_child, subject, grades)
        self.assertEqual(result, len(grades))
        self.assertIn(new_child, self.data)
        self.assertListEqual(self.data[new_child][subject], grades)

if __name__ == '__main__':
    unittest.main()

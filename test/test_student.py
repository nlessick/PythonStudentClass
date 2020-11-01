import unittest
from class_definitions import student as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = t.Student('Manning', 'Peyton')

    def tearDown(self):
        del self.student

    def test_initial_value_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Manning')
        self.assertEqual(self.student.first_name, 'Peyton')

    def test_inital_all_attributes(self):
        student = t.Student('Manning', 'Peyton', 'computer information science', 2.5) # this is not self.person from setUp, but local
        assert student.last_name == 'Manning'                 # note no self here on person or assert
        assert student.first_name == 'Peyton'
        assert student.major == 'computer information science'
        assert student.gpa == 2.5

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = t.Student('123', 'Peyton')

    def test_object_not_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            p = t.Student('Manning', '123')

    def test_object_not_created_error_ssn(self):
        with self.assertRaises(ValueError):
            p = t.Student('Manning', 'Peyton', 'computer information science', 'abc')

    def test_student_class_display_name(self):
        self.assertEqual(str(self.student), "Manning, Peyton:")   # Uses person from setUp()

    def test_student_class_display_name_ssn(self):
        p = t.Student('Manning', 'Peyton', 'computer information science', 2.5)    # Does not use person from setUp(), has local p
        self.assertEqual(str(p), "Manning, Peyton has major computer information science with gpa: 2.5")

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Manning, Peyton:')

if __name__ == '__main__':
    unittest.main()

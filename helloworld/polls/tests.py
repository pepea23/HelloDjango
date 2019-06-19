from django.test import TestCase


class exampleFizzBuzzTest(TestCase):
    
    def test_input_number_3_should_be_Fizz(self):
        expected = 'Fizz'
        result = inputNum(3)
        self.assertEqual(result,expected)
    
    def test_input_number_5_should_be_Buzz(self):
        expected = 'Buzz'
        result = inputNum(5)
        self.assertEqual(result,expected)

    def test_input_number_10_should_be_Buzz(self):
        expected = 'Buzz'
        result = inputNum(10)
        self.assertEqual(result,expected)

    def test_input_number_15_should_be_FizzBuzz(self):
        expected = 'FizzBuzz'
        result = inputNum(15)
        self.assertEqual(result,expected)

    def test_input_number_17_should_be_17(self):
        expected = 17
        result = inputNum(17)
        self.assertEqual(result,expected)

    def test_input_notnumber_ABC_should_be_ABC(self):
        expected = "ABC"
        result = inputNum("ABC")
        self.assertEqual(result,expected)
    
def inputNum(num):
    if type(num) == int:
      
        if num % 3 == 0 and num % 5 == 0:
            return 'FizzBuzz'
        elif(num % 3 == 0):
            return 'Fizz'
        elif(num % 5 == 0):
            return 'Buzz'

    return num

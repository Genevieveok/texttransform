import unittest
from unittest.mock import patch
import io
from text_transform import main, sentence_format

class TestTextTransform(unittest.TestCase):

    def test_sentence_format_single_sentence(self):
        input_text = "a gooD Day to EAt."
        expected_output = "A good day to eat."
        self.assertEqual(sentence_format(input_text), expected_output)

    def test_sentence_format_multiple_sentences(self):
        input_text = "a gooD Day to EAt. happy DAY. Do better."
        expected_output = "A good day to eat. Happy day. Do better."
        self.assertEqual(sentence_format(input_text), expected_output)

    def test_sentence_format_trailing_spaces_period(self):
        input_text = "  a gooD Day to EAt.   happy DAY.  "
        expected_output = "A good day to eat. Happy day."
        self.assertEqual(sentence_format(input_text), expected_output)

    def test_sentence_format_trailing_spaces(self):
        input_text = "  a gooD Day to EAt.   happy DAY  "
        expected_output = "A good day to eat. Happy day"
        self.assertEqual(sentence_format(input_text), expected_output)

    def test_sentence_format_empty_string(self):
        input_text = ""
        expected_output = ""
        self.assertEqual(sentence_format(input_text), expected_output)

    def test_embedded_periods(self):
        self.assertEqual(sentence_format("test... test."), "Test... test.")

    def test_long_string_with_multiple_sentences(self):
        self.assertEqual(sentence_format("this is a long sentence. here is another one. and another one."), 
                         "This is a long sentence. Here is another one. And another one.")

    def test_sentence_format_multiple_periods(self):
        input_text = "hello... world"
        expected_output = "Hello... world"
        self.assertEqual(sentence_format(input_text), expected_output)

    def test_sentence_format_no_period(self):
        input_text = "a gooD Day to EAt"
        expected_output = "A good day to eat"
        self.assertEqual(sentence_format(input_text), expected_output)

    @patch('sys.stdout', new_callable=lambda: io.StringIO())
    @patch('sys.argv', ['text_transform.py', '-sentence', 'a gooD Day to EAt. happy DAY. Do better.'])
    def test_main_sentence_format(self, mock_stdout):
        main()
        expected_output = "A good day to eat. Happy day. Do better.\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=lambda: io.StringIO())
    @patch('sys.argv', ['text_transform.py', '-upper', 'goot milk'])
    def test_main_uppercase(self, mock_stdout):
        main()
        expected_output = "GOOT MILK\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=lambda: io.StringIO())
    @patch('sys.argv', ['text_transform.py', '-lower', 'GOOT MILK'])
    def test_main_lowercase(self, mock_stdout):
        main()
        expected_output = "goot milk\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=lambda: io.StringIO())
    @patch('sys.argv', ['text_transform.py'])
    def test_main_no_arguments(self, mock_stdout):
        main()
        expected_output = "Please provide a sentence to convert.\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()

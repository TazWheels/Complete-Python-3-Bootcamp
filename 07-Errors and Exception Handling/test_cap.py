import unittest
import cap

class TestCap(unittest.TestCase):

	def test_one_word(self):
		text = 'python'
		result = cap.cap_text(text)
		self.assertEqual(result, 'Python')

	def test_multi_word(self):
		text = 'first second third'
		result = cap.cap_text(text)
		self.assertEqual(result, 'First Second Third')

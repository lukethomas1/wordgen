import unittest
import wordgenmethods as m
from approvaltests.Approvals import verify
from approvaltests.GenericDiffReporterFactory import GenericDiffReporterFactory


class TestWordGen(unittest.TestCase):
	def setUp(self):
		self.reporter = GenericDiffReporterFactory().get_first_working()

	def test(self):
		txtFile = open('./testFiles/test.txt', 'w');

		m.write_strings(2, txtFile);

		txtFile.close();

		testFile = open('./testFiles/test.txt', 'r');
		testArray = [];

		for line in testFile:
			testArray.append(line);

		testFile.close();

		verify(''.join(testArray), self.reporter);

		# self.assertEqual('aa', testArray[0]);
		# self.assertEqual('zz', testArray[len(testArray) - 1])
		# self.assertEqual(26 * 26, len(testArray))

if __name__ == '__main__':
	unittest.main();
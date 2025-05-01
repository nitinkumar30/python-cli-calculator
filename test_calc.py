import subprocess
import unittest


class TestCalcCLI(unittest.TestCase):
    def run_cli(self, *args):
        """Helper to run the CLI app and return output"""
        result = subprocess.run(["python", "calc.py", *args], capture_output=True, text=True)
        return result.stdout.strip()

    def test_addition(self):
        output = self.run_cli("add", "5", "3")
        self.assertEqual(output, "8.0")

    def test_subtraction(self):
        output = self.run_cli("sub", "10", "4")
        self.assertEqual(output, "6.0")

    def test_multiplication(self):
        output = self.run_cli("mul", "2", "3")
        self.assertEqual(output, "6.0")

    def test_division(self):
        output = self.run_cli("div", "9", "3")
        self.assertEqual(output, "3.0")

    def test_division_by_zero(self):
        output = self.run_cli("div", "9", "0")
        self.assertEqual(output, "Error: Division by zero")


if __name__ == '__main__':
    unittest.main()

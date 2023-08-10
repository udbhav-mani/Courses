from unittest import TestCase
from printer import Printer, PrinterError


class TestPrinter(TestCase):
    def setUp(self):
        self.printer = Printer(pages_pers=2.0, capacity=300)

    # This one is a shared printer
    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.printer = Printer(pages_pers=2.0, capacity=300)

    #  teardown and teardown class for anything we run after test

    def test_print_within_capacity(self):
        # printer = Printer(pages_pers=2.0, capacity=300)

        # this checks if there was any error only
        # printer.print(25)

        message = self.printer.print(25)
        self.assertEqual(message, f"Printer printed 25 pages in 12.50 seconds.")

    def test_print_outside_capacity(self):
        with self.assertRaises(PrinterError):
            self.printer.print(302)

    def test_print_exact_capacity(self):
        # if there was an equal in the >= this would fail
        message = self.printer.print(300)
        self.assertEqual(message, f"Printer printed 300 pages in 150.00 seconds.")

    def test_print_speed(self):
        message = self.printer.print(10)
        self.assertEqual(message, f"Printer printed 10 pages in 5.00 seconds.")

    def test_print_always2(self):
        fast_printer = Printer(pages_pers=5, capacity=1000)
        message = fast_printer.print(56)
        message2 = fast_printer.print(50)
        # fails
        # self.assertEqual(message2, "Printer printed 50 pages in 10.01 seconds.")
        # passes
        self.assertEqual(message, "Printer printed 56 pages in 11.20 seconds.")

    def test_printer_multipleruns(self):
        self.printer.print(100)
        self.printer.print(50)
        message = self.printer.print(60)

        # self.assertEqual(message, "Printer printed 60 pages in 30.00 seconds.")

    def test_printer_multipleruns_error(self):
        with self.assertRaises(PrinterError):
            self.printer.print(100)
            self.printer.print(50)
            self.printer.print(1000)

        # self.assertEqual(message, "Printer printed 60 pages in 30.00 seconds.")

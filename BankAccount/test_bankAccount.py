import unittest
from .bankAccount import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(1000)

    def tearDown(self):
        del self.account

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

    def test_withdraw_success(self):
        result = self.account.withdraw(400)
        self.assertTrue(result)
        self.assertEqual(self.account.get_balance(), 600)

    def test_withdraw_fail(self):
        result = self.account.withdraw(2000)
        self.assertFalse(result)
        self.assertEqual(self.account.get_balance(), 1000)


if __name__ == '__main__':
    unittest.main()

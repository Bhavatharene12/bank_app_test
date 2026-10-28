import pytest
from app import BankingSystem

def test_initial_balance():
    account = BankingSystem(50.0)
    assert account.check_balance() == 50.0

def test_deposit():
    account = BankingSystem(100.0)
    assert account.deposit(50.0) is True
    assert account.check_balance() == 150.0

def test_withdrawal_success():
    account = BankingSystem(100.0)
    assert account.withdraw(40.0) is True
    assert account.check_balance() == 60.0

def test_withdrawal_insufficient_funds():
    account = BankingSystem(100.0)
    assert account.withdraw(150.0) is False
    assert account.check_balance() == 100.0

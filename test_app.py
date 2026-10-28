import pytest
from app import BankingSystem

def test_initial_balance():
    account = BankingSystem(50.0)
    assert account.check_balance() == 50.0

def test_deposit():
    account = BankingSystem(100.0)
    assert account.deposit(50.0) is True

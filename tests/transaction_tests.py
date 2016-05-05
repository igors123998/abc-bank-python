from nose.tools import assert_is_instance, assert_true, assert_false

from abcbank.transaction import Transaction


def test_type():
    t = Transaction(5)
    assert_is_instance(t, Transaction, "correct type")
    assert_false(t.withdraw)


def test_withdraw():
    t = Transaction(-5)
    assert_true(t.withdraw)

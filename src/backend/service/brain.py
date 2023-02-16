from . import app, db
from .models import *
import random
import string
from datetime import datetime, date


# Basic functions
def hash_gen_engine():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    whole = lower + upper + digits
    hash_string = random.sample(whole, 8)
    hash = "".join(hash_string)
    return hash


def otp_gen_engine():
    digits = string.digits
    whole = digits
    otp_string = random.sample(whole, 6)
    otp = "".join(otp_string)
    return otp


def time_cal():
    current_t = datetime.now()
    current_date = str(date.today())
    current_t_f = current_t.strftime("%H:%M:%S")
    time_date = f'{current_t_f} {current_date}'
    return time_date


def add_owner(name, age):
    owner = Owner(name, hash_gen_engine(), age)
    db.session.add(owner)
    db.session.commit()
    return owner


def edit_owner_entry(name, age, hash):
    owner = Owner.query.filter_by(hash=hash).first()
    owner.name = name
    owner.age = age
    db.session.commit()
    return owner


def add_account(name, owner_hash):
    account = Account(name, hash_gen_engine(), owner_hash, 0)
    db.session.add(account)
    db.session.commit()
    return account


def add_transaction(expense, owner, amount, account_hash, owner_hash):
    transaction = Money(expense=expense, owner=owner, amount=int(amount), hash=hash_gen_engine(),
                        account_hash=account_hash, owner_hash=owner_hash, time=time_cal())
    db.session.add(transaction)
    db.session.commit()
    return transaction


def edit_transaction(expense, owner, amount, account_hash, owner_hash, hash):
    transaction = Money.query.filter_by(hash=hash).first()
    if transaction:
        transaction.expense = expense
        transaction.owner = owner
        transaction.amount = amount
        transaction.account_hash = account_hash
        transaction.owner_hash = owner_hash
        transaction.time = time_cal()
        db.session.commit()
        return transaction
    else:
        return "Transaction not found"


def delete_transaction(hash):
    transaction = Money.query.filter_by(hash=hash).first()
    if transaction:
        db.session.delete(transaction)
        db.session.commit()
        return "Transaction deleted"
    else:
        return "Transaction not found"


def transfer_transaction(hash, account_hash):
    transaction = Money.query.filter_by(hash=hash).first()
    if transaction:
        transaction.account_hash = account_hash
        transaction.time = time_cal()
        db.session.commit()
        return transaction
    else:
        return "Transaction not found"
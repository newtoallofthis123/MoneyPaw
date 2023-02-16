from service import app, db

class Owner(db.Model):
    __tablename__ = 'owner'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Text())
    hash = db.Column(db.Text())
    age = db.Column(db.Integer())

    def __init__(self, name, hash, age):
        self.name = name
        self.hash = hash
        self.age = age
    def __repr__(self):
        import json
        result = {
            "name": self.name,
            "hash": self.hash,
            "age": self.age
        }
        return result


class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Text())
    hash = db.Column(db.Text())
    owner_hash = db.Column(db.Text())
    balance = db.Column(db.Integer())

    def __init__(self, name, hash, owner_hash, balance):
        self.name = name
        self.hash = hash
        self.owner_hash = owner_hash
        self.balance = balance

    def __repr__(self):
        import json
        result = {
            "name": self.name,
            "hash": self.hash,
            "owner_hash": self.owner_hash,
            "balance": self.balance
        }
        return result

class Money(db.Model):
    __tablename__ = 'money'
    id = db.Column(db.Integer(), primary_key=True)
    expense = db.Column(db.Text())
    owner = db.Column(db.Text())
    owner_hash = db.Column(db.Text())
    amount = db.Column(db.Integer())
    account_hash = db.Column(db.Text())
    time = db.Column(db.Text())
    hash = db.Column(db.Text())

    def __init__(self, expense, owner, owner_hash, amount, account_hash, time, hash):
        self.expense = expense
        self.owner = owner
        self.owner_hash = owner_hash
        self.amount = amount
        self.account_hash = account_hash
        self.time = time
        self.hash = hash

    def __repr__(self):
        import json
        result = {
            "expense": self.expense,
            "owner": self.owner,
            "owner_hash": self.owner_hash,
            "amount": self.amount,
            "account_hash": self.account_hash,
            "time": self.time,
            "hash": self.hash
        }
        return result


db.create_all()
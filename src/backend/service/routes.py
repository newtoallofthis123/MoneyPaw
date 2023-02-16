# Service Imports
import os
from flask import jsonify, request
from .brain import *
from .models import *


# Home Route
@app.route("/")
def home():
    return jsonify("MoneyPaw API v.0.1")


# Owner Routes

# Creation Routes
@app.route("/create_owner", methods=["POST"])
def create_owner():
    owner_name = request.values.get("owner_name")
    owner_age = request.values.get("owner_age")
    if owner_name and owner_age:
        owner = add_owner(owner_name, owner_age)
        return owner.__repr__()
    else:
        return jsonify("Missing parameters")


# Edit Routes
@app.route("/edit_owner", methods=["POST"])
def edit_owner():
    owner_hash = request.values.get("owner_hash")
    owner_name = request.values.get("owner_name")
    owner_age = request.values.get("owner_age")
    if owner_hash and owner_name and owner_age:
        owner = Owner.query.filter_by(hash=owner_hash).first()
        if owner:
            response = edit_owner_entry(owner_name, owner_hash, owner_age)
            return response
        else:
            return jsonify("Owner not found")
    else:
        return jsonify("Missing parameters")


# Get Routes
@app.route("/owner/<hash>", methods=["GET"])
def get_owner(hash):
    owner = Owner.query.filter_by(hash=hash).first()
    if owner:
        return owner.__repr__()
    else:
        return jsonify("Owner not found")


# Debug
@app.route("/noobie/get_owners", methods=["GET"])
def get_owners():
    if request.values.get("whoami") != os.environ.get("NOOBIE_PASSWORD"):
        return jsonify("You are not a noobie")
    owners = Owner.query.all()
    response = []
    for owner in owners:
        response.append((owner.__repr__()))
    return response


# Account Routes

# Creation Routes
@app.route("/create_account", methods=["POST"])
def create_account():
    account_name = request.values.get("account_name")
    owner_hash = request.values.get("owner_hash")
    if account_name and owner_hash:
        owner = Owner.query.filter_by(hash=owner_hash).first()
        if owner:
            account = add_account(account_name, owner_hash)
            return account.__repr__()
        else:
            return jsonify(f"Owner with hash {owner_hash} not found")
    else:
        return jsonify("Missing parameters")


# Get Account
@app.route("/account/<hash>", methods=["GET"])
def get_account(hash):
    account = Account.query.filter_by(hash=hash).first()
    if account:
        return account.__repr__()
    else:
        return jsonify("Account not found")


@app.route("/noobie/get_accounts", methods=["GET"])
def get_accounts():
    if request.values.get("whoami") != os.environ.get("NOOBIE_PASSWORD"):
        return jsonify("You are not a noobie")
    accounts = Account.query.all()
    response = []
    for account in accounts:
        response.append(account.__repr__())
    return response


@app.route("/accounts/<owner_hash>", methods=["GET"])
def get_accounts_by_owner(owner_hash):
    accounts = Account.query.filter_by(owner_hash=owner_hash).all()
    response = []
    for account in accounts:
        response.append(account.__repr__())
    return response


# Transaction Routes

# Creation Routes
@app.route("/<owner_hash>/transaction", methods=["POST"])
def transaction_func(owner_hash):
    account_hash = request.values.get("account_hash")
    amount = request.values.get("amount")
    expense = request.values.get("expense")
    if account_hash and amount and expense and owner_hash:
        account = Account.query.filter_by(hash=account_hash).first()
        if account:
            if account.owner_hash == owner_hash:
                owner = Owner.query.filter_by(hash=owner_hash).first()
                if owner:
                    transaction = add_transaction(expense, owner.name, amount, account_hash, owner_hash)
                    return transaction.__repr__()
                else:
                    return jsonify("Owner not found")
            else:
                return jsonify("Account does not belong to owner")
        else:
            return jsonify("Account not found")
    else:
        return jsonify("Missing parameters")


@app.route("/noobie/get_transactions", methods=["GET"])
def get_all_transactions():
    if request.values.get("whoami") != os.environ.get("NOOBIE_PASSWORD"):
        return jsonify("You are not a noobie")
    transactions_info = Money.query.all()
    response = []
    for transaction in transactions_info:
        response.append(transaction.__repr__())
    return response


@app.route("/transaction/<transaction_hash>", methods=["GET"])
def get_transaction(transaction_hash):
    transaction = Money.query.filter_by(hash=transaction_hash).first()
    if transaction:
        return transaction.__repr__()
    else:
        return jsonify("Transaction not found")


@app.route("/transactions/<owner_hash>", methods=["GET"])
def get_transactions_by_owner(owner_hash):
    transactions = Money.query.filter_by(owner_hash=owner_hash).all()
    if transactions:
        response = []
        for transaction in transactions:
            response.append(transaction.__repr__())
        return response
    else:
        return jsonify("No transactions found")


@app.route("/transactions/<owner_hash>/<account_hash>", methods=["GET"])
def get_transactions_by_owner_and_account(owner_hash, account_hash):
    transactions = Money.query.filter_by(owner_hash=owner_hash, account_hash=account_hash).all()
    if transactions:
        response = []
        for transaction in transactions:
            response.append(transaction.__repr__())
        return response
    else:
        return jsonify("No transactions found")
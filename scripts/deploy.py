from brownie import Counter, accounts


def main():
    acct = accounts.load('1')
    Counter.deploy({'from': acct})

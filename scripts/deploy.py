from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Transact
    # Call
    print(simple_storage)


def main():
    deploy_simple_storage()

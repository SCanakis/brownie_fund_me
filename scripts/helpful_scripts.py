from brownie import MockV3Aggregator,accounts, network, config
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000

FORK_LOCAL_ENVIRONMENTS = ["mainnet-fork"] 
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORK_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
    

def deploy_mocks():
    print("The active network is " + network.show_active())
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})

    print("Mock Deployed!")
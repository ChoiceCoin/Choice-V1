#Stateless Smart Contracts on the Algorand Blockhain to send rewards for Democratic Participation.
#Choice Coin seeks to provide rewards to its community for participating in their local democracy.
#The inagaural democratic rewards program will focus on the advocacy for blockchain and cryptocurrency acceptance.

  
from algosdk import account, encoding, mnemonic,transaction
from algosdk.future.transaction import AssetTransferTxn, PaymentTxn
from algosdk.v2client import algod


algod_address = ""
algod_token = ""
# Initializes Client for node
headers = {"X-API-Key": algod_token }
algod_client = algod.AlgodClient(algod_token,algod_address,headers)
reserve_address = "" # Put in main fund address here
reserve_mnemonic = "" # Put in main fund receiver_mnemonic here
reserve_key = mnemonic.to_private_key(reserve_mnemonic)
asset_id =  # Probably will want to change if when we create a new asset

def choice_trade(sender, key, receiver, amount, index,comment):
    parameters = algod_client.suggested_params()
    transaction = AssetTransferTxn(sender, parameters, receiver, amount, index,note=comment)
    #Defines an inital transaction for choice Coin
    signature = transaction.sign(key)
    #Signs the transaction with the senders private key
    algod_client.send_transaction(signature)
    #Sends the transaction with the signature
    final = transaction.get_txid()
    return True, final




def init_democratic_participation():
    parameters = algod_client.suggested_params()
    choice_trade(reserve_address,reserve_key,participation_awards,1200000000,asset_id,'Initial Democratic Participation Rewards')


def democratic_awards(query,address):
    if query == 'Evidence of electoral participation':
        comment = 'Here is your Choice Coin Reward. \n Thanks for your help!'
        reward_amount = "Value"
        choice_trade(fund_address, fund_key, address, reward_amount, asset_id,comment)
    elif query == 'Letter to local legistature':
        comment = 'Here is your Choice Coin Reward. \n Thanks for sending a letter to your local government'
        reward_amount = "Value"
        choice_trade(fund_address, fund_key, address, reward_amount, asset_id,comment)
    else:
        comment = "Here is you Choice Coin Reward! \n Thanks for participating in our democracy!"
        reward_amount = "Value"
        choice_trade(fund_address, fund_key, address, reward_amount, asset_id,comment)


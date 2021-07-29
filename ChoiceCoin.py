from algosdk import account, encoding, mnemonic,algod
from algosdk.future.transaction import AssetTransferTxn, PaymentTxn, AssetConfigTxn
from algosdk.v2client import algod


algod_address = ""
algod_token = ""
#Initializes Client for node
headers = {"X-API-Key": algod_token }
algod_client = algod.AlgodClient(algod_token,algod_address,headers)
creator_address = "" #Put in main creator address here
creator_mnemonic = "" #Put in main creator mnemonic here
creator_key = mnemonic.to_private_key(creator_mnemonic)
#Details of the asset creation transaction.
#Initializes ChoiceCoin, defines manager addresses, and initiaties a main picture/hash


asset_details = {
	"asset_name": "ChoiceCoin",
	"unit_name": "Choice",
	"total": 10000000000,
	"decimals": 2,
  #Default Frozen is set to false to ensure that assets can be moved by holders and users.
	"default_frozen": False,
  #Manager is set to default account which owns a significant portion of Choice Coin and is in charge of distributing it.
	"manager": creator_address,
  #Freeze,Reserve, and Clawback Addresses are all ditributed to trusted custodians who can act accoridng to the standards of ethics and legality.
	"reserve": creator_address,
	"freeze": creator_address,
	"clawback": creator_address,
	"url": "Choice.jpg",
	"metadata_hash": b'\xfd\xeb\x1d.\x1c\xa3dQ\x9b\x84\xc4\xca\x1e\xd8\x82\xb5\xb6D)\x14\x86WZ(\x93=\xf3x\xc4MQ\xbd'
}


# Split files below into two seperate files
# One file will focus on launch
# Democratic participation won't be in the initial launch code
# Democratic participation will be better handled mannually
############################

 #Available once create_choice is run
metadata_file = "Choice.jpg"
metadatahash_b64 = "esdLhyjZFGbhMTKHtiCtbZEKRSGV1ookz3zeMRNUb0="
#Creates ChoiceCoin
def create_choice():
	params = algod_client.suggested_params()
	transaction = AssetConfigTxn(creator_address, params, **asset_details)
	signature = transaction.sign(creator_key)
    #Signs the transaction with the sender's private key
	algod_client.send_transaction(signature)
	transaction_id = transaction.get_txid()
	transaction_id = str(transaction_id)
	print("Your transaction information is at https://testnet.algoexplorer.io/tx/" + transaction_id)
def init_democratic_participation():
    parameters = algod_client.suggested_params()
    choice_trade(fund_address,fund_key,participation_awards,500000000,asset_id,'Initial Democratic Participation Rewards')

# This is not secure because 'Evidence of electoral participation' is ambiguous
# This will be a mannual add on
def democratic_awards(query,address):
    if query == 'Evidence of electoral participation':
        comment = 'Here is your Choice Coin Reward. \n Thanks for voting!'
        reward_amount = 5000
        choice_trade(fund_address, fund_key, address, reward_amount, asset_id,comment)
    elif query == 'Letter to local legistature':
        comment = 'Here is your Choice Coin Reward. \n Thanks for sending a letter to your local government'
        reward_amount = 10000
        choice_trade(fund_address, fund_key, address, reward_amount, asset_id,comment)
    elif query == 'Running in local government':
        comment = "Here is your Choice Coin Reward. \n Congrats on running in local government! Good Luck!"
        reward_amount = 50000
        choice_trade(fund_address, fund_key, address, reward_amount, asset_id,comment)
    else:
        comment = "Here is you Choice Coin Reward! \n Thanks for participating our democracy!"
        reward_amount = 1000
        choice_trade(fund_address, fund_key, address, reward_amount, asset_id,comment)


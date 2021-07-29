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


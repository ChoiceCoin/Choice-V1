# Copyright Fortior Blockchain, LLLP 2021
# Apache License

from algosdk import account, encoding, mnemonic,algod
from algosdk.future.transaction import AssetTransferTxn, PaymentTxn, AssetConfigTxn
from algosdk.future.transaction import AssetFreezeTxn
from algosdk.v2client import algod

#Choice Coin's inital asset architecture and configuration was written in Python.
#The Algorand-Python SDK was leveraged in order to connect effectively with the 
#Algorand Blockchain and create functionality on the network. The Algorand Python-SDK
#is easily imported through a downloadable module, allowing developers to send transactions,
#create smart contracts, and develop assets on the Algorand Blockchain. Specifcally, the 
#AssetConfigTxn function is used to create Choice Coin as a new Algorand-Standard-Asset on the network.


algod_address = "" 
algod_token = ""
#The algod_address and algod_token are unique variables that allow developers to connect to the Algorand Blockchain.
#This can be done through running a node, connecting to an API service, or running a sandbox. 
headers = {"X-API-Key": algod_token }
algod_client = algod.AlgodClient(algod_token,algod_address,headers)
#This secures the connection to the Algorand Blockchain through the parameters defined above.
creator_address = "" #This is the address that deploys Choice Coin to the Algorand Blockchain.
creator_mnemonic = "" 
creator_key = mnemonic.to_private_key(creator_mnemonic)


#Asset Configuration details for Choice Coin
asset_details = {
	"asset_name": "Choice Coin", #Name of the asset
	"unit_name": "Choice", #Individual Unit Name
	"total": 100000000000, #Total number of assets created at configuration
	"decimals": 2, #Decimal places in the total
	"default_frozen": False, #Sets default frozen to false for accounts, allowing them to transact freely.
	"manager": creator_address, #Defines the manager of Choice Coin, an address which is allowed to change the freeze and clawback functionality.
	"reserve": creator_address, #Reserve Address. Determines where all the Choice Coin is stored upon creation.
	"compliance": compliance_address, 
	"url": "https://fortiorblockchain.com/", #URL for Choice Coin website; allows users to find out more about the asset.
}

#The asset_details are used in Choice Coin's initial creation, defined below
def create_choice():
	params = algod_client.suggested_params() 
  #This sets parameters for the Asset Configuration Transaction based on Algorand's protocols.
  #These parameters include block time and executables.
	transaction = AssetConfigTxn(creator_address, params, **asset_details)
  #This defines a new transaction with the creator address and the asset details.
	signature = transaction.sign(creator_key)
	algod_client.send_transaction(signature)
	transaction_id = transaction.get_txid()
  #This signs the transaction with the sender's private key, and then sends it to the Algorand Client.
	transaction_id = str(transaction_id)
	print("Your transaction information is at https://testnet.algoexplorer.io/tx/" + transaction_id)
  #This gets the transaction id and then prints it on the console. The transaction is on AlgoExplorer, a block-explorer for Algorand.
  #AlgoExplorer is also the official block-explorer for Choice Coin as well.


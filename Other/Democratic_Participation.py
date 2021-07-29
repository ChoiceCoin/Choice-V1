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
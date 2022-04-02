#Apache License
import os
import hashlib
from datetime import datetime

import requests
from algosdk import mnemonic
from algosdk.v2client.algod import AlgodClient
from algosdk.future.transaction import AssetTransferTxn, wait_for_confirmation, PaymentTxn
from algosdk.encoding import encode_address

burn_address = '' #Put Address of the account here
burn_mnemonic = '' #Put the mneomonic of the acccount here.
burn_private_key = mnemonic.to_private_key(burn_mnemonic)
assets = ["ID"]
date = "03/14/2022"

algod_client = AlgodClient('', 'https://api.algoexplorer.io', headers={'User-Agent': 'algosdk'})


def asset_opt_in(asa_id):
    default_params = algod_client.suggested_params()
    txn = AssetTransferTxn(
        sender=burn_address,
        sp=default_params,
        receiver=burn_address,
        amt=0,
        index=asa_id)
    stxn = txn.sign(burn_private_key)
    print(f"Opting into Asset ID: {asa_id}")
    txid = algod_client.send_transaction(stxn)
    print(f"Transaction ID: {txid}")
    # Wait for the transaction to be confirmed
    wait_for_confirmation(algod_client, txid)


def get_public_address():
    timestamp = int(datetime.timestamp(datetime.strptime(date, "%m/%d/%Y")))
    r = requests.get(f'https://beacon.nist.gov/beacon/2.0/pulse/time/{timestamp}')
    beacon = r.json()['pulse']['outputValue']
    return encode_address(hashlib.sha256(bytes.fromhex(beacon)).digest())


def rekey_burn_to_address(public_address):
    default_params = algod_client.suggested_params()
    txn_rekey = PaymentTxn(
        sender=burn_address,
        sp=default_params,
        receiver=burn_address,
        amt=0,
        rekey_to=public_address
    )
    stxn = txn_rekey.sign(burn_private_key)
    print(f"Re-keying burn address to generated public address: {public_address}")
    txid = algod_client.send_transaction(stxn)
    print(f"Transaction ID: {txid}")
    # Wait for the transaction to be confirmed
    wait_for_confirmation(algod_client, txid)


def main():
    # opt-into assets
    for asa_id in assets:
        asset_opt_in(asa_id)
    # generate random public address. For more info please refer to:
    # https://algorandfoundation.cdn.prismic.io/algorandfoundation/5c80fdd2-fe08-4bda-8ac5-981b37908031_Early+Redemption+Confirmation.pdf
    public_address = get_public_address()
    rekey_burn_to_address(public_address)


if __name__ == '__main__':
    main()

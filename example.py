from secp256k1 import Signer

# example private key
private_key = 0xF9457396F73E9DFBCC00205FB0345196F33449648B200D709F9A62F4B5329F58

# example message hash
message_hash = 0x0050A397BBAAE4C5BD1C2CB2FDB76BAAA14AE2EF0BADA7723ECC2BE9055FCBE9

# example output, given private key and message hash
print(Signer(private_key).sign_hash(message_hash, print_qr=False))
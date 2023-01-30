# secp256k1
Minimal secp256k1 implementation, in python, that leverages built-in/native packages.

# example

```py
from secp256k1 import Signer

# test private key
private_key = <YOUR_PRIVATE_KEY>

# test eip712 message hash
message_hash = <MESSAGE_HASH_TO_SIGN>

print(Signer(private_key).sign_hash(message_hash, print_qr=False))
# v, r, s = (27, 0xe6fd848f211d1a74e372798b8d113efcab0f0ae8076db2239ad78d11d7c9f388, 0x886429dee386b5964dac0234cc27a732f7a3f75029b12aeb2cd17dd6eea2448a)
```

# disclaimer

WORK IN PROGRESS

**NOTE:** *This code has not been formally audited, and as such, it is not guaranteed to be secure/bug-free.*
# secp256k1
Minimal secp256k1 implementation, in python, that leverages built-in/native packages.

WORK IN PROGRESS

# example

```py
from secp256k1 import Signer

private_key = <YOUR_PRIVATE_KEY>

message_hash = <MESSAGE_HASH_TO_SIGN>

print(Signer(private_key).sign_hash(message_hash, print_qr=False))
# v, r, s = (27, 0xe6fd848f211d1a74e372798b8d113efcab0f0ae8076db2239ad78d11d7c9f388, 0x886429dee386b5964dac0234cc27a732f7a3f75029b12aeb2cd17dd6eea2448a)
```

# disclaimer

*The code provided in this project has not undergone a formal audit or review process. It is provided "as is" without warranty of any kind, either express or implied, including but not limited to the implied warranties of merchantability and fitness for a particular purpose. The user of this code assumes all responsibility and risk for its use, and the author(s) of this code shall not be held liable for any damages or losses resulting from the use of this code. It is recommended that any user of this code perform their own review and testing before using it in a production environment.*

from . import curve

# native modules
import json
import random
import subprocess

MALLEABILITY_THRESHOLD = 0x7fffffffffffffffffffffffffffffff5d576e7357a4501ddfe92f46681b20a0

class Signer:
    def __init__(self, privateKey: int):
        """
        Initialize an ECDSA object with a private key.
        """
        self.privateKey = curve.Fr(privateKey)
        self.publicKey = curve.G * self.privateKey

    def sign_hash(self, message_hash: int, print_qr=True):
        """
        Sign a message hash using the private key associated with this ECDSA object.
        If print_qr is True, then a QR code of the signature is also printed.
        """
        message_hash = curve.Fr(message_hash)

        # Generate the signature
        while True:
            # Generate a random number k
            k = curve.Fr(random.randint(0, curve.N))

            # Calculate the point R = k * G
            R = curve.G * k

            # Calculate the value r as the x coordinate of R
            r = curve.Fr(R.x.x)

            # If r is zero, then try again
            if r.x == 0:
                continue

            # Calculate the value s = (message_hash + private_key * r) / k
            s = (message_hash + self.privateKey * r) / k

            # If s is zero, then try again
            if s.x == 0:
                continue

            # Calculate v
            v = (255 >> s.as_int()) + 27

            # Verify the signature
            u1 = message_hash / s
            u2 = r / s
            x = curve.G * u1 + self.publicKey * u2

            # If the signature is invalid, then try again
            if x == curve.I or curve.Fr(x.x.x) != r:
                continue

            # If the signature is malleable, then try again
            if s.as_int() < MALLEABILITY_THRESHOLD:
                continue

            # If we reach this point, then the signature is valid, so we can break out of the loop
            break

        if print_qr:
            # Use python3-qrcode (built into tails) to create and display qr code
            subprocess.call(
                'qr "' + str(json.dumps({"v": str(v), "r": str(r), "s": str(s)})) + '"',
                shell=True,
            )

        # Return the signature (v, r, s)
        return v, r, s
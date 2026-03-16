# UpsideDown Cipher

[![License](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)
[![Version](https://img.shields.io/badge/version-0.42.1-blue)](https://github.com/BugFreeZone-py/UpsideDown)
[![Stars](https://img.shields.io/github/stars/BugFreeZone-py/UpsideDown?style=social)](https://github.com/BugFreeZone-py/UpsideDown)
[![Last commit](https://img.shields.io/github/last-commit/BugFreeZone-py/UpsideDown)](https://github.com/BugFreeZone-py/UpsideDown)
[![GitHub release](https://img.shields.io/github/v/release/BugFreeZone-py/UpsideDown)](https://github.com/BugFreeZone-py/UpsideDown/releases)

**Turn your data upside down! 🔄**  
UpsideDown is an experimental encryption algorithm that flips, shuffles, and XORs your data using a unique approach. It's not just encryption — it's a journey to the parallel dimension of your bytes.
## 🌟 Features
- **Byte shuffling** — reorders bytes based on your key (with simple salt)
- **Bit reversal** — flips every single bit in each byte (0b11001010 → 0b01010011)
- **XOR with derived key** — generates key stream using MD5 chain
- **The magic of 0.42** — uses `checksum ** 0.42` because 42 is the answer to everything
- **No dependencies** — pure Python, only standard library
## 🎯 Why 0.42?
```text
checksum ** 0.5  →  square root  (boring, everyone does that)
checksum ** 0.42 →  the Answer   (sqrt(2.38) — mysterious and beautiful)
```
The 0.42 exponent adds non-linearity and makes the key uniquely sensitive to the slightest changes. Also, it's a tribute to Douglas Adams.
## 📦 Installation
```bash
# Just copy the file, it's pure Python
# or download upsidedown.py directly
git clone https://github.com/BugFreeZone-py/UpsideDown.git
```
No pip install needed — only standard library modules: hashlib, random, struct, math.
## 🚀 Quick Start
```python
from upsidedown import encrypt, decrypt

# Your secret data
data = b"Hello, this is super secret message!"

# Your key (any integer)
key = 42

# Encrypt
encrypted = encrypt(data, key)
print(f"Encrypted: {encrypted}")

# Decrypt
decrypted = decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")
```
## 🔧 How It Works
UpsideDown uses a 3-layer transformation:
### Layer 1: Byte Shuffling
Bytes are permuted using a pseudo-random generator seeded with key + _simple_checksum(data). This makes the shuffling dependent on the data itself — no extra salt needed!
### Layer 2: Bit Reversal
Every single bit in every byte is reversed:
```text
b7 b6 b5 b4 b3 b2 b1 b0  →  b0 b1 b2 b3 b4 b5 b6 b7
```
This is where the name "UpsideDown" comes from!
### Layer 3: XOR with Derived Key
The XOR key is generated using an MD5 chain:
```python
blocks = ceil(len(data) / 16)
new_key = md5(key + struct.pack('f', _simple_checksum(key) ** .42)).digest()
for _ in range(blocks - 1):
    new_key += md5(new_key).digest()
new_key = new_key[:len(data)]
```
The ** 0.42 magic adds non-linearity and makes the key stream unique.
### Decryption
Decryption applies the layers in reverse order:
1. XOR with the same derived key
2. Bit reversal (self-inverse operation)
3. Reverse shuffling (using the same seed)
## 📊 API Reference
### `encrypt(data: bytes, key: int) -> bytes`
Encrypts bytes data with the given integer key.
### `decrypt(encrypted: bytes, key: int) -> bytes`
Decrypts data encrypted with `encrypt()`.
## 🧪 Examples
See `examples.py` for more:
```python
from upsidedown import encrypt, decrypt

# Your secret message
message = b"Hello, this is UpsideDown Cipher!"
key = 42

# Encrypt
encrypted = encrypt(message, key)
print(f"🔒 Encrypted: {encrypted}")

# Decrypt
decrypted = decrypt(encrypted, key)
print(f"🔓 Decrypted: {decrypted.decode('utf-8')}")

# Verify
assert message == decrypted
print("✅ Success! The message is back to normal.")
```
## ⚠️ Disclaimer
This is an **experimental** cipher created for educational purposes and fun. While it uses solid cryptographic primitives (shuffling, XOR, MD5), it hasn't been audited by professionals.  
**Do not use for protecting actual secrets or sensitive data.** For serious applications, use established algorithms like AES-256-GCM.
## 🤝 Contributing
Feel free to fork, experiment, and send PRs! The weirder the idea, the better. Want to try `checksum ** 0.43`? Go for it!
## 📜 License
**Creative Commons Zero v1.0 Universal (CC0)**  
You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission. No attribution required. See `LICENSE` file for details.
## 🌌 Why "UpsideDown"?
Because it flips bits upside down, turns your data into its mirror image, and sends it to the parallel dimension. Also, Stranger Things. 🌀
___
**Made with 🌀 and 0.42**

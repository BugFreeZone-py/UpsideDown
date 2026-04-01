import random
from hashlib import md5
from math import ceil
import struct

def _simple_checksum(data: bytes) -> int:
    return sum(data)

def shuffle_bytes(data: bytes, key: bytes) -> bytes:
    salt = bytes([_simple_checksum(data) & 0xFF])
    ba = bytearray(data)
    random.seed(key + salt)
    random.shuffle(ba)
    return bytes(ba)

def unshuffle_bytes(shuffled_bytes: bytes, key: bytes) -> bytes:
    salt = bytes([_simple_checksum(shuffled_bytes) & 0xFF])
    ba = bytearray(shuffled_bytes)
    length = len(ba)

    indices = list(range(length))
    random.seed(key + salt)
    random.shuffle(indices)

    unshuffled = bytearray(0 for _ in indices)
    for new_idx, old_idx in enumerate(indices):
        unshuffled[old_idx] = ba[new_idx]

    return bytes(unshuffled)

def reverse_bits_in_byte(b: int) -> int:
    b = ((b & 0xF0) >> 4) | ((b & 0x0F) << 4)
    b = ((b & 0xCC) >> 2) | ((b & 0x33) << 2)
    b = ((b & 0xAA) >> 1) | ((b & 0x55) << 1)
    return b

def reverse_bits_in_bytes(data: bytes) -> bytes:
    return bytes(reverse_bits_in_byte(b) for b in data)

def xor(data: bytes, key: bytes) -> bytes:
    blocks = ceil(len(data) / 16)
    new_key = md5(key + struct.pack('f', _simple_checksum(key) ** .42)).digest()
    for _ in range(blocks - 1):
        new_key += md5(new_key).digest()
    new_key = new_key[:len(data)]
    return bytes(a ^ b for a, b in zip(data, new_key))

def encrypt(data: bytes, key) -> bytes:
    key = key.encode("utf-8") if isinstance(key, str) else bytes(key)
    encrypted = shuffle_bytes(data, key)
    encrypted = reverse_bits_in_bytes(encrypted)
    encrypted = xor(encrypted, key)
    return encrypted

def decrypt(encrypted, key) -> bytes:
    key = key.encode("utf-8") if isinstance(key, str) else bytes(key)
    decrypted = xor(encrypted, key)
    decrypted = reverse_bits_in_bytes(decrypted)
    decrypted = unshuffle_bytes(decrypted, key)
    return decrypted

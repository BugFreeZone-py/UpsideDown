#!/usr/bin/env python3
"""
UpsideDown Cipher - Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Basic usage examples for the UpsideDown encryption algorithm.

Run this file to see UpsideDown in action:
    python examples.py
"""

from upsidedown import encrypt, decrypt


def example_basic():
    print("🔹 BASIC EXAMPLE")
    print("-" * 50)
    
    original = b"Hello, UpsideDown!"
    key = 42
    
    print(f"Original: {original}")
    print(f"Key:      {key}")
    
    encrypted = encrypt(original, key)
    print(f"Encrypted: {encrypted}")
    
    decrypted = decrypt(encrypted, key)
    print(f"Decrypted: {decrypted.decode('utf-8')}")
    
    assert original == decrypted
    print("✅ Success! Message recovered")
    print()


def example_deterministic():
    print("🔹 DETERMINISTIC EXAMPLE")
    print("-" * 50)
    
    data = b"Test"
    key = 123
    
    e1 = encrypt(data, key)
    e2 = encrypt(data, key)
    
    print(f"Data:          {data}")
    print(f"Key:           {key}")
    print(f"Encryption #1: {e1}")
    print(f"Encryption #2: {e2}")
    print(f"Same result?   {e1 == e2}")
    
    if e1 == e2:
        print("✅ Deterministic by design!")
    print()


def example_different_keys():
    print("🔹 DIFFERENT KEYS EXAMPLE")
    print("-" * 50)
    
    data = b"Secret"
    
    for key in [42, 43, 44]:
        encrypted = encrypt(data, key)
        print(f"Key {key}: {encrypted}")
    
    print()


def example_different_data():
    print("🔹 DIFFERENT DATA EXAMPLE")
    print("-" * 50)
    
    key = 42
    messages = [b"Hi", b"Hello", b"Hey there"]
    
    for msg in messages:
        encrypted = encrypt(msg, key)
        print(f"'{msg.decode()}' ({len(msg)} bytes) -> {encrypted}")
    
    print()


def example_binary_data():
    print("🔹 BINARY DATA EXAMPLE")
    print("-" * 50)
    
    binary = bytes([0, 1, 2, 3, 4, 5, 255, 254, 253])
    key = 999
    
    print(f"Binary data:   {binary}")
    print(f"First 5 bytes: {binary[:5]}")
    
    encrypted = encrypt(binary, key)
    print(f"Encrypted:     {encrypted}")
    
    decrypted = decrypt(encrypted, key)
    print(f"Decrypted:     {decrypted}")
    print(f"Match?         {binary == decrypted}")
    
    if binary == decrypted:
        print("✅ Binary data recovered perfectly!")
    print()


def example_large_data():
    print("🔹 LARGE DATA EXAMPLE")
    print("-" * 50)
    
    data = b"UpsideDown" * 100
    key = 42
    
    print(f"Data size: {len(data)} bytes")
    
    import time
    start = time.time()
    encrypted = encrypt(data, key)
    encrypt_time = time.time() - start
    
    start = time.time()
    decrypted = decrypt(encrypted, key)
    decrypt_time = time.time() - start
    
    print(f"Encryption time: {encrypt_time:.4f} seconds")
    print(f"Decryption time: {decrypt_time:.4f} seconds")
    print(f"Data recovered:  {data == decrypted}")
    
    if data == decrypted:
        print("✅ Large data works perfectly!")
    print()


def example_file_like():
    print("🔹 FILE ENCRYPTION SIMULATION")
    print("-" * 50)
    
    fake_file_content = b"USERNAME: admin\nPASSWORD: secret123\nAPI_KEY: 42-is-the-answer"
    key = 4242
    
    print("Original content:")
    print(f"  {fake_file_content[:50]}...")
    
    encrypted = encrypt(fake_file_content, key)
    print(f"Encrypted ({len(encrypted)} bytes):")
    print(f"  {encrypted[:50]}...")
    
    decrypted = decrypt(encrypted, key)
    print("Decrypted content:")
    print(f"  {decrypted[:50].decode()}...")
    
    assert fake_file_content == decrypted
    print("✅ File simulation successful!")
    print()


def example_error_handling():
    print("🔹 ERROR HANDLING EXAMPLE")
    print("-" * 50)
    
    data = b"Important message"
    correct_key = 42
    wrong_key = 43
    
    encrypted = encrypt(data, correct_key)
    
    print(f"Original: {data}")
    print(f"Encrypted with key {correct_key}: {encrypted}")
    
    decrypted_wrong = decrypt(encrypted, wrong_key)
    print(f"Decrypted with WRONG key {wrong_key}: {decrypted_wrong}")
    
    decrypted_correct = decrypt(encrypted, correct_key)
    print(f"Decrypted with CORRECT key {correct_key}: {decrypted_correct.decode()}")
    
    print("✅ Wrong key produces garbage (as expected)")
    print()


if __name__ == "__main__":
    print("\n🔄 UPSIDEDOWN CIPHER - EXAMPLES 🔄\n")
    
    example_basic()
    example_deterministic()
    example_different_keys()
    example_different_data()
    example_binary_data()
    example_large_data()
    example_file_like()
    example_error_handling()
    
    print("\n🎉 All examples completed! 🎉")

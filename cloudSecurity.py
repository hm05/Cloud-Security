import time
import psutil
import os
import hashlib
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from Crypto.Cipher import AES
import os

# Utility to measure processing time and memory usage
def measure_metrics(func, *args):
    start_time = time.time()
    
    # Measure memory usage before running the algorithm
    process = psutil.Process(os.getpid())
    memory_before = process.memory_info().rss / 1024 / 1024  # MB

    result = func(*args)

    # Measure memory usage after running the algorithm
    memory_after = process.memory_info().rss / 1024 / 1024  # MB
    memory_usage = memory_after - memory_before
    end_time = time.time()

    processing_time = end_time - start_time
    return result, processing_time, memory_usage

# Piccolo (Block Cipher) Placeholder (This is just an AES implementation as an example)
def piccolo_encrypt(data):
    # For simplicity, using AES as a placeholder for Piccolo
    key = os.urandom(16)  # 128-bit key for AES
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = data + (16 - len(data) % 16) * ' '  # Padding to be a multiple of 16
    encrypted = cipher.encrypt(padded_data.encode())
    return encrypted

# CHAOS (Stream Cipher) Placeholder
def chaos_encrypt(data):
    # Placeholder for CHAOS stream cipher, here using XOR operation as a simple stream cipher
    key = os.urandom(16)  # 128-bit key
    encrypted = bytes([data[i % len(data)] ^ key[i % len(key)] for i in range(len(data))])
    return encrypted

# BLAKE2 Hash Function
def blake2_hash(data):
    return hashlib.blake2b(data.encode()).hexdigest()

# ECC (Elliptic Curve Cryptography)
def ecc_sign(data):
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    signature = private_key.sign(data.encode(), ec.ECDSA(hashes.SHA256()))
    return signature

# Function to evaluate each algorithm
def evaluate_algorithms():
    data = "This is a test data for cryptographic algorithms!" * 1000  # Example data

    # Evaluate Piccolo (using AES as placeholder)
    encrypted_piccolo, time_piccolo, mem_piccolo = measure_metrics(piccolo_encrypt, data)
    print(f"Piccolo (Block Cipher) - Processing Time: {time_piccolo:.5f}s, Memory Usage: {mem_piccolo:.5f}MB")

    # Evaluate CHAOS Stream Cipher
    encrypted_chaos, time_chaos, mem_chaos = measure_metrics(chaos_encrypt, data.encode())
    print(f"CHAOS (Stream Cipher) - Processing Time: {time_chaos:.5f}s, Memory Usage: {mem_chaos:.5f}MB")

    # Evaluate BLAKE2 Hash Function
    hashed_blake2, time_blake2, mem_blake2 = measure_metrics(blake2_hash, data)
    print(f"BLAKE2 (Hash Function) - Processing Time: {time_blake2:.5f}s, Memory Usage: {mem_blake2:.5f}MB")

    # Evaluate ECC (Elliptic Curve Cryptography)
    signature_ecc, time_ecc, mem_ecc = measure_metrics(ecc_sign, data)
    print(f"ECC (Public Key) - Processing Time: {time_ecc:.5f}s, Memory Usage: {mem_ecc:.5f}MB")

if __name__ == "__main__":
    evaluate_algorithms()

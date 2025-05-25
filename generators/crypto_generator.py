"""
Cryptocurrency Style Private Key Generator
"""

import secrets
import hashlib

def generate_bitcoin_key():
    """Generate Bitcoin-style private key (32 bytes)"""
    try:
        # Generate 256-bit random number
        private_key = secrets.randbits(256)
        return format(private_key, '064x')
        
    except Exception as e:
        return f"Error generating Bitcoin key: {str(e)}"

def generate_ethereum_key():
    """Generate Ethereum-style private key"""
    try:
        # Generate 32 random bytes
        private_key = secrets.token_bytes(32)
        return private_key.hex()
        
    except Exception as e:
        return f"Error generating Ethereum key: {str(e)}"

def generate_wallet_seed():
    """Generate wallet seed phrase style"""
    try:
        # Generate random data
        random_data = secrets.token_bytes(64)
        
        # Hash dengan SHA-256
        seed_hash = hashlib.sha256(random_data).hexdigest()
        return seed_hash
        
    except Exception as e:
        return f"Error generating wallet seed: {str(e)}"

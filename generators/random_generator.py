"""
Random Private Key Generator
"""

import secrets
import hashlib

def generate_random_key(length=32):
    """Generate random private key"""
    try:
        return secrets.token_hex(length)
    except Exception as e:
        return f"Error generating random key: {str(e)}"

def generate_secure_random_key():
    """Generate extra secure random key"""
    try:
        # Generate random bytes
        random_bytes = secrets.token_bytes(32)
        
        # Hash untuk extra security
        hash_object = hashlib.sha256(random_bytes)
        return hash_object.hexdigest()
        
    except Exception as e:
        return f"Error generating secure random key: {str(e)}"

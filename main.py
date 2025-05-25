#!/usr/bin/env python3
"""
Private Key Generator - Simple Python Version with Safe Logging
Author: Your Name
"""

import os
from datetime import datetime
from generators.rsa_generator import generate_rsa_key
from generators.random_generator import generate_random_key
from generators.crypto_generator import generate_bitcoin_key, generate_ethereum_key
from utils.logger import KeyLogger

def main():
    print("=" * 50)
    print("🔐 PRIVATE KEY GENERATOR")
    print("=" * 50)
    
    # Initialize logger
    logger = KeyLogger()
    
    while True:
        print("\nPilih jenis private key:")
        print("1. RSA Private Key (2048-bit)")
        print("2. Random Private Key (256-bit)")
        print("3. Bitcoin Style Private Key")
        print("4. Ethereum Style Private Key")
        print("5. Generate Semua")
        print("6. 📝 Lihat Log History")
        print("7. 💾 Export Keys ke File")
        print("8. 🗑️ Clear Log History")
        print("0. Keluar")
        
        choice = input("\nMasukkan pilihan (0-8): ").strip()
        
        if choice == "1":
            print("\n🔑 Generating RSA Private Key...")
            key = generate_rsa_key()
            print(key)
            logger.log_key_generation("RSA", key[:50] + "..." if len(key) > 50 else key)
            
        elif choice == "2":
            print("\n🔑 Generating Random Private Key...")
            key = generate_random_key()
            print(f"Random Key: {key}")
            logger.log_key_generation("Random", key)
            
        elif choice == "3":
            print("\n🔑 Generating Bitcoin Private Key...")
            key = generate_bitcoin_key()
            print(f"Bitcoin Key: {key}")
            logger.log_key_generation("Bitcoin", key)
            
        elif choice == "4":
            print("\n🔑 Generating Ethereum Private Key...")
            key = generate_ethereum_key()
            print(f"Ethereum Key: {key}")
            logger.log_key_generation("Ethereum", key)
            
        elif choice == "5":
            print("\n🔑 Generating All Types...")
            rsa_key = generate_rsa_key()
            random_key = generate_random_key()
            bitcoin_key = generate_bitcoin_key()
            ethereum_key = generate_ethereum_key()
            
            print("\n1. RSA Private Key:")
            print(rsa_key)
            print(f"\n2. Random Key: {random_key}")
            print(f"\n3. Bitcoin Key: {bitcoin_key}")
            print(f"\n4. Ethereum Key: {ethereum_key}")
            
            # Log semua
            logger.log_key_generation("RSA", rsa_key[:50] + "...")
            logger.log_key_generation("Random", random_key)
            logger.log_key_generation("Bitcoin", bitcoin_key)
            logger.log_key_generation("Ethereum", ethereum_key)
            
        elif choice == "6":
            print("\n📝 Log History:")
            logger.show_log_history()
            
        elif choice == "7":
            print("\n💾 Export Options:")
            print("1. Export Log Only (Aman)")
            print("2. Export Keys (⚠️ BERBAHAYA!)")
            export_choice = input("Pilih (1-2): ").strip()
            
            if export_choice == "1":
                logger.export_log_only()
            elif export_choice == "2":
                confirm = input("⚠️ YAKIN? Ini akan menyimpan private key! (yes/no): ")
                if confirm.lower() == "yes":
                    logger.export_with_keys()
                else:
                    print("❌ Export dibatalkan")
            
        elif choice == "8":
            confirm = input("🗑️ Yakin ingin hapus semua log? (yes/no): ")
            if confirm.lower() == "yes":
                logger.clear_logs()
                print("✅ Log history berhasil dihapus")
            
        elif choice == "0":
            print("\n👋 Terima kasih!")
            break
            
        else:
            print("\n❌ Pilihan tidak valid!")
        
        input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()

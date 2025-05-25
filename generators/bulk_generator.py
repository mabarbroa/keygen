"""
Bulk Private Key Generator - Clean Output Version
"""

import time
from datetime import datetime
from .rsa_generator import generate_rsa_key
from .random_generator import generate_random_key
from .crypto_generator import generate_bitcoin_key, generate_ethereum_key

class BulkKeyGenerator:
    def __init__(self, logger):
        self.logger = logger
        
    def bulk_generation_menu(self):
        """Menu untuk bulk generation"""
        print("\n" + "="*50)
        print("🔢 BULK PRIVATE KEY GENERATOR")
        print("="*50)
        
        # Pilih jenis key
        print("\nPilih jenis private key:")
        print("1. Random Private Key (Tercepat)")
        print("2. Bitcoin Style Private Key")
        print("3. Ethereum Style Private Key")
        print("4. RSA Private Key (Terlambat)")
        print("5. Mixed (Semua jenis)")
        print("0. Kembali")
        
        key_type = input("\nMasukkan pilihan (0-5): ").strip()
        
        if key_type == "0":
            return
            
        # Input jumlah key
        try:
            count = int(input("\nMasukkan jumlah key yang ingin di-generate (1-100): "))
            if count < 1 or count > 100:
                print("❌ Jumlah harus antara 1-100!")
                return
        except ValueError:
            print("❌ Input tidak valid!")
            return
        
        # Konfirmasi
        type_names = {
            "1": "Random",
            "2": "Bitcoin",
            "3": "Ethereum", 
            "4": "RSA",
            "5": "Mixed"
        }
        
        print(f"\n📋 Akan generate {count} {type_names.get(key_type, 'Unknown')} private key(s)")
        confirm = input("Lanjutkan? (y/n): ").strip().lower()
        
        if confirm != 'y':
            print("❌ Bulk generation dibatalkan")
            return
        
        # Mulai generation
        self._generate_bulk_keys(key_type, count)
    
    def _generate_bulk_keys(self, key_type, count):
        """Generate bulk keys"""
        print(f"\n🚀 Memulai bulk generation {count} keys...")
        print("⏳ Mohon tunggu...")
        
        start_time = time.time()
        generated_keys = []
        
        try:
            for i in range(count):
                # Progress indicator
                if count > 10:
                    progress = (i + 1) / count * 100
                    print(f"\r🔄 Progress: {progress:.1f}% ({i+1}/{count})", end="", flush=True)
                
                if key_type == "1":  # Random
                    key = generate_random_key()
                    generated_keys.append(key)
                    self.logger.log_key_generation("Random", key)
                    
                elif key_type == "2":  # Bitcoin
                    key = generate_bitcoin_key()
                    generated_keys.append(key)
                    self.logger.log_key_generation("Bitcoin", key)
                    
                elif key_type == "3":  # Ethereum
                    key = generate_ethereum_key()
                    generated_keys.append(key)
                    self.logger.log_key_generation("Ethereum", key)
                    
                elif key_type == "4":  # RSA
                    key = generate_rsa_key()
                    generated_keys.append(key)
                    self.logger.log_key_generation("RSA", key[:50] + "...")
                    
                elif key_type == "5":  # Mixed
                    # Rotasi jenis key
                    types = ["Random", "Bitcoin", "Ethereum"]
                    selected_type = types[i % len(types)]
                    
                    if selected_type == "Random":
                        key = generate_random_key()
                    elif selected_type == "Bitcoin":
                        key = generate_bitcoin_key()
                    else:  # Ethereum
                        key = generate_ethereum_key()
                    
                    generated_keys.append(key)
                    self.logger.log_key_generation(selected_type, key)
            
            end_time = time.time()
            duration = end_time - start_time
            
            print(f"\n\n✅ Berhasil generate {count} keys dalam {duration:.2f} detik!")
            print(f"⚡ Rate: {count/duration:.1f} keys/detik")
            
            # Tampilkan hasil
            self._display_bulk_results(generated_keys, count, key_type)
            
        except Exception as e:
            print(f"\n❌ Error saat bulk generation: {e}")
    
    def _display_bulk_results(self, generated_keys, count, key_type):
        """Tampilkan hasil bulk generation - OUTPUT BERSIH"""
        print("\n" + "="*60)
        print("📊 HASIL BULK GENERATION")
        print("="*60)
        
        # Tampilkan semua keys tanpa nomor
        print(f"\n🔑 {count} Private Keys:")
        print("="*50)
        
        # Output bersih - langsung private key saja
        for key in generated_keys:
            print(key)  # TANPA NOMOR, TANPA LABEL
        
        # Opsi export
        print(f"\n💾 Export Options:")
        print("1. Export ke file TXT")
        print("2. Export ke file JSON") 
        print("3. Tidak export")
        
        export_choice = input("\nPilih export (1-3): ").strip()
        
        if export_choice == "1":
            self._export_to_txt(generated_keys, key_type)
        elif export_choice == "2":
            self._export_to_json(generated_keys, key_type)
        elif export_choice == "3":
            print("✅ Keys tidak di-export")
    
    def _export_to_txt(self, generated_keys, key_type):
        """Export keys ke file TXT - BERSIH TANPA NOMOR"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"generated_keys/bulk_keys_{timestamp}.txt"
            
            # Buat direktori jika belum ada
            import os
            os.makedirs("generated_keys", exist_ok=True)
            
            with open(filename, 'w') as f:
                f.write("BULK GENERATED PRIVATE KEYS\n")
                f.write("="*50 + "\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Total Keys: {len(generated_keys)}\n\n")
                
                # Output bersih tanpa nomor
                for key in generated_keys:
                    f.write(f"{key}\n")
            
            print(f"✅ Keys berhasil di-export ke: {filename}")
            print("⚠️ JANGAN COMMIT FILE INI KE GIT!")
            
        except Exception as e:
            print(f"❌ Error export ke TXT: {e}")
    
    def _export_to_json(self, generated_keys, key_type):
        """Export keys ke file JSON - BERSIH"""
        try:
            import json
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"generated_keys/bulk_keys_{timestamp}.json"
            
            # Buat direktori jika belum ada
            import os
            os.makedirs("generated_keys", exist_ok=True)
            
            export_data = {
                "metadata": {
                    "generated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "total_keys": len(generated_keys),
                    "generator": "Bulk Private Key Generator"
                },
                "keys": generated_keys  # Langsung array keys tanpa index
            }
            
            with open(filename, 'w') as f:
                json.dump(export_data, f, indent=2)
            
            print(f"✅ Keys berhasil di-export ke: {filename}")
            print("⚠️ JANGAN COMMIT FILE INI KE GIT!")
            
        except Exception as e:
            print(f"❌ Error export ke JSON: {e}")

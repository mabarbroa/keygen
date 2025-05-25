"""
Safe Key Logger - Logging dengan opsi keamanan
"""

import os
import json
import hashlib
from datetime import datetime
from typing import List, Dict

class KeyLogger:
    def __init__(self):
        self.log_dir = "logs"
        self.keys_dir = "generated_keys"  # HANYA untuk testing!
        self.log_file = os.path.join(self.log_dir, "key_generation.log")
        self.session_keys = []  # Temporary storage untuk session
        
        # Buat direktori jika belum ada
        os.makedirs(self.log_dir, exist_ok=True)
        
    def log_key_generation(self, key_type: str, key_preview: str):
        """Log key generation dengan informasi aman"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Hash key untuk identifikasi aman
        key_hash = hashlib.sha256(key_preview.encode()).hexdigest()[:16]
        
        log_entry = {
            "timestamp": timestamp,
            "type": key_type,
            "key_hash": key_hash,
            "key_length": len(key_preview),
            "session_id": id(self)
        }
        
        # Simpan ke session (temporary)
        self.session_keys.append({
            **log_entry,
            "full_key": key_preview  # HANYA untuk session ini!
        })
        
        # Simpan log aman ke file
        self._write_safe_log(log_entry)
        
    def _write_safe_log(self, log_entry: Dict):
        """Write safe log tanpa private key"""
        try:
            # Baca log existing
            logs = []
            if os.path.exists(self.log_file):
                with open(self.log_file, 'r') as f:
                    logs = json.load(f)
            
            # Tambah log baru
            logs.append(log_entry)
            
            # Simpan kembali
            with open(self.log_file, 'w') as f:
                json.dump(logs, f, indent=2)
                
        except Exception as e:
            print(f"❌ Error writing log: {e}")
    
    def show_log_history(self):
        """Tampilkan history log yang aman"""
        try:
            if not os.path.exists(self.log_file):
                print("📝 Belum ada log history")
                return
                
            with open(self.log_file, 'r') as f:
                logs = json.load(f)
            
            if not logs:
                print("📝 Log history kosong")
                return
                
            print("\n" + "="*60)
            print("📝 LOG HISTORY (AMAN - TANPA PRIVATE KEY)")
            print("="*60)
            
            for i, log in enumerate(logs[-10:], 1):  # Show last 10
                print(f"\n{i}. {log['timestamp']}")
                print(f"   Type: {log['type']}")
                print(f"   Hash: {log['key_hash']}")
                print(f"   Length: {log['key_length']} chars")
                
        except Exception as e:
            print(f"❌ Error reading log: {e}")
    
    def export_log_only(self):
        """Export hanya log tanpa private key"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            export_file = f"logs/safe_export_{timestamp}.json"
            
            if os.path.exists(self.log_file):
                with open(self.log_file, 'r') as f:
                    logs = json.load(f)
                
                with open(export_file, 'w') as f:
                    json.dump(logs, f, indent=2)
                
                print(f"✅ Log aman berhasil di-export ke: {export_file}")
            else:
                print("❌ Tidak ada log untuk di-export")
                
        except Exception as e:
            print(f"❌ Error export log: {e}")
    
    def export_with_keys(self):
        """⚠️ BERBAHAYA: Export dengan private key"""
        try:
            # Buat direktori keys (BERBAHAYA!)
            os.makedirs(self.keys_dir, exist_ok=True)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Export session keys
            if self.session_keys:
                keys_file = f"{self.keys_dir}/DANGEROUS_keys_{timestamp}.json"
                
                with open(keys_file, 'w') as f:
                    json.dump(self.session_keys, f, indent=2)
                
                print(f"⚠️ BERBAHAYA: Keys dengan private key di-export ke: {keys_file}")
                print("🚨 SEGERA HAPUS FILE INI SETELAH DIGUNAKAN!")
                print("🚨 JANGAN COMMIT KE GIT!")
            else:
                print("❌ Tidak ada keys di session ini")
                
        except Exception as e:
            print(f"❌ Error export keys: {e}")
    
    def clear_logs(self):
        """Clear semua logs"""
        try:
            if os.path.exists(self.log_file):
                os.remove(self.log_file)
            
            # Clear session
            self.session_keys = []
            
        except Exception as e:
            print(f"❌ Error clearing logs: {e}")

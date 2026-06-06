import json
import os
import base64
import hashlib


class GMDB:
    def __init__(self, filename, password):
        self.filename = filename
        self.password = password
        self.key = self._derive_key(password)
        self.data = {}

        if os.path.exists(filename):
            try:
                self._load()
            except:
                print("[GMDB] Wrong password or corrupted file!")
                raise
        else:
            print("[GMDB] Creating new database...")
            self.data = {}

    # -----------------------------
    # SIMPLE ENCRYPTION SYSTEM
    # -----------------------------
    def _derive_key(self, password):
        return hashlib.sha256(password.encode()).digest()

    def _encrypt(self, text):
        raw = text.encode()
        out = bytes([raw[i] ^ self.key[i % len(self.key)] for i in range(len(raw))])
        return base64.b64encode(out).decode()

    def _decrypt(self, text):
        raw = base64.b64decode(text.encode())
        out = bytes([raw[i] ^ self.key[i % len(self.key)] for i in range(len(raw))])
        return out.decode()

    # -----------------------------
    # INTERNAL FILE OPERATIONS
    # -----------------------------
    def _load(self):
        with open(self.filename, "r") as f:
            enc = f.read().strip()
            dec = self._decrypt(enc)
            self.data = json.loads(dec)

    def save(self):
        raw = json.dumps(self.data)
        enc = self._encrypt(raw)

        # Create backup
        with open(self.filename + ".bak", "w") as b:
            b.write(enc)

        # Save database
        with open(self.filename, "w") as f:
            f.write(enc)

    # -----------------------------
    # PUBLIC FUNCTIONS
    # -----------------------------
    def create_storage(self, name):
        if name not in self.data:
            self.data[name] = {}
            self.save()

    def set(self, storage, key, field, value):
        if storage not in self.data:
            self.data[storage] = {}

        if key not in self.data[storage]:
            self.data[storage][key] = {}

        self.data[storage][key][field] = value
        self.save()

    def get(self, storage, key):
        return self.data[storage].get(key, None)

    def export(self, filename):
        with open(filename, "w") as f:
            json.dump(self.data, f, indent=4)

    def close(self):
        self.save()


# -----------------------------
# PUBLIC FUNCTION FOR IMPORT
# -----------------------------
def open_db(filename, password):
    return GMDB(filename, password)

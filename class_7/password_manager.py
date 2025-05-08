import json
import getpass
from cryptography.fernet import Fernet
import base64
import os
from hashlib import pbkdf2_hmac
import secrets
import string
from typing import Dict, Optional, List

class PasswordGenerator:
    """Handles password generation functionality"""
    def __init__(self, length: int = 16):
        self.length = length
    
    def generate(self, use_symbols: bool = True) -> str:
        """Generate a strong random password"""
        chars = string.ascii_letters + string.digits
        if use_symbols:
            chars += string.punctuation
        
        while True:
            password = ''.join(secrets.choice(chars) for _ in range(self.length))
            if (any(c.islower() for c in password)
                    and any(c.isupper() for c in password)
                    and any(c.isdigit() for c in password)
                    and (not use_symbols or any(c in string.punctuation for c in password))):
                return password

class EncryptionManager:
    """Handles encryption and decryption of passwords"""
    def __init__(self, master_password: str):
        self.key = self._derive_key(master_password)
    
    @staticmethod
    def _derive_key(master_password: str, salt: bytes = b'salt_', iterations: int = 100000) -> bytes:
        """Derive encryption key from master password"""
        kdf = pbkdf2_hmac(
            'sha256',
            master_password.encode(),
            salt,
            iterations
        )
        return base64.urlsafe_b64encode(kdf)
    
    def encrypt(self, data: str) -> str:
        """Encrypt sensitive data"""
        fernet = Fernet(self.key)
        return fernet.encrypt(data.encode()).decode()
    
    def decrypt(self, encrypted_data: str) -> str:
        """Decrypt sensitive data"""
        fernet = Fernet(self.key)
        return fernet.decrypt(encrypted_data.encode()).decode()

class PasswordEntry:
    """Represents a single password entry"""
    def __init__(self, service: str, username: str, password: str):
        self.service = service
        self.username = username
        self.password = password
    
    def to_dict(self) -> Dict[str, str]:
        """Convert entry to dictionary for storage"""
        return {
            'service': self.service,
            'username': self.username,
            'password': self.password
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, str]):
        """Create entry from dictionary"""
        return cls(data['service'], data['username'], data['password'])

class PasswordManager:
    """Main password manager class"""
    def __init__(self, data_file: str = 'passwords.json'):
        self.data_file = data_file
        self.entries: List[PasswordEntry] = []
        self.encryption_manager: Optional[EncryptionManager] = None
    
    def initialize(self, master_password: str):
        """Initialize the manager with master password"""
        self.encryption_manager = EncryptionManager(master_password)
        if os.path.exists(self.data_file):
            self._load_entries()
    
    def _load_entries(self):
        """Load entries from file"""
        with open(self.data_file, 'r') as f:
            encrypted_data = json.load(f)
        
        decrypted_data = self.encryption_manager.decrypt(encrypted_data['data'])
        self.entries = [PasswordEntry.from_dict(entry) for entry in json.loads(decrypted_data)]
    
    def _save_entries(self):
        """Save entries to file"""
        entries_data = [entry.to_dict() for entry in self.entries]
        encrypted_data = self.encryption_manager.encrypt(json.dumps(entries_data))
        
        with open(self.data_file, 'w') as f:
            json.dump({'data': encrypted_data}, f)
    
    def add_entry(self, service: str, username: str, password: str):
        """Add a new password entry"""
        self.entries.append(PasswordEntry(service, username, password))
        self._save_entries()
    
    def get_entry(self, service: str) -> Optional[PasswordEntry]:
        """Retrieve a password entry by service name"""
        for entry in self.entries:
            if entry.service.lower() == service.lower():
                return entry
        return None
    
    def list_services(self) -> List[str]:
        """List all stored services"""
        return [entry.service for entry in self.entries]

class PasswordManagerCLI:
    """Command Line Interface for the Password Manager"""
    def __init__(self):
        self.manager = PasswordManager()
        self.password_generator = PasswordGenerator()
    
    def run(self):
        """Run the CLI interface"""
        print("=== Password Manager ===")
        
        # Initialize with master password
        master_password = getpass.getpass("Enter master password: ")
        self.manager.initialize(master_password)
        
        while True:
            print("\nOptions:")
            print("1. Store new password")
            print("2. Retrieve password")
            print("3. Generate strong password")
            print("4. List all services")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self._store_password()
            elif choice == '2':
                self._retrieve_password()
            elif choice == '3':
                self._generate_password()
            elif choice == '4':
                self._list_services()
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def _store_password(self):
        """Handle storing new password"""
        service = input("Enter service name: ")
        username = input("Enter username: ")
        password = getpass.getpass("Enter password (leave empty to generate): ")
        
        if not password:
            use_symbols = input("Include symbols in password? (y/n): ").lower() == 'y'
            password = self.password_generator.generate(use_symbols)
            print(f"Generated password: {password}")
        
        self.manager.add_entry(service, username, password)
        print("Password stored successfully!")
    
    def _retrieve_password(self):
        """Handle password retrieval"""
        service = input("Enter service name: ")
        entry = self.manager.get_entry(service)
        
        if entry:
            print(f"\nService: {entry.service}")
            print(f"Username: {entry.username}")
            print(f"Password: {entry.password}")
        else:
            print("No entry found for that service.")
    
    def _generate_password(self):
        """Handle password generation"""
        length = int(input("Enter password length (default 16): ") or 16)
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        self.password_generator.length = length
        password = self.password_generator.generate(use_symbols)
        print(f"\nGenerated password: {password}")
    
    def _list_services(self):
        """List all stored services"""
        services = self.manager.list_services()
        if services:
            print("\nStored services:")
            for service in services:
                print(f"- {service}")
        else:
            print("No services stored yet.")

if __name__ == "__main__":
    cli = PasswordManagerCLI()
    cli.run()





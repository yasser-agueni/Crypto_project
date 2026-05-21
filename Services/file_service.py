import os
from Security.symmetric import rc4

class FileService:

    def __init__(self, password_service):

        self.password_service = password_service

        self.folder = "Files"

        if not os.path.exists(self.folder):

            os.makedirs(self.folder)

    # =====================================
    # SAVE ENCRYPTED FILE
    # =====================================

    def save_encrypted_file(
        self,
        filename,
        content,
        key
    ):

        encrypted = (
            self.password_service.encrypt_rc4(
                content,
                key
            )
        )

        path = (
            f"{self.folder}/{filename}"
        )

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(encrypted)

        print(
            "Fichier chiffré sauvegardé"
        )

    # =====================================
    # READ ENCRYPTED FILE
    # =====================================

    def read_encrypted_file(
        self,
        filename,
        key
    ):

        path = (
            f"{self.folder}/{filename}"
        )

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            encrypted = f.read()

        decrypted = (
            self.password_service.decrypt_rc4(
                encrypted,
                key
            )
        )

        return decrypted
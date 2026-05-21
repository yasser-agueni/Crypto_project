from Security.hash import sha1
from Security.hash import sha256

from Security.symmetric import (
    chiffrerCesar,
    dechiffrerCesar,
    chiffrerVigenere,
    dechiffrerVigenere,
    generer_cle,
    cryptage_Vernam,
    decryptage_Vernam,
    rc4
)

from Security.asymmetric import RSAEncryption


class PasswordService:

    def __init__(self):

        self.rsa = RSAEncryption()

    # =====================================
    # SHA1
    # =====================================

    def hash_sha1(self, texte):

        return sha1(texte)

    # =====================================
    # SHA256
    # =====================================

    def hash_sha256(self, texte):

        return sha256(texte)

    # =====================================
    # CESAR
    # =====================================

    def encrypt_cesar(
        self,
        texte,
        decalage
    ):

        return chiffrerCesar(
            texte,
            decalage
        )

    def decrypt_cesar(
        self,
        texte,
        decalage
    ):

        return dechiffrerCesar(
            texte,
            decalage
        )

    # =====================================
    # VIGENERE
    # =====================================

    def encrypt_vigenere(
        self,
        texte,
        cle
    ):

        return chiffrerVigenere(
            texte,
            cle
        )

    def decrypt_vigenere(
        self,
        texte,
        cle
    ):

        return dechiffrerVigenere(
            texte,
            cle
        )

    # =====================================
    # VERNAM
    # =====================================

    def generate_key(self, texte):

        return generer_cle(texte)

    def encrypt_vernam(
        self,
        texte,
        cle
    ):

        return cryptage_Vernam(
            texte,
            cle
        )

    def decrypt_vernam(
        self,
        texte,
        cle
    ):

        return decryptage_Vernam(
            texte,
            cle
        )

    # =====================================
    # RC4
    # =====================================

    def encrypt_rc4(
        self,
        texte,
        cle
    ):

        return rc4(texte, cle)

    def decrypt_rc4(
        self,
        texte,
        cle
    ):

        return rc4(texte, cle)

    # =====================================
    # RSA
    # =====================================

    def encrypt_rsa(self, texte):

        return self.rsa.encrypt(texte)

    def decrypt_rsa(self, texte):

        return self.rsa.decrypt(texte)
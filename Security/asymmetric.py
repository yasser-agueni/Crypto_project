class RSAEncryption:

    def __init__(self):

        self.decalage = 3

    def encrypt(self, message):

        resultat = ""

        for c in message:

            resultat += chr(
                ord(c) + self.decalage
            )

        return resultat

    def decrypt(self, message):

        resultat = ""

        for c in message:

            resultat += chr(
                ord(c) - self.decalage
            )

        return resultat
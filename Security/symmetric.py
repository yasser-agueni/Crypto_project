import random


# ================= CESAR =================


def chiffrerCesar(texte, decalage):

    resultat = ""

    for c in texte.upper():

        if c.isalpha():

            resultat += chr(
                (ord(c) - ord('A') + decalage)
                % 26 + ord('A')
            )

        else:

            resultat += c

    return resultat



def dechiffrerCesar(texte, decalage):

    return chiffrerCesar(
        texte,
        -decalage
    )


# ================= VIGENERE =================


def chiffrerVigenere(texte, cle):

    texte = texte.upper()

    cle = cle.upper()

    resultat = ""

    for i, c in enumerate(texte):

        if c.isalpha():

            t_i = ord(c) - ord('A')

            k_i = ord(
                cle[i % len(cle)]
            ) - ord('A')

            resultat += chr(
                (t_i + k_i)
                % 26 + ord('A')
            )

        else:

            resultat += c

    return resultat



def dechiffrerVigenere(texte, cle):

    texte = texte.upper()

    cle = cle.upper()

    resultat = ""

    for i, c in enumerate(texte):

        if c.isalpha():

            c_i = ord(c) - ord('A')

            k_i = ord(
                cle[i % len(cle)]
            ) - ord('A')

            resultat += chr(
                (c_i - k_i)
                % 26 + ord('A')
            )

        else:

            resultat += c

    return resultat


# ================= VERNAM =================


def generer_cle(message):

    cle = ''

    for i in range(len(message)):

        cle += chr(random.randint(0, 255))

    return cle



def cryptage_Vernam(message, cle):

    chiffre = ''

    for i in range(len(message)):

        chiffre += chr(
            ord(message[i]) ^ ord(cle[i])
        )

    return chiffre



def decryptage_Vernam(chiffre, cle):

    return cryptage_Vernam(
        chiffre,
        cle
    )


# ================= RC4 =================


def rc4(message, cle):

    s = list(range(0, 256))

    j = 0

    for i in range(256):

        j = (
            j + s[i] + cle[i % len(cle)]
        ) % 256

        s[i], s[j] = s[j], s[i]

    i = 0

    j = 0

    resultat = ''

    for caractere in message:

        i = (i + 1) % 256

        j = (j + s[i]) % 256

        s[i], s[j] = s[j], s[i]

        keystream = s[(s[i] + s[j]) % 256]

        resultat += chr(
            ord(caractere) ^ keystream
        )

    return resultat
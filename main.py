from Storage.database import Database

from Services.user_service import UserService
from Services.password_service import PasswordService
from Services.file_service import FileService

from Utils.menu import afficher_menu


# =====================================
# INITIALISATION
# =====================================

password_service = PasswordService()


database = Database()


user_service = UserService(
    database,
    password_service
)


file_service = FileService(
    password_service
)


current_user = None


# =====================================
# MAIN PROGRAM
# =====================================

while True:

    afficher_menu()

    choix = input("\nVotre choix : ")

    # =====================================
    # ADD USER
    # =====================================

    if choix == "1":

        try:

            id = int(input("ID : "))

            nom = input("Nom : ")

            prenom = input("Prenom : ")

            email = input("Email : ")

            password = input(
                "Mot de passe : "
            )

            user_service.create_user(
                id,
                nom,
                prenom,
                email,
                password
            )

        except Exception as e:

            print("Erreur :", e)

    # =====================================
    # LOGIN
    # =====================================

    elif choix == "2":

        email = input("Email : ")

        password = input(
            "Mot de passe : "
        )

        user = user_service.login(
            email,
            password
        )

        if user:

            current_user = user

            print(
                "Connexion réussie"
            )

        else:

            print(
                "Email ou mot de passe incorrect"
            )

    # =====================================
    # SHOW USERS
    # =====================================

    elif choix == "3":

        user_service.show_users()

    # =====================================
    # CESAR
    # =====================================

    elif choix == "4":

        texte = input("Texte : ")

        decalage = int(
            input("Décalage : ")
        )

        chiffre = (
            password_service.encrypt_cesar(
                texte,
                decalage
            )
        )

        print("\nTexte chiffré :")

        print(chiffre)

        print("\nTexte déchiffré :")

        print(
            password_service.decrypt_cesar(
                chiffre,
                decalage
            )
        )

    # =====================================
    # VIGENERE
    # =====================================

    elif choix == "5":

        texte = input("Texte : ")

        cle = input("Clé : ")

        chiffre = (
            password_service.encrypt_vigenere(
                texte,
                cle
            )
        )

        print("\nTexte chiffré :")

        print(chiffre)

        print("\nTexte déchiffré :")

        print(
            password_service.decrypt_vigenere(
                chiffre,
                cle
            )
        )

    # =====================================
    # SHA1
    # =====================================

    elif choix == "6":

        texte = input("Texte : ")

        print(
            password_service.hash_sha1(
                texte
            )
        )

    # =====================================
    # SHA256
    # =====================================

    elif choix == "7":

        texte = input("Texte : ")

        print(
            password_service.hash_sha256(
                texte
            )
        )

    # =====================================
    # RSA
    # =====================================

    elif choix == "8":

        texte = input("Texte : ")

        chiffre = (
            password_service.encrypt_rsa(
                texte
            )
        )

        print("\nMessage chiffré :")

        print(chiffre)

        print("\nMessage déchiffré :")

        print(
            password_service.decrypt_rsa(
                chiffre
            )
        )

    # =====================================
    # SAVE ENCRYPTED FILE
    # =====================================

    elif choix == "9":

        if not current_user:

            print(
                "Connectez-vous d'abord"
            )

            continue

        filename = input(
            "Nom fichier : "
        )

        content = input(
            "Contenu fichier : "
        )

        key = input("Clé : ")

        key = [ord(c) for c in key]

        file_service.save_encrypted_file(
            filename,
            content,
            key
        )

    # =====================================
    # READ ENCRYPTED FILE
    # =====================================

    elif choix == "10":

        if not current_user:

            print(
                "Connectez-vous d'abord"
            )

            continue

        filename = input(
            "Nom fichier : "
        )

        key = input("Clé : ")

        key = [ord(c) for c in key]

        contenu = (
            file_service.read_encrypted_file(
                filename,
                key
            )
        )

        print("\nContenu déchiffré :")

        print(contenu)

    # =====================================
    # UPDATE PASSWORD
    # =====================================

    elif choix == "11":

        email = input("Email : ")

        new_password = input(
            "Nouveau mot de passe : "
        )

        user_service.update_password(
            email,
            new_password
        )

    # =====================================
    # DELETE USER
    # =====================================

    elif choix == "12":

        id = int(
            input("ID utilisateur : ")
        )

        user_service.delete_user(id)

        
    # =====================================
    # QUIT
    # =====================================

    elif choix == "0":

        break

    else:

        print("Choix invalide")

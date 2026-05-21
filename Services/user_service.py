from Models.user import Utilisateur
from Security.hash import sha256

class UserService:

    def __init__(
        self,
        database,
        password_service
    ):

        self.database = database

        self.password_service = password_service

    # =====================================
    # CREATE USER
    # =====================================

    def create_user(
        self,
        id,
        nom,
        prenom,
        email,
        password
    ):

        hashed_password = (
            self.password_service.hash_sha256(
                password
            )
        )

        user = Utilisateur(
            id,
            nom,
            prenom,
            email,
            hashed_password
        )

        self.database.add_user(user)

        print(
            "Utilisateur ajouté"
        )

    # =====================================
    # LOGIN
    # =====================================

    def login(self, email, password):

        user = (
            self.database.find_user_by_email(
                email
            )
        )

        if not user:

            return None

        hashed_password = (
            self.password_service.hash_sha256(
                password
            )
        )

        if user.password_ == hashed_password:

            return user

        return None

    # =====================================
    # DELETE USER
    # =====================================

    def delete_user(self, id):

        self.database.remove_user(id)

    # =====================================
    # SHOW USERS
    # =====================================

    def show_users(self):

        for user in self.database.users:

            print("\n================")

            print("ID :", user.id_)
            print("Nom :", user.nom)
            print("Prenom :", user.prenom)
            print("Email :", user.email)

            print("================")

    

    # =====================================
    # UPDATE PASSWORD
    # =====================================

    def update_password(
        self,
        email,
        new_password
    ):

        user = (
            self.database.find_user_by_email(
                email
            )
        )

        if not user:

            print("Utilisateur introuvable")

            return

        hashed_password = (
            self.password_service.hash_sha256(
                new_password
            )
        )

        user.password_ = hashed_password

        self.database.save_users()

        print("Mot de passe modifié")
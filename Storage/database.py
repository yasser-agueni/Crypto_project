import json
from Models.user import Utilisateur

class Database:

    def __init__(self):

        self.file = "users.json"

        self.users = []

        self.load_users()

    # =====================================
    # LOAD USERS
    # =====================================

    def load_users(self):

        try:

            with open(
                self.file,
                "r",
                encoding="utf-8"
            ) as f:

                data = json.load(f)

                for u in data:

                    user = Utilisateur(
                        u["id"],
                        u["nom"],
                        u["prenom"],
                        u["email"],
                        u["password"]
                    )

                    self.users.append(user)

        except:

            self.users = []

    # =====================================
    # SAVE USERS
    # =====================================

    def save_users(self):

        data = []

        for user in self.users:

            data.append({

                "id": user.id_,
                "nom": user.nom,
                "prenom": user.prenom,
                "email": user.email,
                "password": user.password_
            })

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )

    # =====================================
    # ADD USER
    # =====================================

    def add_user(self, user):

        self.users.append(user)

        self.save_users()

    # =====================================
    # REMOVE USER
    # =====================================

    def remove_user(self, id):

        for user in self.users:

            if user.id_ == id:

                self.users.remove(user)

                self.save_users()

                print("Utilisateur supprimé")

                return

    # =====================================
    # FIND USER BY ID
    # =====================================

    def find_user(self, id):

        for user in self.users:

            if user.id_ == id:

                return user

        return None

    # =====================================
    # FIND USER BY EMAIL
    # =====================================

    def find_user_by_email(self, email):

        for user in self.users:

            if user.email == email:

                return user

        return None
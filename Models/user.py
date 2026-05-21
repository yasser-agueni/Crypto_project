class Utilisateur :

    def __init__(self, id=None, nom=None, prenom=None, email=None, password=None):

        self.id_ = id
        self.nom_ = nom
        self.prenom_ = prenom
        self.email_ = email
        self.password_ = password

    @property
    def nom(self):
        return self.nom_

    @nom.setter
    def nom(self, value):
        self.nom_ = value

    @property
    def prenom(self):
        return self.prenom_

    @prenom.setter
    def prenom(self, value):
        self.prenom_ = value

    @property
    def email(self):
        return self.email_

    @email.setter
    def email(self, value):
        self.email_ = value

    @property
    def password(self):
        return self.password_

    @password.setter
    def password(self, value):

        if len(value) < 4:
            raise ValueError("Mot de passe trop court")

        self.password_ = value      
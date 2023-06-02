class Contact:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def __str__(self) -> str:
        return f"(nome:{self.name}, e-mail:{self.email}, telefone:{self.phone_number})"

    def __repr__(self):
        return self.name


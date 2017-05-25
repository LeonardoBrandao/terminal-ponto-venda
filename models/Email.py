class Email:
    def __init__(self, email):
        self.email = email

    def __str__(self):
        return '{}'.format(self.email)
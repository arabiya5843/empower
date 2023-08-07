from django.db.models import Model, ForeignKey, CASCADE, CharField


# Create a model named UserCard to represent user payment cards
class UserCard(Model):
    # Define a foreign key,py to associate the card with a user.
    # CASCADE option means that if a user is deleted, all their associated cards will also be deleted.
    user = ForeignKey('users.User', CASCADE)

    # CharField to store the card number. Max length is set to 16 and the field is unique.
    card_number = CharField(max_length=16, unique=True)

    # CharField to store the expiration date of the card in MM/YY format.
    expiration_date = CharField(max_length=5)

    # Customize the representation of the model instance as a string.
    def __str__(self):
        return f"{self.card_number} - {self.expiration_date}"

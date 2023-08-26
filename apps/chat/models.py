from django.db.models import TextField, Model, DateTimeField, ForeignKey, CASCADE
from apps.users.models import User


class Chat(Model):
    sender = ForeignKey(User, on_delete=CASCADE, related_name='sent_chats')
    receiver = ForeignKey(User, on_delete=CASCADE, related_name='received_chats')

    def __str__(self):
        return f"{self.sender.username}, {self.receiver.username}"


class Message(Model):
    chat = ForeignKey(Chat, on_delete=CASCADE, related_name='messages')
    sender = ForeignKey(User, on_delete=CASCADE)
    text = TextField()
    timestamp = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.chat}, {self.sender.username}, {self.text}, {self.timestamp}"

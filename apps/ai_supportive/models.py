from django.db.models import TextField, Model, DateTimeField, ForeignKey, CASCADE
from apps.users.models import User


class ChatMessage(Model):
    question = TextField()
    answer = TextField(null=True)
    user = ForeignKey(User, CASCADE)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.question}, {self.answer}, {self.user.username}"

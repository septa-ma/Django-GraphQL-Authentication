from django.core.management.base import BaseCommand
from users.models import NewUser
from datetime import timedelta, date

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        today = date.today()
        users = NewUser.objects.filter(is_active=False)
        
        for user in users:
            start_date = user.created_at.date()
            end_date = start_date + timedelta(days=3)

            if end_date < today:
                NewUser.objects.get(pk=user.id).delete()
                print(f'deleted user is: {user.first_name}')
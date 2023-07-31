from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
     Команда суперпользователя
    """

    def handle(self, *args, **options):

        user = User.objects.create(
            email='q@q.ru',
            first_name='Admin',
            last_name='Temp',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('12345')
        user.save()

from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'

#Note: Import the signals to the ready function
    def ready(self):
        import users.signals
from django.apps import AppConfig


class CategoryConfig(AppConfig):
    name = 'category'

    def ready(self):
        print(self.__class__.__name__ + ' is ready')
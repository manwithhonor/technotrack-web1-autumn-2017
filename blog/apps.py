from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        print(self.__class__.__name__ + ' is ready')

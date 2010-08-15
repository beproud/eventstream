from django.dispatch import Signal

logout_done = Signal(providing_args=["request"])

from inspect import signature

from django.apps import AppConfig


class Config(AppConfig):
    name = "oeidc"

    def ready(self):
        from sentry import auth

        from .provider import OEIDCProvider

        # In Sentry 25.3.0, the signature of `ProviderManager.register()` changed:
        # Instead of providing the key as a parameter, it is now expected to be a
        # property of the provider class.
        if len(signature(auth.register).parameters) == 1:
            auth.register(OEIDCProvider)
        else:
            auth.register("oeidc", OEIDCProvider)

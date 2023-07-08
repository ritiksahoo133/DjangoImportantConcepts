from django.contrib.auth.signals import (
    user_logged_in,
    user_logged_out,
    user_login_failed,
)
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import (
    pre_init,
    pre_delete,
    pre_save,
    post_save,
    post_delete,
    post_init,
)
from django.core.signals import request_started, request_finished, got_request_exception


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("------------------------------------")
    print("Logged-in signal.. Run Intro")
    print("Sender:", sender)
    print("User:", user.password)
    print("Request:", request)
    print(f"kwargs:{kwargs}")


# user_logged_in.connect(login_success, sender=User)
@receiver(user_logged_out, sender=User)
def log_out(sender, request, user, **kwargs):
    print("------------------------------------")
    print("Logged-out signal.. Run outro")
    print("Sender:", sender)
    print("User:", user)
    print("Request:", request)
    print(f"kwargs:{kwargs}")


# user_logged_out.connect(log_out, sender=User)
@receiver(user_login_failed)
def login_failed(sender, request, credentials, **kwargs):
    print("------------------------------------")
    print("Logged-in failed signal.. Run failed")
    print("Sender:", sender)
    print("Credentials:", credentials)
    print("Request:", request)
    print(f"kwargs:{kwargs}")


# user_login_failed.connect(login_failed)
@receiver(pre_save, sender=User)
def at_beggining_save(sender, instance, **kwargs):
    print("------------------------------------")
    print("Pre-save signals")
    print("Sender:", sender)
    print("instance:", instance)
    print(f"kwargs:{kwargs}")


# post_save
@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        print("----------------New Record--------------------")
        print("Post-save signals")
        print("Sender:", sender)
        print("instance:", instance)
        print("created:", created)
        print(f"kwargs:{kwargs}")
    else:
        print("----------------update--------------------")
        print("Post-save signals")
        print("Sender:", sender)
        print("instance:", instance)
        print("created:", created)
        print(f"kwargs:{kwargs}")


# pre_delete
@receiver(pre_delete, sender=User)
def at_pre_delete(sender, instance, **kwargs):
    print("------------------------------------")
    print("Pre-delete signals")
    print("Sender:", sender)
    print("instance:", instance)
    print(f"kwargs:{kwargs}")


# post_delete
@receiver(pre_delete, sender=User)
def at_post_delete(sender, instance, **kwargs):
    print("------------------------------------")
    print("Post-delete signals")
    print("Sender:", sender)
    print("instance:", instance)
    print(f"kwargs:{kwargs}")


# pre_init
@receiver(pre_init, sender=User)
def at_pre_init(sender, *args, **kwargs):
    print("------------------------------------")
    print("Pre-init signals")
    print("Sender:", sender)
    print("args:", args)
    print(f"kwargs:{kwargs}")


# post_init
@receiver(post_init, sender=User)
def at_pre_init(sender, *args, **kwargs):
    print("------------------------------------")
    print("Post-init signals")
    print("Sender:", sender)
    print("args:", args)
    print(f"kwargs:{kwargs}")


@receiver(
    request_started,
)
def at_beggining_request(sender, environ, **kwargs):
    print("------------------------------------")
    print("request start signals")
    print("Sender:", sender)
    print("Environ:", environ)
    print(f"kwargs:{kwargs}")


@receiver(request_finished)
def at_ending_request(sender, environ, **kwargs):
    print("------------------------------------")
    print("request finished signals")
    print("Sender:", sender)
    print("Environ:", environ)
    print(f"kwargs:{kwargs}")


@receiver(got_request_exception)
def at_ending_request(sender, request, **kwargs):
    print("------------------------------------")
    print("Exception signals")
    print("Sender:", sender)
    print("request:", request)
    print(f"kwargs:{kwargs}")

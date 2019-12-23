from allauth.account.models import EmailAddress
from django.core.exceptions import ObjectDoesNotExist


def is_email_verified(user):
    """
    Helper method to determine if the user's default email is verified
    Args:
        user: User object

    Returns: <bool> True/False
    """
    try:
        return EmailAddress.objects.get(user=user, email=user.email).verified
    except ObjectDoesNotExist:
        return False


from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.exceptions import ImmediateHttpResponse
from django.contrib.auth import get_user_model

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user
        if not user.email:
            return

        try:
            existing_user = get_user_model().objects.get(email=user.email)
            sociallogin.connect(request, existing_user)
        except get_user_model().DoesNotExist:
            pass  # No existing user, continue as normal

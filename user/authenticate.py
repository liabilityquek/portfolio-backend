import jwt
import django
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework import exceptions
from django.conf import settings
from urllib.request import urlopen
import json
from django.utils.encoding import smart_str
django.utils.encoding.smart_text = smart_str
from jose import jwt, jwk
from jose.utils import base64url_decode
from django.utils.translation import gettext_lazy as _
from jose.constants import ALGORITHMS
from .models import UserData

# from rest_framework.authentication import CSRFCheck
# from rest_framework import exceptions

# def enforce_csrf(request):
#     check = CSRFCheck()
#     check.process_request(request)
#     reason = check.process_view(request, None, (), {})
#     if reason:
#         raise exceptions.PermissionDenied('CSRF Failed: %s' % reason)

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or smart_str(auth[0].lower()) != "bearer":
            return None

        token = auth[1]

        # You will also need your Auth0 Domain.
        AUTH0_DOMAIN = settings.AUTH0_DOMAIN
        jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
        jwks = json.loads(jsonurl.read())
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks['keys']:
            if key['kid'] == unverified_header['kid']:
                rsa_key = {
                    'kty': key['kty'],
                    'kid': key['kid'],
                    'use': key['use'],
                    'n': key['n'],
                    'e': key['e'],
                }
        if rsa_key:
            try:
                key = jwk.construct(rsa_key, ALGORITHMS.RS256)
                header, payload, encoded_signature = token.decode().split('.')
                message = f"{header}.{payload}"
                # print(message)
                decoded_signature = base64url_decode(encoded_signature.encode())
                if not key.verify(message.encode(), decoded_signature):
                    raise exceptions.AuthenticationFailed("Signature verification failed")
                claims = jwt.get_unverified_claims(token)
                # print(claims)
                try:
                    user = UserData.objects.get(name=claims['name'])
                    # print("Sub claim from the token:", claims['name'])

                except UserData.DoesNotExist:
                    raise exceptions.AuthenticationFailed('User does not exist')
                # Now 'claims' contains the payload of the decoded JWT token

                # You can fetch the user based on the 'sub' claim which contains the user's id.
                # user = User.objects.get(id=claims['sub'])

                return (user, token)
            except jwt.JWTError:
                msg = _("Error decoding signature.")
                raise exceptions.AuthenticationFailed(msg)
        return None
from django.contrib.auth.hashers import (
    mask_hash,
    make_password,
    check_password,
    PBKDF2PasswordHasher,
)


class PassworHasher(PBKDF2PasswordHasher):
    """
    <algorithm>$<iterations>$<salt>$<hash>
    https://docs.djangoproject.com/en/5.2/topics/auth/passwords/
    """

    def hasher(self, password, salt_, iterations=None):
        hashed_password = make_password(password, salt=salt_)
        # mask_password_chash = mask_hash(hashed_password)
        return hashed_password

    # def hasher_check(self, password, salt, hashed_password):
    #     result = check_password(password, hashed_password)
    #     return result

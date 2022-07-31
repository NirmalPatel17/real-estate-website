from django.contrib.auth.base_user import BaseUserManager
# from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    use_in_migration = True


    def create_user(self, email, password=None, **extra_fileds):
        
        if not email:
            raise ValueError('Email is require')
        
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fileds)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class Timecolumn(models.Model):
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email), # 회원가입시 email 형식에 대한 validation 실시
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # py manage.py createsuperuser 시에 사용하는 메소드 오버라이딩
    def create_superuser(self, email, nickname, password):
        
        user = self.create_user(
            email=email,
            password=password,
            nickname=nickname,
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser, PermissionsMixin, Timecolumn):
    email = models.EmailField(
        db_column='user_email',
        verbose_name=_('user_email'),
        max_length=50,
        unique=True,
    )
    nickname = models.TextField(
        db_column='user_nickname',
        verbose_name=_('user_nickname'),
        unique=True,
    )
    name = models.CharField(
        db_column='user_name',
        verbose_name=_('user_name'),
        max_length=20,
        unique=False
    )
    
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', 'name',]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-created_date',) # 빨리 가입한 사람부터 정렬

    def __str__(self):
        return self.nickname


    # def get_short_name(self):
    #     return self.nickname
    
    
    def get_full_name(self):        
        return self.nickname

    @property
    def is_staff(self):
        return self.is_superuser

    get_full_name.short_description = _('Full name')
    
    
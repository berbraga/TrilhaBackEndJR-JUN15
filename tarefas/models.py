from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Manager para o modelo de usuário personalizado
class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Usuários precisam de um email')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(
            email,
            name=name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    # Campos extras para gerenciar permissões
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    # Métodos adicionais para permissões
    @property
    def is_staff(self):
        return self.is_admin


class Tarefa(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relacionamento com User

    def __str__(self):
        return self.nome

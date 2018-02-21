from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def check_if_name_exists(value):
	if User.objects.filter(username=value).exists():
		raise ValidationError("Username aldready exists")
	else:
		return value
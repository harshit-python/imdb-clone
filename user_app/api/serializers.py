from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )  # write only means user cannot read it

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # overriding save() method
    def save(self, **kwargs):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError(
                {
                    'error': 'password and password2 should be same!'
                }
            )

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError(
                {
                    'error': 'Provided email is already registered with some other account'
                }
            )

        # creating user
        account = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        # setting password
        account.set_password(password)
        account.save()
        return account

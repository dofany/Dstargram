from django.contrib.auth.models import User
from django import forms

class SignUpForm(forms.ModelForm):
    password = forms.CharField(label = 'password', widget=forms.PasswordInput)
    Repeat_password = forms.CharField(label='Repeat_password', widget=forms.PasswordInput)

    class Meta:
        model = User
        # fields에는 해당 모델에 대해 입력받을 필드들을 나열한다.
        # + 추가 필드도 포함 될 수 있다.
        fields = ['username','password', 'first_name','last_name','email',]

    def clean_Repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['Repeat_password']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        return cd['Repeat_password']
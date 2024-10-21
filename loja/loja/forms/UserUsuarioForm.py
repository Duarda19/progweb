from django.forms import ModelForm
from django import forms
from loja.models.Usuario import Usuario
class UserUsuarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserUsuarioForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.perfil != 1:
            del self.fields['perfil']
    class Meta:
        model = Usuario
        fields = ['user', 'perfil', 'aniversario']
        # Usamos '__all__' para exibir todos os campos do formulário
        # fields = '__all__'
        # Usamos uma lista para exibir campos específicos
        # fields = ['pub_date', 'headline', 'content', 'reporter']
        # Usamos exclude para excluir campos específicos do sistema
        # exclude = ['']
        widgets = {'user': forms.HiddenInput(), 'perfil': forms.Select(attrs={'class': "form-control"}), 'aniversario': forms.DateInput(attrs={'class': "form-control", "type": "date"})}
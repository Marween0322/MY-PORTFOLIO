from django import forms  
from myapp.models import Employee  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewEmployeeForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Employee
        # specify fields to be used
    #     fields = ['loc', 'fund', 'desc', 'cont', 'proj_profile', 'proj_stat'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
    #     widgets = { 'loc': forms.TextInput(attrs={ 'class': 'form-control' }), 
    #                'desc': forms.Textarea(attrs={'rows':1, 'cols':44}),
    #                'fund': forms.Textarea(attrs={'rows':1, 'cols':44}),
    #                'cont': forms.Textarea(attrs={'rows':1, 'cols':44}),
    #                'proj_profile': forms.Textarea(attrs={'rows':1, 'cols':44}),
    #                'proj_comment': forms.Textarea(attrs={'rows':1, 'cols':44}),
    #                'agency': forms.Textarea(attrs={'rows':1, 'cols':44}),
    #                'cert': forms.Textarea(attrs={'rows':1, 'cols':44}),
                   
    #             #    'proj_stat': forms.Textarea(attrs={'rows':4, 'cols':15}),
    #         # 'desc': forms.TextInput(attrs={ 'class': 'form-control' }),
    #         # 'fund': forms.TextInput(attrs={ 'class': 'form-control' }),
            
    #   }
        fields = '__all__'
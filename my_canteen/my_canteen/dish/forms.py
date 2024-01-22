from django import forms


class ChooseTableForm(forms.Form):
    table_numbers = forms.CharField(
        label="桌号", max_length=20, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': "table_number", 'autofocus': ''})
    )
    quantity = forms.CharField(
        label="份数",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "quantity", 'autofocus': ''})
    )


class EvaluateForm(forms.Form):
    evaluation_star = forms.CharField(
        label="星级", max_length=20, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': "evaluation_star", 'autofocus': ''})
    )
    content = forms.CharField(
        label="内容",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': "content", 'autofocus': '', 'rows': 4})
    )

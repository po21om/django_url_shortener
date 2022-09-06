from django.forms import ModelForm
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView
from shortener_app.models import AliasedUrl


def redirect_view(req, alias):
    try:
        aliased_url = AliasedUrl.objects.get(alias=alias)
        return redirect(aliased_url.url)
    except AliasedUrl.DoesNotExist:
        raise Http404("There is no such alias.")


class AliasedUrlForm(ModelForm):
    class Meta:
        model = AliasedUrl
        fields = ["url"]


class AliasCreateView(CreateView):
    form_class = AliasedUrlForm
    template_name = "create_alias.html"

    def get_success_url(self):
        return f"{reverse('create')}?created_alias={self.object.alias}"

from django.views.generic import TemplateView
from apps.post.models import Post


class HomeView(TemplateView):
    template_name = "Index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mas_nuevos"] = Post.objects.order_by("-create_at")[:3]
        context["nuevos"] = Post.objects.filter(category="2")[:3]
        context["usados"] = Post.objects.filter(category="1")[:3]
        context["reparar"] = Post.objects.filter(category="4")[:3]
        return context


class helpCenterView(TemplateView):
    template_name = "help_center.html"


class howToBuyView(TemplateView):
    template_name = "how_to_buy.html"


class howToSellView(TemplateView):
    template_name = "how_to_sell.html"


class TermsAndConditionsView(TemplateView):
    template_name = "terms_and_conditions.html"

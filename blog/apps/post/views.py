from django.views.generic import TemplateView

# Create your views here.
class PostDetailView(TemplateView):
    template_name = "post/post_detail.html"
from django.views.generic import TemplateView, ListView
from apps.post.models import *
from apps.post.forms import PostFilterForm


class PostListView(ListView):
    model = Post
    template_name = "post/post_list.html"
    context_object_name = "posts"

    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = PostFilterForm(self.request.GET)

        if context.get("is_paginated", False):
            query_params = self.request.GET.copy()
            query_params.pop("page", None)

            pagination = {}
            page_obj = context["page_obj"]
            paginator = context["paginator"]

            if page_obj.number > 1:
                pagination["first_page"] = (
                    f"?{query_params.urlencode()}&page={paginator.page_range[0]}"
                )

            if page_obj.has_previous():
                pagination["previous_page"] = (
                    f"?{query_params.urlencode()}&page={page_obj.number -1}"
                )

            if page_obj.has_next():
                pagination["next_page"] = (
                    f"?{query_params.urlencode()}&page={page_obj.number +1}"
                )

            if page_obj.number < paginator.num_pages:
                pagination["last_page"] = (
                    f"?{query_params.urlencode()}&page={paginator.num_pages}"
                )
            context["pagination"] = pagination

        return context


class PostDetailView(TemplateView):
    template_name = "post/post_detail.html"


class PostCreateView(TemplateView):
    template_name = "post/post_detail.html"


class PostUpdateView(TemplateView):
    template_name = "post/post_detail.html"


class PostDeleteView(TemplateView):
    template_name = "post/post_detail.html"

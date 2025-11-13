from django.views.generic import TemplateView, ListView, CreateView
from django.db.models import Count, Q
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.post.models import *
from apps.post.forms import PostFilterForm, PostForm
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post
    template_name = "post/post_list.html"
    context_object_name = "posts"

    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("search_query", "")
        order_by = self.request.GET.get("order_by", "-create_at")

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query)
                | Q(author__username__icontains=search_query)
                | Q(content__icontains=search_query)
                | Q(category__name__icontains=search_query)
            )
        return queryset.order_by(order_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = PostFilterForm(self.request.GET)
        context["categories"] = Category.objects.all()

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


print("Este es el error: ", PostForm)


class PostDetailView(TemplateView):
    template_name = "post/post_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "post/post_create.html"
    success_url = reverse_lazy("post:post_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        image_file = self.request.FILES.get("image")

        if image_file:
            PostImage.objects.create(post=self.object, image=image_file)

        return response


class PostUpdateView(TemplateView):
    template_name = "post/post_detail.html"


class PostDeleteView(TemplateView):
    template_name = "post/post_detail.html"


class MyPostView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "post/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

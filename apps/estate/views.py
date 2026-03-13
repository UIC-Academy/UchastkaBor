from django.shortcuts import render
from django.views.generic import TemplateView

from apps.estate.models import Estate, EstateAgent
from apps.blog.models import Post


def home(request):
    estates = (
        Estate.objects.prefetch_related("images")
        .filter(is_featured=True)
        .order_by("-price")[:3]
    )
    properties = (
        Estate.objects.prefetch_related("images").all().order_by("-created_at")[:4]
    )
    agents = (
        EstateAgent.objects.select_related("avatar").order_by("-rating")[:3]
    )
    posts = (
        Post.objects.select_related("image").order_by("-created_at")[:4]
    )

    context = {
        "estates": estates,
        "properties": properties,
        "agents": agents,
        "posts": posts
    }
    return render(request, "estate/index.html", context=context)


def about(request):
    return render(request, "about.html")


class PropertyView(TemplateView):
    template_name = "property-grid.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["estates"] = Estate.objects.prefetch_related("images").all()
        return context


class BlogListView(TemplateView):
    template_name = "blog-grid.html"


class PropertySingleView(TemplateView):
    template_name = "property-single.html"


class BlogSingleView(TemplateView):
    template_name = "blog-single.html"


class AgentListView(TemplateView):
    template_name = "agent-grid.html"


class AgentSingleView(TemplateView):
    template_name = "agent-single.html"


class ContactView(TemplateView):
    template_name = "contact.html"

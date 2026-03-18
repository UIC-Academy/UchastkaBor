from django.urls import path

from apps.estate.views import (
    home,
    about,
    PropertyView,
    PropertySingleView,
    EstateAgentCommentHandlerView,
    AgentListView,
    AgentSingleView,
    ContactView,
)


urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("properties/", PropertyView.as_view(), name="properties"),
    path(
        "properties/<slug:slug>/", PropertySingleView.as_view(), name="property-single"
    ),
    path("properties/agent/comment/", EstateAgentCommentHandlerView.as_view(), name="estate-agent-comment-handler"),
    path("agents/", AgentListView.as_view(), name="agents"),
    path("agents/<slug:slug>/", AgentSingleView.as_view(), name="agent-single"),
    path("contact/", ContactView.as_view(), name="contact"),
]

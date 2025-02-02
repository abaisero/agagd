from agagd_core.views import core as agagd_views
from agagd_core.views.all_chapters import AllChaptersPageView
from agagd_core.views.all_players import AllPlayersPageView
from agagd_core.views.all_tournaments import AllTournamentsPageView
from agagd_core.views.api import ApiGameCountView, ApiPlayerRatings, ApiStatusView
from agagd_core.views.chapter_profile import ChaptersProfilePageView
from agagd_core.views.frontpage import FrontPageView
from agagd_core.views.players_profile import PlayersProfilePageView
from agagd_core.views.qualifications import QualificationsPageView
from agagd_core.views.ratings_overview import RatingsOverviewPageView
from agagd_core.views.search import SearchView
from agagd_core.views.tournament_detail import TournamentDetailPageView
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    path("", FrontPageView.as_view(), name="frontpage_view"),
    path("api/games/count/daily/", ApiGameCountView.as_view(), name="game_stats"),
    path("api/status/", ApiStatusView.as_view(), name="api_status_view"),
    path(
        "api/ratings/<int:player_id>/<int:time_period>/",
        ApiPlayerRatings.as_view(),
        name="member_ratings",
    ),
    path("chapters/", AllChaptersPageView.as_view(), name="all_chapters_page_view"),
    path(
        "chapter/<int:chapter_id>/",
        ChaptersProfilePageView.as_view(),
        name="chapter_detail",
    ),
    path(
        "chapter/<str:chapter_code>/",
        agagd_views.chapter_code_redirect,
        name="chapter_code_redirect",
    ),
    path("players/", AllPlayersPageView.as_view(), name="players_list"),
    path(
        "player/<int:player_id>/",
        PlayersProfilePageView.as_view(),
        name="players_profile",
    ),
    path(
        "ratings/overview/",
        RatingsOverviewPageView.as_view(),
        name="ratings_overview_page_view",
    ),
    path(
        "ratings/qualifications/",
        QualificationsPageView.as_view(),
        name="qualifications_page_view",
    ),
    path("search/", SearchView.as_view(), name="search"),
    path("search/q<str:query>/", SearchView.as_view(), name="search"),
    path(
        "tournaments/",
        AllTournamentsPageView.as_view(),
        name="all_tournaments_page_view",
    ),
    path(
        "tournament/<slug:code>/",
        TournamentDetailPageView.as_view(),
        name="tournament_detail",
    ),
    url(r".php$", RedirectView.as_view(url=reverse_lazy("index"))),
]

# DebugToolbar URL Configuration
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

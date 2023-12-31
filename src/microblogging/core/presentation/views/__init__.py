from .authentication import authentication_controller, logout_controller
from .index import index_controller
from .notification import get_user_notifications_controller
from .profile import (
    adding_a_follower_profile_controller,
    edit_field_profile_controller,
    follower_profile_removal_controller,
    get_followers_profile_controller,
    my_profile_controller,
    profile_edit_controller,
    profile_users_controller,
    receiving_profile_followings_controller,
)
from .registration import (
    registration_confirmations_controller,
    registrations_controller,
)
from .search_twit_by_tag import get_twits_by_tag_controller
from .trending_in_your_country import trending_in_your_country_controller
from .twits import (
    add_a_twits_controller,
    create_answer_to_twit_controller,
    edit_twit_controller,
    twit_deletion_controller,
    view_twits_controller,
)
from .twits_likes import add_like_the_twit_controller, deleting_a_twit_likes_controller
from .twits_repost import (
    adding_a_tweet_repost_controller,
    twit_repost_deletion_controller,
)

__all__ = [
    "index_controller",
    "registrations_controller",
    "authentication_controller",
    "logout_controller",
    "profile_controller",
    "profile_users_controller",
    "receiving_profile_followings_controller",
    "get_followers_profile_controller",
    "profile_edit_controller",
    "edit_field_profile_controller",
    "adding_a_follower_profile_controller",
    "add_a_twits_controller",
    "view_twits_controller",
    "twit_deletion_controller",
    "add_like_the_twit_controller",
    "adding_a_tweet_repost_controller",
    "create_answer_to_twit_controller",
    "edit_twit_controller",
    "registration_confirmations_controller",
    "deleting_a_twit_likes_controller",
    "twit_repost_deletion_controller",
    "follower_profile_removal_controller",
    "my_profile_controller",
    "get_twits_by_tag_controller",
    "trending_in_your_country_controller",
    "get_user_notifications_controller",
]

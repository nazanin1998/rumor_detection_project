class User:
    def __init__(self, id, verified, friends_count, statuses_count, listed_count, followers_count, follow_request_sent,
                 default_profile_image, profile_text_color, favourites_count,
                 profile_use_background_image, profile_image_url_https,
                 profile_background_image_url_https, profile_sidebar_fill_color, description):
        self.id = id
        self.verified = verified
        self.statuses_count = statuses_count
        self.friends_count = friends_count
        self.favourites_count = favourites_count
        self.description = description
        self.listed_count = listed_count
        self.followers_count = followers_count
        self.profile_text_color = profile_text_color
        self.follow_request_sent = follow_request_sent
        self.default_profile_image = default_profile_image
        self.profile_image_url_https = profile_image_url_https
        self.profile_sidebar_fill_color = profile_sidebar_fill_color
        self.profile_use_background_image = profile_use_background_image
        self.profile_background_image_url_https = profile_background_image_url_https

    @staticmethod
    def from_json(js_obj):
        id = js_obj['id_str']
        verified = js_obj['verified']
        description = js_obj['description']
        statuses_count = js_obj['statuses_count']
        friends_count = js_obj['friends_count']
        favourites_count = js_obj['favourites_count']
        listed_count = js_obj['listed_count']
        followers_count = js_obj['followers_count']
        # profile_location = js_obj['profile_location']
        profile_text_color = js_obj['profile_text_color']
        follow_request_sent = js_obj['follow_request_sent']
        default_profile_image = js_obj['default_profile_image']
        profile_image_url_https = js_obj['profile_image_url_https']
        profile_sidebar_fill_color = js_obj['profile_sidebar_fill_color']
        profile_use_background_image = js_obj['profile_use_background_image']
        profile_background_image_url_https = js_obj['profile_background_image_url_https']

        return User(id=id, verified=verified, description=description, statuses_count=statuses_count,
                    friends_count=friends_count, favourites_count=favourites_count, listed_count=listed_count,
                    followers_count=followers_count,
                    profile_text_color=profile_text_color, follow_request_sent=follow_request_sent,
                    default_profile_image=default_profile_image, profile_image_url_https=profile_image_url_https,
                    profile_sidebar_fill_color=profile_sidebar_fill_color,
                    profile_use_background_image=profile_use_background_image,
                    profile_background_image_url_https=profile_background_image_url_https)
#   "user": {
#     "friends_count": 2268,
#     "location": "",
#     "profile_link_color": "1F527B",
#     "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1497949200\/DanielSandfordSmall_normal.jpg",
#     "following": false,
#     "geo_enabled": true,
#     "profile_location"
#     "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/331658004\/1360223450",
#     "profile_background_image_url": "http:\/\/pbs.twimg.com\/profile_background_images\/337316083\/bbc_twitter_template1280.jpg",
#     "name": "Daniel Sandford",
#     "lang": "en",
#     "profile_background_tile": false,
#     "favourites_count": 0,
#     "screen_name": "BBCDanielS",
#     "notifications": false,
#     "url": "http:\/\/t.co\/tPNR3GoVZJ",
#     "created_at": "Fri Jul 08 14:32:54 +0000 2011",
#     "contributors_enabled": false,
#     "time_zone": "Moscow",
#     "protected": false,
#     "default_profile": false,
#     "is_translator": false
#     "entities": {
#       "url": {
#         "urls": [
#           {
#             "url": "http:\/\/t.co\/tPNR3GoVZJ",
#             "indices": [
#               0,
#               22
#             ],
#             "expanded_url": "http:\/\/news.bbc.co.uk",
#             "display_url": "news.bbc.co.uk"
#           }
#         ]
#       },
#       "description": {
#         "urls": []
#       }
#     },
#     "profile_sidebar_border_color": "CCCCCC",
#     "id_str": "331658004",
#     "profile_background_color": "FFFFFF",
#     "is_translation_enabled": false,
#     "utc_offset": 14400,

#   },

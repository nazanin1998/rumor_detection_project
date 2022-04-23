from lib.models.user import User


class Tweet:
    def __init__(self, id, source, favorited, retweeted, in_reply_to_user_id, retweet_count, contributors, text,
                 in_reply_to_status_id, created_at, favorite_count, user):
        self.id = id
        self.text = text
        self.user = user
        self.source = source
        self.favorited = favorited
        self.retweeted = retweeted
        self.created_at = created_at
        self.retweet_count = retweet_count
        self.contributors = contributors
        self.favorite_count = favorite_count
        self.in_reply_to_user_id = in_reply_to_user_id
        self.in_reply_to_status_id = in_reply_to_status_id

    @staticmethod
    def from_json(js_obj):
        id = js_obj['id_str']
        text = js_obj['text']
        source = js_obj['source']
        user = User.from_json(js_obj['user'])
        favorited = js_obj['favorited']
        retweeted = js_obj['retweeted']
        created_at = js_obj['created_at']
        retweet_count = js_obj['retweet_count']
        contributors = js_obj['contributors']
        favorite_count = js_obj['favorite_count']
        in_reply_to_user_id = js_obj['in_reply_to_user_id']
        in_reply_to_status_id = js_obj['in_reply_to_status_id']

        return Tweet(id=id, text=text, source=source, user=user, favorited=favorited, retweeted=retweeted,
                     created_at=created_at, retweet_count=retweet_count, contributors=contributors,
                     favorite_count=favorite_count, in_reply_to_user_id=in_reply_to_user_id,
                     in_reply_to_status_id=in_reply_to_status_id)
# {
#   "truncated": false,
#   "coordinates": null,
#   "entities": {
#     "symbols": [],
#     "user_mentions": [],
#     "hashtags": [],
#     "urls": []
#   },
#   "in_reply_to_screen_name": null,
#   "id_str": "552784600502915072",
#   "geo": null,
#   "in_reply_to_user_id_str": null,
#   "lang": "en",
#   "in_reply_to_status_id_str": null,
#   "place": null
# }

Seed data.
Flush dev database, then run the script below in python shell.
```
from datetime import date
from organizer.models import Tag, Startup, NewsLink
from blog.models import Post

social_news_tag = Tag.objects.create(name='social news', slug='social_news')
social_media_tag = Tag.objects.create(name='social media', slug='social_media')
photo_sharing_tag = Tag.objects.create(name='photo sharing', slug='photo_sharing')
instant_messaging_tag = Tag.objects.create(name='instant messaging', slug='instant_messaging')
multimedia_tag = Tag.objects.create(name='multimedia', slug='multimedia')
voice_chat_tag = Tag.objects.create(name='voice chat', slug='voice_chat')

reddit = Startup.objects.create(name='reddit', slug='reddit', contact='huffman@reddit.com', founded_date=date(2005,6,23), website='https://www.reddit.com/', description='social news aggregation, web content rating, and discussion website.')

snapchat = Startup.objects.create(name='snapchat', slug='snapchat', contact='spiegel@snap.com', founded_date=date(2011,1,1), website='https://www.snapchat.com/', description='an image messaging and multimedia mobile application')

instagram = Startup.objects.create(name='instagram', slug='instagram', contact='krieger@instagram.com', founded_date=date(2010,10,6), website='https://www.instagram.com/', description='a mobile, desktop, and Internet-based photo-sharing application and service that allows users to share pictures and videos either publicly, or privately to pre-approved followers')
instagram.tags.add(social_media_tag, photo_sharing_tag)
social_media_tag.startup_set.add(instagram)
photo_sharing_tag.startup_set.add(instagram)

instagram_newslink = NewsLink.objects.create(title='Instagram becomes an interest network with hashtag following', pub_date=date(2017,12,12), link='https://techcrunch.com/2017/12/12/follow-instagram-hashtags/', startup=instagram)

instagram_post = Post.objects.create(title='Instagram History', slug='instagram-history', text='Instagram began development in San Francisco, when Kevin Systrom and Mike Krieger chose to focus their multi-featured HTML5 check-in project, Burbn, on mobile photography.')
instagram_post.tags.add(social_media_tag, photo_sharing_tag)
social_media_tag.blog_posts.add(instagram_post)
photo_sharing_tag.blog_posts.add(instagram_post)
instagram_post.startups.add(instagram)
instagram.blog_posts.add(instagram_post)
```
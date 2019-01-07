# connect data-base
import mlab
from mongoengine import Document, StringField, IntField

mlab.connect()

# define model (document)
class Movie(Document):
    title = StringField()
    image = StringField()
    link = StringField()
    rate = IntField()


movie_list = Movie.objects(rate__gte=7, title__contains="Iron")    # Lazy Loading
for m in movie_list:
    print(m.title, m.rate)

# create data
# m = Movie(  title="Captain America", 
#             image="https://i.pinimg.com/originals/ec/b8/67/ecb867283a30f334f40d11de551f5f36.jpg",
#             link="https://www.imdb.com/title/tt0458339/",
#             rate=6)

# m.save()
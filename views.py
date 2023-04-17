from main.models import *
import datetime
from django.db.models import Count, Avg, Sum, Max, Min
from django.db.models import Q, F

ans1 = Books.objects.all()

ans2 = Books.objects.all().values_list('title', 'published_date')

ans3 = Authors.objects.all().filter(popularity_score=0).values_list('firstname', 'lastname')

ans4 = Authors.objects.all().filter(firstname__startswith='a', popularity_score__gte=8).values_list('firstname', 'popularity_score')

ans5 = Authors.objects.all().filter(firstname__icontains='aa').values_list('firstname')

ans6 = Authors.objects.all().filter(pk__in=[1, 3, 23, 43, 134, 25])

ans7 = Authors.objects.all().filter(joindate__gte=datetime.date(year=2012, month=9, day=1)).order_by('joindate').values_list('firstname', 'joindate')

ans8 = Publishers.objects.all().order_by('lastname').values_list('lastname').distinct()[:10]

ans9 = [Authors.objects.all().order_by('joindate').last(),
        
Publishers.objects.all().order_by('-joindate').first()]

ans10 = Authors.objects.all().order_by('-joindate').values_list('firstname', 'lastname', 'joindate').first()

ans11 = Authors.objects.all().filter(joindate__year__gte=2013)

ans12 = Books.objects.all().filter(author__popularity_score__gte=7).aggregate(total_book_price=Sum('price'))

ans13 = Books.objects.all().filter(author__firstname__contains='a').values_list('title', flat=True)

ans14 = Books.objects.all().filter(author__pk__in=[1, 3, 4]).aggregate('price')

ans15 = Authors.objects.all().values_list('firstname', 'recommendedby__firstname')

ans16 = Authors.objects.all().filter(books__publisher__pk=1)

user1 = Users.objects.create(username='user1', email='user1@test.com')

user2 = Users.objects.create(username='user2', email='user2@test.com')

user3 = Users.objects.create(username='user3', email='user3@test.com')

ans17 = Authors.objects.get(pk=1).followers.add(user1, user2, user3)

ans18 = Authors.objects.get(pk=2).followers.set(user1)

ans19 = Authors.objects.get(pk=1).followers.add(user1)

ans20 = Authors.objects.get(pk=1).followers.remove(user1)

ans21 = Users.objects.get(pk=1).followed_authors.all().values_list('firstname', flat=True)

ans22 = Authors.objects.all().filter(books__title__icontains='tle')

ans23 = Authors.objects.all().filter(Q(firstname__istartswith='a') and ( Q(popularity_score__gt=5) or Q(joindate__year__gt=2014)))

ans24 = Authors.objects.all().get(pk=1)

ans25 = Authors.objects.all()[:10]

qs = Authors.objects.all().filter(popularity_scre=7)

author1 = qs.first()

author2 = qs.last()

ans26 = [author1, author2]
ans27 = Authors.objects.all().filter(joindate__year__gte=2012, popularity_score__gte=4, joindate__day__gte=12, firstame__istartswith='a')

ans28 = Authors.objects.all().exclude(joindate__year=2012)

oldest_author = Authors.objects.all().aggregate(Min('joindate'))

newest_author = Authors.objects.all().aggregate(Max('joindate'))

avg_pop_score = Authors.objects.all().aggregate(Avg('popularity_score'))

sum_price = Books.objects.all().aggregate(Sum('price'))

ans29 = [oldest_author, newest_author, avg_pop_score, sum_price]

ans30 = Authors.objects.all().filter(recommendedby__isnull=True)

one = Books.objects.all().filter(author__isnull=False)

two = Books.objects.all().filter(author__isnull=False, author__recommender__isnull=True)

ans31 = [one, two]

ans32 = Books.objects.all().filter(author__pk=1).aggregate(Sum('price'))

ans33 = Books.objects.all().order_by('published_date').last().title

ans34 = Books.objects.all().aggregate(Avg('price'))

ans35 = Publishers.objects.filter(books__author__pk=1).aggregate(Max('popularity_score'))

ans36 = Authors.objects.filter(books__title__icontains='ab').count()

ans37 = Authors.objects.annotate(f_count=Count('followers')).filter(f_count__gt=216)

ans38 = Authors.objects.filter(joindate__gt=datetime.date(year=2014, month=9, day=20)).aggregate(Avg('popularity_score'))

ans39 = Books.objects.all().annotate(bk_count=Count('author__books')).filter(bk_count__gt=10).distinct()

ans40 = Books.objects.all().annotate(count_title=Count('title')).filter(count_title__gt=1)

from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from django.shortcuts import render
from article.models import Article, Comments

from django.core.exceptions import ObjectDoesNotExist
from article.forms import CommentForm
from django.template.context_processors import csrf

from django.contrib import auth # отвечает за работу с юзерами


# Create your views here.
def basic_one(request):
    view = "basic_one"
    html = "<html><body>This is %s view</body></html>" % view
    return HttpResponse(html)

def template_two(request):
    view = "template_two"
    html = get_template("myview.html").render({'name': view})
    return HttpResponse(html)

def template_three_simple(request):
    view = "template_three"
    return render_to_response('myview.html', {'name': view})

def index(request):
    return render(request, 'index.html')

def articles(request):
    return render_to_response('articles.html', {'articles' : Article.objects.all(), 'username': auth.get_user(request).username})

# def article(request, article_id=1):
#     return render_to_response('article.html', {'article': Article.objects.get(id = article_id), 'comments': Comments.objects.filter(comments_article_id=article_id)})


def article(request, article_id):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id = article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)

def addlike(request, article_id):
    try:

        if article_id in request.COOKIES:
            redirect('/')
        else:

            article = Article.objects.get(id = article_id)
            article.article_likes +=1
            article.save()

            response = redirect('/')
            response.set_cookie(article_id, "test")
            return response

    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


def addcomment(request, article_id):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id = article_id)
            form.save()

            request.session.set_expiry(60)
            request.session['pause'] = True

    return redirect('/articles/get/%s' % article_id)













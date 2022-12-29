from django.shortcuts import render
from django.contrib.auth import login,authenticate
from django.http import Http404
from articles.models import Article
from django.shortcuts import redirect
from django.contrib.auth.models import User

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
                }
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
            # если поля заполнены без ошибок
                try:
                    Article.objects.get(title=form['title'])
                    form['errors'] = u"Статья с таким названием уже существует"
                    return render(request, 'create_post.html', {'form': form})
                except Article.DoesNotExist:
                    article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                    return redirect('get_article', article_id=article.id)
                # перейти на страницу поста
            else:
            # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})
    else:
        raise Http404

def user_login(request):
    if request.user.is_anonymous:
        if request.method =="POST":
            form = {'login': request.POST["login"], 'pass': request.POST["pass"]}
            if form['login'] and form['pass']:
                user = authenticate(username=form["login"],password=form["pass"])
                if user:
                    login(request, user)
                    return redirect("home")
                else:
                    form['errors'] = u"Неверные данные"
                    return render(request, 'auth.html', {'form': form})
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'auth.html', {'form': form})
        else:
            return render(request, 'auth.html', {})
    else:
        return redirect("home")

def user_reg(request):
    if request.user.is_anonymous:
        if request.method =="POST":
            form = {'login': request.POST["login"], 'email': request.POST["email"], 'pass': request.POST["pass"]}
            if form['login'] and form['pass'] and form['email']:
                try:
                    User.objects.get(username=form['login'])
                    # если пользователь существует, то ошибки не произойдет и программа # удачно доберется до следующей строчки
                    form['errors'] = u"Пользователь с таким именем уже есть"
                    return render(request, "reg.html",{'form':form})
                except User.DoesNotExist:
                    user = User.objects.create_user(form['login'], form['email'],form['pass'],)
                    return redirect("home")
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'auth.html', {'form': form})
        else:
            return render(request, 'reg.html', {})
    else:
        return redirect("home")


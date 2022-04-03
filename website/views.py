from django.shortcuts import render, get_object_or_404
from website.models import Movie, Actor, Director
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your views here.
def home(request):
    movies = Movie.objects.order_by('-year')[:3]
    return render(request, 'home.html', {'movies': movies})


def actor_detail(request, actor_id):
    actor = get_object_or_404(Actor, pk=actor_id)
    return render(request, 'actor_detail.html', {'actor': actor})

def director_detail(request, director_id):
    director = get_object_or_404(Director, pk=director_id)
    return render(request, 'director_detail.html', {'director': director})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})  

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            return render(request, 'registration/signup.html', {'error': 'Passwords do not match'})

        myuser = User.objects.create_user(username, email, pass1)
        myuser.is_active = False
        myuser.save()
        # messages.success(request, "Signed Up Successfully!")
        # template = render_to_string('email_template.html', {'name':username})
        # email = EmailMessage(
        #     'Welcome to IMDB',
        #     template,
        #     settings.EMAIL_HOST_USER,
        #     [email],
        # )
        # email.send(fail_silently=False)
        return redirect('home')
    return render(request, 'registration/signup.html')
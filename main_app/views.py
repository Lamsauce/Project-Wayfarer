from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic.edit import UpdateView

# Create your views here.

def homepage(request):
    error_message = ''
    if request.method == "POST":
        if request.POST.get('submit') == 'sign_up':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('profile')
            else: 
                error_message = "Invalid Sign Up - Please Try Again"
        elif request.POST.get('submit') == 'sign_in':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                error_message = "Invalid Sign In Credentials - Please Try Again"
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'homepage.html', context)


def logout(request):
    logout(request)
    return redirect('homepage')


@login_required(login_url='homepage')
def profile(req):
    # if req.method == 'POST':
    #     comment_form = AddComment_Form(req.POST)
    #     if comment_form .is_valid():
    #         new_comment = comment_form .save(commit=False)
    #         new_comment.user = req.user
    #         new_comment.save()
    #         return redirect('profile')
    # # Selected city
    # selected_city = City.objects.filter(id=city_id)

    # # all citys
    # cities = SelectedCity.objects.all()

    # comment_form = AddComment_Form()
    # context = {'city': selected_city, 'cities': cities}
    return render(req, 'profile.html')

def posts(request):
    return render(request, 'posts.html')

def post(request):
  if request.method == "POST":
    title = request.POST['title']
    content = request.POST['content']
    username_form = request.POST['username']

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('profile')


class EditUserProfileView(UpdateView):
    model = Profile
    form_class = UserProfileForm
    template_name = "profiles/user_profile.html"

def get_object(self, *args, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs['pk'])

        # We can also get user object using self.request.user  but that doesnt work
        # for other models.

        return user.userprofile

def get_success_url(self, *args, **kwargs):
        return reverse("some url name")
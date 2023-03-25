from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project, Comment
from .forms import ProjectForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
#def home(request):
#	return render(request, 'home.html', {})


def LikeView(request, pk):
	Project = get_object_or_404(Project, id=request.Project.get('Project_id'))
	liked = False
	if Project.likes.filter(id=request.user.id).exists():
		Project.likes.remove(request.user)
		liked = False
	else:
		Project.likes.add(request.user)
		liked = True

	return HttpResponseRedirect(reverse('Project-detail', args=[str(pk)]))


class HomeView(ListView):
	model = Project
	template_name = 'home.html'
	# cats = Category.objects.all()
	# ordering = ['-project_date']
	#ordering = ['-id']

	def get_context_data(self, *args, **kwargs):
		# cat_menu = Category.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		# context["cat_menu"] = cat_menu
		return context





class ProjectDetailView(DetailView):
	model = Project
	template_name = 'project_details.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(ProjectDetailView, self).get_context_data(*args, **kwargs)

		stuff = get_object_or_404(Project, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()

		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True

		context["cat_menu"] = cat_menu
		context["total_likes"] = total_likes
		context["liked"] = liked
		return context


class AddProjectView(CreateView):
	model = Project
	form_class = ProjectForm
	template_name = 'add_project.html'
	#fields = '__all__'
	#fields = ('title', 'body')


class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'
	#fields = '__all__'

	def form_valid(self, form):
		form.instance.Project_id = self.kwargs['pk']
		return super().form_valid(form)

	success_url = reverse_lazy('home')


# class AddCategoryView(CreateView):
# 	model = Category
# 	#form_class = ProjectForm
# 	template_name = 'add_category.html'
# 	fields = '__all__'
# 	#fields = ('title', 'body')


class UpdateProjectView(UpdateView):
	model = Project
	form_class = EditForm
	template_name = 'update_project.html'
	#fields = ['title', 'title_tag', 'body']


class DeleteProjectView(DeleteView):
	model = Project
	template_name = 'delete_project.html'
	success_url = reverse_lazy('home')

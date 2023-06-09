from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project, Comment
from .forms import ProjectForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


def about(request):
	return render(request, 'about.html', {})

def review(request):
	return render(request, 'review.html', {})


def LikeView(request, pk):
	project = get_object_or_404(Project, id=request.POST.get('project_id'))
	liked = False
	if project.likes.filter(id=request.user.id).exists():
		project.likes.remove(request.user)
		liked = False
	else:
		project.likes.add(request.user)
		liked = True

	return HttpResponseRedirect(reverse('project-detail', args=[str(pk)]))


class HomeView(ListView):
	model = Project
	template_name = 'home.html'

	def get_context_data(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		return context


class ProjectVIew(ListView):
	model = Project
	template_name = 'project_home.html'
	# ordering = ['-post_date']
	ordering = ['-id']

	def get_context_data(self, *args, **kwargs):
		context = super(ProjectVIew, self).get_context_data(*args, **kwargs)
		return context




class ProjectDetailView(DetailView):
	model = Project
	template_name = 'project_details.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ProjectDetailView, self).get_context_data(*args, **kwargs)

		stuff = get_object_or_404(Project, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()

		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True

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



class UpdateProjectView(UpdateView):
	model = Project
	form_class = EditForm
	template_name = 'update_project.html'


class DeleteProjectView(DeleteView):
	model = Project
	template_name = 'delete_project.html'
	success_url = reverse_lazy('project-view')

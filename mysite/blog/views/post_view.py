from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404, render

from blog.models import Postagem
from blog.forms import CommentForm


#View para alimentar a lista de itens a serem puxados para o template:
class PostView(generic.ListView):
    queryset = Postagem.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

#View para dispor o template do detalhe das postagens:
#class PostDetail(generic.DetailView):
#    model = Postagem
#    template_name = 'post_detail.html'


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Postagem, slug=slug)
    comments = post.comments.filter(active=True).order_by('-created_on')
    new_comment = None

    #Comment posted

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            #Create comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            #Assign the current post to the comment
            new_comment.post = post
            #Save the comment to the database
            new_comment.save()

    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form,
        }
    )
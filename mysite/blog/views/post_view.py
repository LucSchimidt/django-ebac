from django.http import HttpResponse
from django.views import generic
from blog.models.post import Postagem


#View para alimentar a lista de itens a serem puxados para o template:
class PostView(generic.ListView):
    queryset = Postagem.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

#View para dispor o template do detalhe das postagens:
class PostDetail(generic.DetailView):
    model = Postagem
    template_name = 'post_detail.html'
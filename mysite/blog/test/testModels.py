from django.test import TestCase
from blog.models import Topics, Postagem


class TestModels(TestCase):

    def setUp(self):
        self.postagem = Postagem.objects.create(
            title = 'Microsoft lança um console no meio da geração!',
            slug = 'news-1',
            content = 'A Microsoft surpreende o mundo da tecnologia com o lançamento surpresa de um novo console no auge da geração, deixando os fãs ansiosos por mais detalhes.',
            status = 1
        )

        self.topico = Topics.objects.create(
            title = 'Notícias de jogos',
            type = 0
        )

    #== TESTES DO MODELO POSTAGEM: ==
    
    #Testa se o nome da postagem criada está correto:
    def test_postagem_title_value(self):
        self.assertEquals(self.postagem.title, 'Microsoft lança um console no meio da geração!')

    #Testa se o slug da postagem criada está correto:
    def test_postagem_slug_value(self):
        self.assertAlmostEquals(self.postagem.slug, 'news-1')


    #== TESTES DO MODELO TOPICS: ==

    def test_topics_title_value(self):
        self.assertEquals(self.topico.title, 'Notícias de jogos')

    def test_topics_type_value(self):
        self.assertAlmostEquals(self.topico.type, 0)

    
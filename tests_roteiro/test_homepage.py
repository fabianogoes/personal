from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class HomePageTest(TestCase):
    def setUp(self):
        url = reverse('home')
        self.resp = self.client.get(url)

    def test_get_deve_retornar_codigo_200(self):
        'GET deve retornar codigo 200'
        self.assertEqual(200, self.resp.status_code)

    def test_deve_usar_o_template_index(self):
        'Homepage deve user o template index.html'
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_conteudo_html(self):
    	'html index deve ter dados experados: Titulo, links, etc...'
    	self.assertContains(self.resp, 'Titulo da Pagina')

    	url_cadastro = reverse('core:cadastro', args=[0])
    	self.assertContains(self.resp, url_cadastro)

    def test_context_in_template(self):
    	'template deve conter objetos no context'
    	self.assertIn('usuario_logado', self.resp.context)
    	self.assertIn('texto_boas_vindas', self.resp.context)

    def test_objeto_user_deve_ser_uma_instancia_de_User(self):
    	'no contexto deve ter uma instancia de User'
    	user = self.resp.context['usuario_logado']
    	self.assertIsInstance(user, User)


from django.test import TestCase
from django.core.urlresolvers import reverse


class PessoaViewFormTest(TestCase):
    def setUp(self):
        url = reverse('core:cadastro', args=[0])
        self.resp = self.client.get(url)


    def test_get_deve_retornar_codigo_200(self):
        'GET deve retornar codigo 200'
        self.assertEqual(200, self.resp.status_code)

    def test_deve_usar_o_template_index(self):
        'cadastro deve user o template cadastro.html'
        self.assertTemplateUsed(self.resp, 'cadastro.html')
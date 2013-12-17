# coding: utf-8
from django.test import TestCase
from core.models import Pessoa

class PessoaModelTest(TestCase):
	def setUp(self):
		self.pessoa = Pessoa.objects.create(
				nome=u'Fabiano',
				cpf='1234567890',
				email='fabianogoes@gmail.com'
			)


	def test_get_model_id_um(self):
		'deve retornar um objeto pessoa com o id 1'
		p = Pessoa.objects.get(id=1)
		self.assertEqual(unicode(p), u'Fabiano')


	def test_create_new_model(self):
		'deve criar um novo registro de pessoa'
		p = Pessoa.objects.create(
				nome=u'Fulano',
				cpf='1234567890',
				email='fulano@gmail.com'
			)
		self.assertIsInstance(p, Pessoa)


	def test_cpf(self):
		'cpf do objeto pessoa criado deve ser igual a 1234567890'
		self.assertEqual(unicode(self.pessoa.cpf), '1234567890')


	def test_email(self):
		'email do objeto pessoa criado deve ser igual a fabianogoes@gmail.com'
		self.assertEqual(unicode(self.pessoa.email), 'fabianogoes@gmail.com')


	def test_filter_por_nome_deve_retornar_um_registro(self):
		'o filtro por nome deve retornar um registro'
		count = Pessoa.objects.filter(nome='Fabiano').count()
		self.assertEqual(count, 1)
    
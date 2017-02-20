from django.db import models

#Criando objeto para realizar buscas no sistema
class CourseManager(models.Manager):

		def search(self, query):
			return self.get_queryset().filter(
			models.Q(name__icontains=query) | 
			models.Q(descríption__icontains=query))

class Course(models.Model):

	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Atalho')
	descríption = models.TextField('Descrição', blank=True)
	start_date = models.DateField('Data de Início', null=True, blank=True)
	image = models.ImageField (upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	update_at = models.DateTimeField('Atualizado em', auto_now=True)

#Definindo que o manager padrão do projeto agora é o CourserManager

	objects = CourseManager()
		
	def __str__(self):
		return self.name

	class Meta:
		# Substituindo o nome dos titulos no admin
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'
		# Exibindo os resultdos em ordem alfabética pelo nome
		ordering = ['name']
import random
import string


from django.test import TestCase
from app_blog.models import Post

class posttestcase(TestCase):
    pass
# test post: este test esta diseñado para comprobar la creacion de los posteos en el blog.
    def test_creacion_post(self):
        lista_letras_title = [random.choice(string.ascii_letters + string.digits) for _ in range(15)]
        lista_letras_subtitle = [random.choice(string.ascii_letters + string.digits) for _ in range(25)]
        lista_letras_body = [random.choice(string.ascii_letters + string.digits) for _ in range (100) ]
        body_prueba = "".join(lista_letras_body)
        title_prueba = "".join(lista_letras_title)
        subtitle_prueba ="".join(lista_letras_subtitle)
        post_1 = Post.objects.create(title=title_prueba, subtitle=subtitle_prueba, body=body_prueba)

        self.assertIsnotnone(post_1.id)
        self.assertEqual(post_1.title, title_prueba)
        self.assertEqual(post_1.subtitle, subtitle_prueba)
        self.assertEqual(post_1.body, body_prueba)
#con estos assert se espera el retorno de comprobacion con id si el post se guardo correctamente. 
#Con title si el titulo es creo correctamente
#con subtitle si el subtitulo se creo correctamente.
#con body si el cuerpo de texto se creo correctamente.


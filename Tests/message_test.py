import random
import string
import pytest

from django.test import TestCase
from app_messages.models import Message


class messagetestcase(TestCase):
    pass
# test de message: este test corrobora si las creacion y envio de mensajes es correcta.
    def test_creacion_message(self):
        lista_letras_title = [random.choice(string.ascii_letters + string.digits) for _ in range(10)]
        lista_letras_content = [random.choice(string.ascii_letters + string.digits) for _ in range(100)]
        title_prueba = "".join(lista_letras_title)
        content_prueba ="".join(lista_letras_content)
        message_1 = message.objects.create(title=title_prueba, content=content_prueba,)

        self.assertIsnotnone(message_1.id)
        self.assertEqual(message_1.title, title_prueba)
        self.assertEqual(message_1.content, content_prueba)
        #con assertisnotnone se busca saber si los mensajes se guardaron correctamente.
        #con assertequal se espera confirmar la creacion del mensaje y su envio.

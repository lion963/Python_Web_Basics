from django.test import TestCase, Client, RequestFactory


class LostAndFoundViewTest(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_getIndex_should_render_template(self):
        response = self.test_client.get('')
        self.assertTemplateUsed(response, 'index.html')
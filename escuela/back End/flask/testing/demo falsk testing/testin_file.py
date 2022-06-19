from app import app
from unittest import TestCase


class ColorView(TestCase):
    def test_color_form(self):
        with app.test_client() as client:
            #making a request to '/'
            res = client.get('/')
            #  this gives us whatever fata is beaing reveived in this case html data
            html = res.get_data(as_text=True)

            # making sure our get request(res) is 200 code (ok)
            self.assertEqual(res.status_code, 200)
            # is this inside our html variable ,
            self.assertIn('<h1>Color Form</h1>', html)
            #POST request

    def test_color_form(self):
        with app.test_client() as client:
            # sending a post request to /fav-color
            res = client.post('/fav-color', data={'color': 'blue'})

            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)

            self.assertIn('<h3>Woah! I like blue, too</h3>', html)

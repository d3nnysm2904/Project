from app import app  #this is importinmg thr app file to make test 
from unittest import TestCase


# to run this file in terminal needs to be python -m unittest testin_file.py


# client can be any name is just acting like a user , a client 
class ColorView(TestCase):
    def test_color_form(self):
        with app.test_client() as client:
            #making a request to '/'
            res = client.get('/')
            #  this gives us whatever data is beaing received ;in this case html data  (as_text=True) 
            html = res.get_data(as_text=True)

            # making sure our get request(res) is 200 code (ok)
            self.assertEqual(res.status_code, 200)
            # is this inside our html variable ,
            self.assertIn('<h1>Color Form</h1>', html)
            #POST request

    def test_color_form(self):
        with app.test_client() as client:
            # sending a post request to /fav-color and the data send should be blue, but also we can pass a query string
            res = client.post('/fav-color', data={'color': 'blue'})

            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)

            self.assertIn('<h3>Woah! I like blue, too</h3>', html)
            
            #test redirect 
    def test_redirect(self):
        with app.test_client()as client:
            res = client.get('redirect-me')     
            
            self.assertEqual(res.status_code,302) # is the status code 302? 
            self.assertEqual(res.location, 'http://127.0.0.1:5000')        
 
    def test_redirection_followed(self):
        with app.test_client()as client:
            res=client.get('/redirect-me',follow_redirects=True)
            
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code,302)
            self.assertIn('<h1>Color Form</h1>', html)


 
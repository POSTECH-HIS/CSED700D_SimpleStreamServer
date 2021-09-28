# CSED700D Simple HTTP Stream Server
- Tested with Python 3.9.6 and Flask 2.0.1
- Server listens to 5000 port by default

## Usage

Install dependencies:

```bash
pip install -r requirements.txt
```

Running the server:
```bash
$ python app.py
```

Open your browser, and visit <http://localhost:5000/>

As soon as your Android app makes a POST request to the server with an activity label, your browser will display it. 

To conveniently make HTTP GET or POST requests from Android, you might find [Volley](https://developer.android.com/training/volley) useful. 
[This page](https://nabeelj.medium.com/making-a-simple-get-and-post-request-using-volley-beginners-guide-ee608f10c0a9) provides sample codes making GET and POST 
requests using Volley. 

To test the server by manually making a POST request, you may download the enclosed post.html and open it using your browser on the machine where the server runs. (Modify the POST URL in the HTML input form if testing from a different machine.)

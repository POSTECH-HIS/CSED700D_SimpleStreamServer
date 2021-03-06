# CSED700D Simple HTTP Stream Server

## Tested with:
- Python 3.9.6
- Flask 2.0.1
- Chrome 94.0.4606.61 (which is the current stable release in Windows, Mac, and Linux, as of September 24, 2021. 

## Usage

Install dependencies:

```bash
pip install -r requirements.txt
```

Running the server:
```bash
$ python app.py
```

Open your browser, and visit <http://localhost:5000/> (Server listens to 5000 port by default.)

As soon as your Android app makes a fresh classification, have your app send a POST request to the server with the new activity label. Your browser will keep updating the new activity labels. 

To conveniently make HTTP GET or POST requests from Android, you might find [Volley](https://developer.android.com/training/volley) useful. 
[This page](https://nabeelj.medium.com/making-a-simple-get-and-post-request-using-volley-beginners-guide-ee608f10c0a9) provides sample codes making GET and POST 
requests using Volley. 

To test the server by manually making a POST request, you may download the enclosed post.html and open it using your browser on the machine where the server runs. (Modify the POST URL in the HTML input form if testing from a different machine.)

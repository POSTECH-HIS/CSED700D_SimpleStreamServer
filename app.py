from flask import Flask, render_template, request, Response
import time, json, queue
app = Flask(__name__)  

q = queue.SimpleQueue()
q.put('No activity')

def pop_activity():
    global q
    activity = q.get()
    return activity

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/post_activity', methods=['POST'])
def post_activity():
    #global activity
    global q
    activity = request.form['activity']
    q.put(activity)
    return json.dumps({'result':True})

@app.route('/stream')
def stream():
    def eventStream():
        while True:
            # wait for activity to be available, then push it
            yield 'data: {}\n\n'.format(pop_activity())
    return Response(eventStream(), mimetype="text/event-stream")

if __name__ == "__main__":  
    app.run(debug=True, host='0.0.0.0', port=5000)  



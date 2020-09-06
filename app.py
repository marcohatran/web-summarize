from flask import Flask, request,render_template,jsonify,url_for,Response,jsonify,make_response, redirect
from utils.utils import get_data_from_url
from utils.summarizer import summarizer
app = Flask(__name__)
@app.route('/summarizer', methods =['POST'])
def original_text_form():
    url = request.form['input_text']
    text = get_data_from_url(url)
    number_of_sent = request.form['num_sentences']
    summary = summarizer(text,int(number_of_sent))
    

    return render_template('index1.html', title = "Summarizer", original_text = text, output_summary = summary)

@app.route('/')
def homepage():
    title = "TEXT summarizer"
    return render_template('index1.html', title = title)
@app.route("/summarize",methods =  ['GET'])
def post_url():
    if 'url' not in request.args:
        return make_response(jsonify({'error': str('Bad Request: argument `url` is not available')}), 400)

    url = request.args['url']

    if not url:  # if url is empty
        return make_response(jsonify({'error': str('Bad Request: `url` is empty')}), 400)

    try:
        article = get_data_from_url(url)
        summary = summarizer(article,2)
    except Exception as e:
        print("Error: "+str(e))
        pass
    return make_response(jsonify({'summary': summary}))
        




if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
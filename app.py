from Flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    query = request.form['query']
    results = google_dork_search(query)
    return render_template('results.html', query=query, results=results)
  return render_template('index.html')

def google_dork_search(query):
  url = f'https://www.google.com/search?q={query}'
  headers = {'User-Agent': 'Mozilla/5.0'}
  response = requests.get(url, headers=headers)
  return response.text

if __name__ == '__main__':
  app.run(debug=True)

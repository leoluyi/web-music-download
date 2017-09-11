from flask import Flask, render_template, request
from modules import item

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('base.html')


@app.route("/result")
def result_page():
    search = request.args.get('search')
    soup = item.search_soup(search)
    res = item.find_video_(soup)
    return render_template('result.html', result=search, all_item=res)


if __name__ == '__main__':
    app.run(debug=True)

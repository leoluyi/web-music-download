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
    pages = item.page_bar(soup)
    return render_template('result.html', result=search, all_item=res, all_page=pages)

@app.route("/download")
def download_page():
    value = request.args.get('value')
    dl_type, url = value.split('&')
    if dl_type == 'mp3':
        item.download_mp3(url)
    elif dl_type == 'mp4':
        item.download_mp4(url)

    return render_template('download.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import re

app = Flask(__name__)

def brute_force_search(text, pattern):
    positions = []
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            positions.append(i)
    return positions

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    highlighted_text = ""
    count = 0

    if request.method == 'POST':
        file = request.files['file']
        keyword = request.form['keyword']

        text = file.read().decode('utf-8')
        positions = brute_force_search(text.lower(), keyword.lower())
        count = len(positions)

        highlighted_text = text
        for pos in reversed(positions):
            highlighted_text = (
                highlighted_text[:pos] +
                "<mark>" + highlighted_text[pos:pos+len(keyword)] + "</mark>" +
                highlighted_text[pos+len(keyword):]
            )

        result = True

    return render_template(
        'index.html',
        result=result,
        highlighted_text=highlighted_text,
        count=count
    )

if __name__ == '__main__':
    app.run(debug=True)

from flask import *
from Conversion import *
import uuid

app = Flask(__name__)


@app.route('/videoFormats')
def videoFormats():
    ll = {'result': []}
    req = request.form
    if req.get('url'):
        url = req.get('url')
        res = extractVideoFormats(url)
        for format in res['formats']:
            ll['result'].append({
                'format': '{}x{}'.format(format['height'], format['width']),
                'url': format['url']
            })
        return ll
    return jsonify({'msg': 'massing input'})


@app.route('/downloadFeet')
def downloadFeet():
    req = request.form
    if req.get('url'):
        input = req.get('url')
        output = './videos/{}.mp4'.format(uuid.uuid4())
        st = convertHLStoMP4(input, output)
        return send_file(st)
    return jsonify({'msg': 'massing input'})


if __name__ == '__main__':
    app.run()

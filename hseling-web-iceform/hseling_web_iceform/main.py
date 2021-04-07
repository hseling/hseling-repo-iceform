# -*- coding: utf-8 -*-
"""
USER
/ - index
/search - formula search
/formula/<int:formula_id> - single formula page
"""
import os
import requests
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
API_URL = os.environ.get('HSELING_API_ENDPOINT')
print("------------------------------------------")
print(API_URL)
print("------------------------------------------")

# @app.context_processor
# def add_prefix():
#     return dict(api_url=API_URL)


@app.route('/web/healthz')
def healthz():
    app.logger.info('Health checked')
    return jsonify({"status": "ok", "message": "hseling-web-iceform"})


@app.route('/web/')
def index():
    """Index page"""
    return render_template("index.html")


@app.route('/web/search')
def search_page():
    """Search page"""
    return render_template("search.html")


@app.route("/web/formula/<int:formula_id>")
def formula_view(formula_id):
    """Page for single formula"""
    print(API_URL + f"contexts/{formula_id}")
    data = requests.get(API_URL + f"contexts/{formula_id}").json()
    return render_template("formula.html", data=data)


# @app.route("/web/final")
# def final_list():
#     """Page for final list"""
#     return render_template("final_list.html")


# api = Api(app)
# api.add_resource(FormulaSearch, '/api/formula_search')
# api.add_resource(FinalList, '/api/final')
# api.add_resource(FormulaContexts, '/api/contexts/<formula_id>')
@app.route("/web/api/<path:path>")
def api_redirect(path):

    print(path)
    print(API_URL + path)
    print(request.query_string.decode())
    if request.query_string.decode():
        data = requests.get(API_URL + path + "?" + request.query_string.decode()).json()
    else:
        data = requests.get(API_URL + path).json()
    return jsonify(data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8000)


__all__ = [app]

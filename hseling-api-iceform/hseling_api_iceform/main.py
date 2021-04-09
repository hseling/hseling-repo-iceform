# -*- coding: utf-8 -*-
"""
API
/api_part/formula_search - search API
/api_part/contexts/<formula_id> - contexts for one formula (with span)
"""
from flask import Flask, jsonify
from flask_restful import Api
from hseling_api_iceform.models import db
from .api import FormulaSearch, FormulaContexts, FinalList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////data/ice_site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
db.app = app
db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(FormulaSearch, '/api/formula_search')
api.add_resource(FinalList, '/api/final')
api.add_resource(FormulaContexts, '/api/contexts/<formula_id>')


@app.route('/api/healthz')
def healthz():
    app.logger.info('Health checked')
    return jsonify({"status": "ok", "message": "hseling-api-iceform"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)


__all__ = [app]

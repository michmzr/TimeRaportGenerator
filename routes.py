import logging

from flask import Blueprint, request, jsonify, send_file

from raport import fill_template
from schema import RaportSchema
from marshmallow import ValidationError

bp_raport = Blueprint('raport', __name__)

@bp_raport.route('/raport', methods=['POST'])
def project():
    schema = RaportSchema()
    try:
        data = schema.load(request.json)

        raport = fill_template(data['output_file_path'],
        data['year'], data['month'], data['out_days'],
        data['project_name'],
        data['contractor_name'],
        data['nip'],
        data['position'],
        data['client_name'])
        print(raport)
        logging.debug(f'Raport\n{jsonify(raport)}')

        return send_file(raport["raport_file_path"], as_attachment=True)
    except ValidationError as e:
        return jsonify(e.messages), 400
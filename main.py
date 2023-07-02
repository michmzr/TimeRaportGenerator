from flask import Flask, jsonify
from routes import bp_raport

import logging
logging.basicConfig(level=logging.DEBUG)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_raport)
    register_error_handlers(app)
    return app


def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found_error(e):
        return jsonify({"message": "Resource not found"}), 404

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({"message": "Internal server error"}), 500


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify
from flask_restful import Api,Resource, fields, marshal_with, reqparse
from flask_sqlalchemy import SQLAlchemy
from utils import get_info

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/info.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class WikiInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(50), nullable=False)
    details = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'Topic is {self.topic}'

info_fields = {
    'id': fields.Integer,
    'topic': fields.String,
    'details': fields.String
}

class Information(Resource):

    @marshal_with(info_fields)
    def get(self):
        info = WikiInfo.query.all()
        return info

    def post(self):
        info_args = reqparse.RequestParser()
        info_args.add_argument("topic_name", type=str, help="You must provide topic name", required=True)
        args = info_args.parse_args()
        topic = WikiInfo.query.filter_by(topic=args['topic_name']).first()
        if topic:
            return jsonify({
                "message": "topic already exists",
                "topic": args['topic_name'],
                "details": topic.details
            })
        else:
            new_topic = get_info(args['topic_name'])
            if new_topic['message'] != 'error':
                add_topic = WikiInfo(topic=args['topic_name'], details=new_topic['details'])
                db.session.add(add_topic)
                db.session.commit()
                return jsonify({
                    "message": 'success',
                    "topic": args['topic_name'],
                    "details": new_topic['details']
                })
            else:
                print(args)
                return jsonify({
                    "message": 'fail',
                    "details": 'no details found'
                })


api.add_resource(Information, "/info")

if __name__ == "__main__":
    app.run(debug=True)
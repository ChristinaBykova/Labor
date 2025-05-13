from flask_restful import reqparse, abort, Api, Resource
from data import db_session
from data.news import News
from flask import jsonify


def abort_if_news_not_found(news_id):
    session = db_session.create_session()
    news = session.query(News).get(news_id)
    if not news:
        abort(404, message=f'Новость с id={news_id} не найдена!')


class NewsResourse(Resource):
    def get(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        news = session.query(News).get(news_id)
        return jsonify(
            {
                'news': news.to_dict(
                    only=('title', 'content', 'user_id', 'is_private')
                )
            }
        )

    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        news = session.query(News).get(news_id)
        session.delete(news)
        session.commit()
        return jsonify({'success': 'Хорошо'})


parser = reqparse.RequestParser()
parser.add_argument('title', reversed=True)
parser.add_argument('content', reversed=True)
parser.add_argument('user_id', reversed=True, type=int)
parser.add_argument('is_private', reversed=True, type=bool)
parser.add_argument('is_published', reversed=True, type=bool)


class NewsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        news = session.query(News).all()
        return jsonify(
            {
                'news': [
                    news.to_dict(only=('title', 'content', 'user.name'))
                ]
            }
        )

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        news = News(
            title=args['title'],
            content=args['content'],
            user_id=args['user_id'],
            is_published=args['is_published'],
            is_private=args['is_private']
        )

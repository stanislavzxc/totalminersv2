from flask import Blueprint, jsonify, request

from admin.db import database
from admin.db.database import basic_get_all_asc, basic_create, basic_get, basic_delete, basic_update
from admin.db.models import News
from admin.utils import admin_only, auth_required

news_router = Blueprint(name='news_router', import_name='news_router')

@news_router.get('/news')
@auth_required
def get_all_news():
    """Получение всех новостей."""
    news_items = basic_get_all_asc(News)
    return jsonify([{
        'id': news.id,
        'user_id': news.user_id,
        'title': news.title,
        'description': news.description,
        'url': news.url,
        'image': news.image,
        'created': news.created.isoformat()
    } for news in news_items])

@news_router.post('/news/new')
@auth_required
@admin_only
def create_new_news():
    """Создание новой новости."""
    data = request.get_json()
    user_id = data.get('user_id')
    title = data.get('title')
    description = data.get('description')
    url = data.get('url')
    image = data.get('image')  # Base64 string
    if not title or not description or not url:
        return jsonify({"error": "Недостаточно данных"}), 400
    news = basic_create(News, user_id=user_id, title=title, description=description, url=url, image=image)
    return jsonify({"message": "Новость успешно создана", "news_id": news.id}), 201

@news_router.put('/news/<int:id>/update')
@auth_required
@admin_only
def update_news(id):
    """Обновление новости по ID."""
    data = request.get_json()
    news = basic_get(News, id=id)
    if not news:
        return jsonify({"error": "Новость не найдена"}), 404
    
    # Update the news item with the provided data
    updated_news = basic_update(news, **data)
    
    return jsonify({
        "message": "Новость успешно обновлена",
        "news_id": updated_news.id,
        "news": {
            'id': updated_news.id,
            'user_id': updated_news.user_id,
            'title': updated_news.title,
            'description': updated_news.description,
            'url': updated_news.url,
            'image': updated_news.image,
            'created': updated_news.created.isoformat()
        }
    }), 200

@news_router.post('/news/<int:id>/delete')
@auth_required
@admin_only
def delete_news(id):
    """Удаление новости по ID."""
    news = basic_get(News, id=id)
    if not news:
        return jsonify({"error": "Новость не найдена"}), 404
    basic_delete(News, id)
    return jsonify({"message": "Новость успешно удалена"}), 200
from flask import Blueprint, jsonify, request

from admin.db import database
from admin.db.database import basic_get_all_asc, basic_create, basic_get, basic_delete, basic_update
from admin.db.models import MailTemplate
from admin.utils import admin_only, auth_required

mail_templates_router = Blueprint(name='mail_templates_router', import_name='mail_templates_router')

@mail_templates_router.get('/mail_templates')
#@auth_required
def get_all_mail_templates():
    """Получение всех шаблонов писем."""
    templates = basic_get_all_asc(MailTemplate)
    return jsonify([{
        'id': template.id,
        'title': template.title,
        'content': template.content,
    } for template in templates])

@mail_templates_router.post('/mail_templates/new')
@auth_required
@admin_only
def create_new_mail_template():
    """Создание нового шаблона письма."""
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    if not title or not content:
        return jsonify({"error": "Недостаточно данных"}), 400
    mail_template = basic_create(MailTemplate, title=title, content=content)
    return jsonify({"message": "Шаблон письма успешно создан", "mail_template_id": mail_template.id}), 201

@mail_templates_router.put('/mail_templates/<int:id>/update')
@auth_required
@admin_only
def update_mail_template(id):
    """Обновление шаблона письма по ID."""
    data = request.get_json()
    mail_template = basic_get(MailTemplate, id=id)
    if not mail_template:
        return jsonify({"error": "Шаблон письма не найден"}), 404
    
    updated_template = basic_update(mail_template, **data)
    
    return jsonify({
        "message": "Шаблон письма успешно обновлён",
        "id": updated_template.id,
        "mail_template": {
            'id': updated_template.id,
            'title': updated_template.title,
            'content': updated_template.content,
        }
    }), 200

@mail_templates_router.post('/mail_templates/<int:id>/delete')
@auth_required
@admin_only
def delete_mail_template(id):
    """Удаление шаблона письма по ID."""
    mail_template = basic_get(MailTemplate, id=id)
    if not mail_template:
        return jsonify({"error": "Шаблон письма не найден"}), 404
    basic_delete(MailTemplate, id)
    return jsonify({"message": "Шаблон письма успешно удалён"}), 200
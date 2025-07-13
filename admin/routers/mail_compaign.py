from flask import Blueprint, jsonify, request

from admin.db import database
from admin.db.database import basic_get_all_asc, basic_create, basic_get, basic_delete, basic_update
from admin.db.models import MailCampaign, MailTemplate, User
from admin.utils import admin_only, auth_required, send_email

mail_campaign_router = Blueprint(name='mail_campaign_router', import_name='mail_campaign_router')

@mail_campaign_router.post('/campaign/send')
@auth_required
@admin_only
def send_mail_campaign():
    """
    Отправляет рассылку по указанным пользователям.
    Принимает:
        - template_id: int
        - user_ids: str (через запятую, например "1,2,3")
    """
    data = request.get_json()
    template_id = int(data.get('template_id'))
    user_ids_str = data.get('user_ids')

    if not template_id or not user_ids_str:
        return jsonify({"error": "Недостаточно данных"}), 400

    try:
        user_ids = [int(uid.strip()) for uid in user_ids_str.split(',')]
    except ValueError:
        return jsonify({"error": "Некорректные ID пользователей"}), 400

    users = []
    for user_id in user_ids:
        user = basic_get(User, id=int(user_id))
        if not user:
            continue
        users.append(user)

    mail_template = basic_get(MailTemplate, id=template_id)

    if not mail_template:
        return jsonify({"error": "Шаблон письма не найден"}), 404

    if not users:
        return jsonify({"error": "Пользователи не найдены"}), 404

    created_campaigns = []

    for user in users:
        try:
            send_email(user.email, mail_template.title, mail_template.content)
            campaign = basic_create(
                MailCampaign,
                user_id=user.id,
                template_id=template_id,
                status=True
            )
            created_campaigns.append(campaign)
        except Exception as e:
            print(f"Failed to send mail to {user.email}: {e}")
            campaign = basic_create(
                MailCampaign,
                user_id=user.id,
                template_id=template_id,
                status=False
            )
            created_campaigns.append(campaign)

    return jsonify({
        "message": f"Рассылка успешно отправлена {len(created_campaigns)} пользователям"
    }), 201

@mail_campaign_router.get('/campaign/recipients/<int:template_id>')
@auth_required
@admin_only
def get_recipients_by_template(template_id):
    """
    Возвращает список пользователей, которым была отправлена рассылка с указанным template_id.
    Для каждого пользователя:
        - id
        - email
        - дата последней рассылки по этому шаблону
        - ID шаблона (template_id)
        - статус последней рассылки
    """

    # Получаем все кампании с данным template_id
    campaigns = basic_get_all_asc(MailCampaign, template_id=template_id)

    if not campaigns:
        return jsonify({"message": "Рассылка с таким шаблоном никому не отправлялась"}), 404

    # Группируем кампании по user_id, берём последнюю для каждого пользователя
    from collections import defaultdict
    user_campaigns = defaultdict(list)

    for campaign in campaigns:
        user_campaigns[campaign.user_id].append(campaign)

    result = []

    for user_id, campaign_list in user_campaigns.items():
        latest_campaign = max(campaign_list, key=lambda c: c.sent_at)
        user = basic_get(User, id=user_id)
        if not user:
            continue  # На случай, если пользователь удален, но остались записи в рассылках

        result.append({
            'id': user.id,
            'email': user.email,
            'last_sent': latest_campaign.sent_at.isoformat(),
            'template_id': latest_campaign.template_id,
            'status': latest_campaign.status
        })

    return jsonify(result), 200
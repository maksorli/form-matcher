# scripts/init_db.py

import asyncio

from app.db.database import init_db
from app.models.form_template import FormTemplate


async def seed():
    await init_db()
    # await FormTemplate.find({}).delete_many() #очистка коллекции

    templates = [
        FormTemplate(
            name="Order Form",
            fields={"user_name": "text", "user_email": "email", "order_date": "date"},
        ),
        FormTemplate(
            name="Lead Form", fields={"lead_email": "email", "lead_phone": "phone"}
        ),
        FormTemplate(name="Basic Form", fields={"contact_info": "text"}),
    ]

    await FormTemplate.insert_many(templates)
    print("Templates inserted")


if __name__ == "__main__":
    asyncio.run(seed())

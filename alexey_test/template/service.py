from fastapi import FastAPI


class TemplateService:
    def __init__(self, app_config, mongo):
        self.app_config = app_config
        self.mongo = mongo

    async def get_form(self, find_form_data: dict):
        form = await self.mongo.forms_collection.find_one(find_form_data)
        return form or find_form_data


app = FastAPI()
app.template_service = TemplateService()

from pydantic import BaseModel


class NameValueModel(BaseModel):
    name: str
    value: str

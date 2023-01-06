import pydantic


class SendMessageSchema(pydantic.BaseModel):
    message: str = pydantic.fields.Field(description="Telegram message", example="Hello, world")

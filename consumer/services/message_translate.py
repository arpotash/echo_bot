import abc
import requests
import fastapi

from consumer.settings import settings


class Platform:

    @abc.abstractmethod
    async def send(self, message: str):
        pass


class Telegram(Platform):

    def send(self, message: bytes):
        try:
            response = requests.post(
                settings.telegram_url, json={"chat_id": settings.telegram_char_id, "text": message.decode("utf-8")}
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise fastapi.HTTPException(status_code=fastapi.status.HTTP_400_BAD_REQUEST, detail={"error": e})
        except requests.exceptions.InvalidURL as e:
            raise fastapi.HTTPException(status_code=fastapi.status.HTTP_404_NOT_FOUND, detail={"error": e})

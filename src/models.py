from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from enum import Enum


class BaseModel(DeclarativeBase):
    ...


class PreparedMessages(BaseModel):
    __tablename__ = 'prepared_messages'

    message_id: Mapped[str] = mapped_column(primary_key=True, index=True)
    message_text: Mapped[str]


class User(BaseModel):
    __tablename__ = 'users'

    chat_id: Mapped[int] = mapped_column(primary_key=True)


class SettingType(Enum):
    weather = 'weather'
    news = 'news'
    jokes = 'jokes'


class UserSetting(BaseModel):
    __tablename__ = 'user_settings'

    setting_id: Mapped[int] = mapped_column(primary_key=True,
                                            autoincrement=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("users.chat_id"))
    setting_type: Mapped[SettingType]
    setting_allowed: Mapped[bool]

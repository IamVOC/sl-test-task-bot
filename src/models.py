from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


class BaseModel(DeclarativeBase):
    ...


class PreparedMessages(BaseModel):
    __tablename__ = 'prepared_messages'

    message_id: Mapped[str] = mapped_column(primary_key=True, index=True)
    message_text: Mapped[str]

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY, ENUM
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import relationship

from .database import Base


class Category(Base):
    __tablename__ = 'categories'

    name = Column(String, primary_key=True, index=True)
    message_sent = Column(MutableList.as_mutable(ARRAY(String)), default=[])

    def __repr__(self):
        return f"<Category(name='{self.name}', message_sent={self.message_sent})>"


class User(Base):
    __tablename__ = 'users'

    username = Column(String, primary_key=True, index=True)
    categories = Column(MutableList.as_mutable(ARRAY(String)), ForeignKey('categories.name'), nullable=False)
    received_messages = Column(MutableList.as_mutable(ARRAY(Integer)), ForeignKey('mensajes.id'), nullable=False)

    rel_category = relationship("Category", backref="users", primaryjoin="User.categories.contains(Category.name)")
    rel_message = relationship("Message", backref="users", primaryjoin="User.messages.contains(Message.id)")

    def __repr__(self):
        return f"<User(username='{self.username}', categories={self.categories}, messages={self.messages})>"


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, ForeignKey('categories.name'), nullable=False)
    message = Column(String, nullable=False)

    rel_category = relationship("Category", back_populates="messages")

    def __repr__(self):
        return f"<Message(category='{self.category}', message='{self.message}')>"

import sqlalchemy


from sqlalchemy import create_engine
engine=create_engine("postgresql://user:user@localhost:5432/postgres")

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String




class User(Base):
    __tablename__ = "user"  # テーブル名を指定
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    age = Column(Integer)

    def full_name(self):  # フルネームを返すメソッド
        return "{self.first_name} {self.last_name}"
        
    def as_dict(self):
        print(self.__table__.columns)
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}



Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
SessionClass = sessionmaker(engine)  # セッションを作るクラスを作成
session = SessionClass()

user_a = User(first_name="first_a", last_name="last_a", age=20)
session.add(user_a)
session.commit()

users = session.query(User).all()  

#print([i.__dict__ for i in users])

print(users[0].as_dict())

a = list(map(lambda x:x.as_dict(),users))

print(type(a[0]))
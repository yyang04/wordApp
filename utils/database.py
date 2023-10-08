from typing import Optional, Type, Sequence
from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy import select, func
import logging
from typing import List

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.ERROR)


class Base(DeclarativeBase):
    pass


class Word(Base):
    __tablename__ = 'word'
    id: Mapped[int] = mapped_column(primary_key=True)
    word: Mapped[str] = mapped_column(String(100), nullable=False, index=True)

    definitions: Mapped[List['Definition']] = relationship(back_populates='word')  # ClassName,ColumnName
    resources: Mapped[List['Resource']] = relationship(back_populates='word')
    memory: Mapped['Memory'] = relationship(back_populates='word')

    score: Mapped[float] = mapped_column(nullable=True, default=0.0)
    is_exposed: Mapped[bool] = mapped_column(nullable=True, default=False)
    is_memorized: Mapped[bool] = mapped_column(nullable=True, default=False)
    half_life_days: Mapped[int] = mapped_column(nullable=True, default=1)


class Resource(Base):
    __tablename__ = 'resource'
    id: Mapped[int] = mapped_column(primary_key=True)
    resource: Mapped[str] = mapped_column(String(100), nullable=False)
    freq: Mapped[int] = mapped_column(nullable=True)

    word_id: Mapped[int] = mapped_column(ForeignKey('word.id'))
    word: Mapped['Word'] = relationship(back_populates='resources')


class Memory(Base):
    __tablename__ = 'memory'
    id: Mapped[int] = mapped_column(primary_key=True)

    word_id: Mapped[int] = mapped_column(ForeignKey('word.id'))
    word: Mapped['Word'] = relationship(back_populates='memory')


class Definition(Base):
    __tablename__ = 'definition'
    id: Mapped[int] = mapped_column(primary_key=True)
    definition: Mapped[str] = mapped_column(String(200), nullable=True)
    pos: Mapped[str] = mapped_column(String(50), nullable=True)

    word_id: Mapped[int] = mapped_column(ForeignKey('word.id'))  # tableName.columnName
    word: Mapped['Word'] = relationship(back_populates='definitions')
    sentences: Mapped[List['Sentence']] = relationship(back_populates='definition')


class Sentence(Base):
    __tablename__ = 'sentence'
    id: Mapped[int] = mapped_column(primary_key=True)
    sentence: Mapped[str] = mapped_column(String(200), nullable=True)

    definition_id: Mapped[int] = mapped_column(ForeignKey('definition.id'))
    definition: Mapped['Definition'] = relationship(back_populates='sentences')


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)


class DataBase:
    def __init__(self, path='sqlite:///database.db'):
        self.engine = create_engine(path)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def createTable(self):
        Base.metadata.create_all(self.engine)

    def insert(self, instance):
        if isinstance(instance, list):
            for ins in instance:
                self.session.add(ins)
            self.session.commit()
        else:
            self.session.add(instance)
            self.session.commit()

    def searchDict(self, w) -> Optional[Word]:
        stmt = select(Word).where(Word.word == w)
        return self.session.scalars(stmt).one_or_none()

    def get_resc(self):
        stmt = select(Resource.resource, func.count(Resource.word_id)).group_by(Resource.resource)
        return self.session.execute(stmt).all()

    def get_item(self, r):
        stmt = select(Word.word, Resource.freq).join(Word).where(Resource.resource == r).order_by(Word.word)
        result = self.session.execute(stmt).all()

        return [{'text': word, 'rtext': f"{freq}"} for word, freq in result]


if __name__ == '__main__':
    db = DataBase('sqlite:///../database.db')
    result = db.searchDict('123445')
    a = db.get_resc()
    b = db.get_item("Les assassins de la 5e-B.pdf")

    print(1)






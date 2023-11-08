from typing import Optional, Sequence, Dict, List, Tuple, Any
from sqlalchemy import create_engine, String, ForeignKey, Column, Integer, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import func, desc, case, and_, or_
import logging
from typing import List

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.ERROR)

Base = declarative_base()


class Word(Base):
    __tablename__ = 'word'
    id = Column(Integer, primary_key=True)
    word = Column(String(100), nullable=False, index=True)

    definitions = relationship("Definition", back_populates='word')  # ClassName,ColumnName
    resources = relationship("Resource", back_populates='word')
    memory = relationship("Memory", back_populates='word')

    score = Column(Float, nullable=True, default=0.0)
    is_exposed = Column(Boolean, nullable=True, default=False)
    is_memorized = Column(Boolean, nullable=True, default=False)
    half_life_days = Column(Integer, nullable=True, default=1)


class Resource(Base):
    __tablename__ = 'resource'
    id = Column(Integer, primary_key=True)
    resource = Column(String(100), nullable=False)

    freq = Column(Integer, nullable=True)
    word_id = Column(ForeignKey('word.id'))
    word = relationship("Word", back_populates='resources')


class Memory(Base):
    __tablename__ = 'memory'
    id = Column(Integer, primary_key=True)
    word_id = Column(ForeignKey('word.id'))

    word = relationship("Word", back_populates='memory')


class Definition(Base):
    __tablename__ = 'definition'
    id = Column(Integer, primary_key=True)
    definition = Column(String(200), nullable=True)
    pos = Column(String(50), nullable=True)
    word_id = Column(ForeignKey('word.id'))
    word = relationship('Word', back_populates='definitions')
    sentences = relationship('Sentence', back_populates='definition')


class Sentence(Base):
    __tablename__ = 'sentence'
    id = Column(Integer, primary_key=True)
    sentence = Column(String(200), nullable=True)
    definition_id = Column(ForeignKey('definition.id'))
    definition = relationship('Definition', back_populates='sentences')


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)


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

    def get_def(self, w: str) -> Optional[Word]:
        return (self.session.query(Word)
                .filter(Word.word == w)
                .one_or_none())

    def get_memo(self) -> Sequence[Word]:
        return (self.session.query(Word)
                .join(Memory)
                .filter(Word.is_memorized == False)
                .order_by(desc(func.lower(Word.word))).all())

    def get_resc(self):
        return (self.session.query(Resource.resource,
                                   func.count(Resource.word_id))
                .group_by(Resource.resource).all())

    def get_item(self, r) -> List[Tuple[Any, ...]]:
        return (self.session.query(Word.word, Resource.freq, Word.is_memorized, Word.is_exposed, Word.score)
                .join(Resource)
                .filter(Resource.resource == r)
                .order_by(desc(func.lower(Word.word))).all())

    def get_freq(self, w):
        return (self.session.query(Resource.resource, Resource.freq)
                .join(Word)
                .filter(Word.word == w)
                .order_by(desc(Resource.freq))
                .limit(3)
                .all())

    def get_progress(self):
        progress = self.session.query(func.count(Word.id),
                                      func.sum(case([(Word.is_exposed == True, 1)], else_=0)),
                                      func.sum(case([(and_(Word.score < 150, Word.is_exposed == True, Word.is_memorized == False), 1)], else_=0)),
                                      func.sum(case([(or_(Word.is_memorized == True, Word.score >= 150), 1)], else_=0))
                                      ).join(Memory).one_or_none()
        if progress:
            return progress
        else:
            return 0, 0, 0, 0

    def add_memo(self, r):
        words = (self.session.query(Word.id, Word.word)
                 .join(Resource)
                 .filter(Resource.resource == r)
                 .all())
        memories = []
        for word_id, word in words:
            existing_word = (self.session.query(Memory)
                             .filter(Memory.word_id == word_id)
                             .one_or_none())
            if not existing_word:
                memo = Memory(word_id=word_id)
                memories.append(memo)
        self.session.add_all(memories)
        self.session.commit()

    def init_task(self):
        self.session.query(Memory).delete()
        self.session.commit()

    def init_memo(self):
        words = (self.session.query(Word)
                 .filter(Word.is_exposed == True)
                 .all())

        for word in words:
            word.score = 0.0
            word.is_memorized = False
            word.is_exposed = False
            word.half_life_days = 1

        self.session.commit()


if __name__ == '__main__':
    db = DataBase('sqlite:///../database.db')
    result = db.get_def('vanter')
    result = db.get_freq('abandonner')
    a = db.get_progress()
    print(1)
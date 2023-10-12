import random
import time
from datetime import datetime
from typing import List
from enum import Enum
from utils.database import Word
from utils.timeop import getTimestampForDawn, getDaysBetweenTimestamp


class Action(Enum):
    memorized = 1
    blurred = 2
    forgetful = 3


class MemoryQueue:
    def __init__(self, db, conf):
        self.db = db
        self.conf = conf
        lastUpdateTime = conf.get_config('lastUpdateTime', datetime.now().timestamp())
        conf.set_config('lastUpdateTime', time.time())

        self.word_total: List[Word] = self.db.get_memo()
        self.word_queue: List[Word] = []
        self.memory_decay_daily(lastUpdateTime)

    def refresh(self):
        self.word_queue: List[Word] = self.db.get_memo()

    @staticmethod
    def memory_decay(days, half_life_days, score):
        return int(pow(0.5, days / half_life_days) * score)

    def memory_decay_daily(self, lastUpdateTime):
        days = - getDaysBetweenTimestamp(lastUpdateTime, getTimestampForDawn())
        for word in self.word_total:
            score = word.score
            if score > 0 and days > 1:
                # 重新赋值单词记忆分
                word.score = self.memory_decay(days, word.half_life_days, score)
            if word.score < 150:
                self.word_queue.append(word)
        self.db.session.commit()

    def pop_memory(self):
        if self.word_queue:
            return self.word_queue.pop(0)

    def modify_memory(self, memo: Word, action: Action):
        # 如果没曝光的单词首次曝光，如果认识就不再出现，如果模糊就+100分，如果不认识就不加分
        if not memo.is_exposed:
            memo.is_exposed = True
            if action == Action.memorized:
                memo.is_memorized = True
            elif action == Action.blurred:
                memo.score = 100
                self._add_to_queue(memo)
            elif action == Action.forgetful:
                memo.score += 0
                self._add_to_queue(memo)
        else:
            if action == Action.memorized:
                memo.score += 200
                if memo.score >= 300:
                    memo.score = 300
                    memo.half_life_days *= 2
                else:
                    self._add_to_queue(memo)
            if action == Action.blurred:
                memo.score += 50
                if memo.score >= 149:
                    memo.score = 149
                self._add_to_queue(memo)
            if action == Action.forgetful:
                if memo.score >= 149:
                    memo.score = 149
                self._add_to_queue(memo)
        self.db.session.commit()

    def _add_to_queue(self, memo: Word):
        r = random.randint(5, 20)
        if len(self.word_queue) >= r:
            self.word_queue.insert(r, memo)
        else:
            self.word_queue.append(memo)

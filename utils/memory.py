import random
from typing import List
from enum import Enum
from utils.database import Memory
from utils.timeop import getTimestampForDawn, getDaysBetweenTimestamp


class Action(Enum):
    memorized = 1
    blurred = 2
    forgetful = 3


class MemoryQueue:
    def __init__(self, lastUpdateTime=0):
        self.word_total: List[Memory] = []
        self.word_queue: List[Memory] = []
        self.memory_decay_daily(lastUpdateTime)

    @staticmethod
    def memory_decay(days, half_life_days, score):
        return int(pow(0.5, days / half_life_days) * score)

    def memory_decay_daily(self, lastUpdateTime):

        days = getDaysBetweenTimestamp(lastUpdateTime, getTimestampForDawn())
        for word in self.word_total:
            score = word.word.score
            if score > 0 and days >= 1:
                # 重新赋值单词记忆分
                word.word.score = self.memory_decay(days, word.word.half_life_days, score)
                if word.word.score < 150:
                    self.word_queue.append(word)
            else:
                self.word_queue.append(word)

    def pop_memory(self) -> Memory:
        return self.word_queue.pop(0)

    def modify_memory(self, memo: Memory, action: Action):
        # 如果没曝光的单词首次曝光，如果认识就不再出现，如果模糊就+100分，如果不认识就不加分
        if not memo.word.is_exposed:
            memo.word.is_memorized = True
            if action == Action.memorized:
                memo.word.is_exposed = True
            elif action == Action.blurred:
                memo.word.score = 100
                self._add_to_queue(memo)
            elif action == Action.forgetful:
                memo.word.score += 0
                self._add_to_queue(memo)

        # 如果曝光的单词再次出现，那一定是第一轮没有认识的
        if memo.word.is_exposed:
            if action == Action.memorized:
                memo.word.score += 200
                if memo.word.score >= 300:
                    memo.word.score = 300
                    memo.word.half_life_days *= 2
                else:
                    self._add_to_queue(memo)

            if action == Action.blurred:
                memo.word.score += 50
                if memo.word.score >= 300:
                    memo.word.score = 300
                self._add_to_queue(memo)
            if action == Action.forgetful:
                self._add_to_queue(memo)

    def _add_to_queue(self, memo: Memory):
        r = random.randint(5, 20)
        if len(self.word_queue) < r:
            self.word_queue.insert(r, memo)
        else:
            self.word_queue.append(memo)

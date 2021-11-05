from abc import ABC, abstractmethod
import praw
import os

class Source(ABC):

  @abstractmethod
  def connect(self):
    pass

  @abstractmethod
  def fetch(self):
    pass


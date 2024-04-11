from abc import ABC, abstractmethod


class StorySource(ABC):
    @abstractmethod
    def get_story(self):
        pass


class Book(StorySource):
    def get_story(self):
        print("The story is being read.")


class AudioBook(StorySource):
    def get_story(self):
        print("The audio book is being played.")


class StoryReader:
    def __init__(self, story_source: StorySource):
        self.story_source = story_source

    def tell_story(self):
        self.story_source.get_story()


book = Book()
book_reader = StoryReader(book)
book_reader.tell_story()

audio_book = AudioBook()
book_reader = StoryReader(audio_book)
book_reader.tell_story()

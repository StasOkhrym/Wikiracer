import re
from collections import deque

from sqlalchemy.orm import sessionmaker, Query
from wikipediaapi import Wikipedia, WikipediaPage

from model import engine, Article


class WikiRacer:
    def __init__(self):
        self.session = sessionmaker(bind=engine)()
        self.wikipedia = Wikipedia(language="uk")

    def find_path(self, start: str, finish: str) -> list[str | None]:
        visited = {start: None}
        queue = deque([start])

        while queue:
            current = queue.popleft()
            article_queryset = self.check_if_exists_or_create(current)
            if article_queryset:
                for article in article_queryset:
                    if article.child not in visited:
                        visited[article.child] = current
                        queue.append(article.child)
                        if article.child == finish:
                            return self.construct_path(visited, article.child)
        return []

    @staticmethod
    def construct_path(visited: dict, finish: str) -> list[str]:
        path = [finish]
        parent = visited[finish]
        while parent:
            path.append(parent)
            parent = visited[parent]
        path.reverse()
        return path

    def check_if_exists_or_create(self, article_name: str) -> Query | None:
        article_queryset = self.session.query(Article).filter_by(
            parent=article_name
        )
        if article_queryset.count() > 0:
            return article_queryset
        else:
            page = self.wikipedia.page(article_name)
            if page.exists():
                new_article_queryset = self.create_and_write_to_db(page)

                return new_article_queryset
            return None

    def create_and_write_to_db(self, wiki_page: WikipediaPage) -> Query | None:
        article_name = wiki_page.title
        links = [link for link in wiki_page.links if self.verify_name(link)][
            :200
        ]

        if not links:
            return None

        for link in links:
            new_article = Article(parent=article_name, child=link)
            self.session.add(new_article)

        self.session.commit()

        new_article_queryset = self.session.query(Article).filter_by(
            parent=article_name
        )

        return new_article_queryset

    @staticmethod
    def verify_name(article_name: str) -> bool:
        cyrillic_pattern = re.compile(r"^[А-ЯІЇЄҐа-яіїєґ0-9]+")
        if cyrillic_pattern.match(article_name) and ":" not in article_name:
            return True
        else:
            return False

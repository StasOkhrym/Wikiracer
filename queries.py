from sqlalchemy import func, desc
from sqlalchemy.orm import sessionmaker

from model import Article, engine

session = sessionmaker(bind=engine)()


def top_5_most_popular_articles() -> list[tuple]:
    return (
        session.query(
            Article.parent, func.count(Article.parent).label("popularity")
        )
        .group_by(Article.parent)
        .order_by(desc("popularity"))
        .limit(5)
        .all()
    )


def top_5_with_most_links_to_other() -> list[tuple]:
    return (
        session.query(Article.parent, func.count(Article.parent))
        .group_by(Article.parent)
        .order_by(func.count(Article.parent).desc())
        .limit(5)
        .all()
    )


def average_descendants(article_name: str) -> float:
    subquery = (
        session.query(Article.child)
        .filter(Article.parent == article_name)
        .subquery()
    )
    first_level_descendants = (
        session.query(Article.child)
        .filter(Article.parent == article_name)
        .count()
    )
    second_level_descendants = (
        session.query(Article.child)
        .filter(Article.parent.in_(subquery))
        .count()
    )
    average = second_level_descendants / first_level_descendants
    return average

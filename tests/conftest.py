from typing import Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from warehouse_management.infrastructure.orm import Base


@pytest.fixture(scope="module")
def session() -> Generator[Session, None, None]:

    DATABASE_URL = "sqlite:///:memory:"

    engine = create_engine(DATABASE_URL)
    SessionFactory = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = SessionFactory()
    yield session

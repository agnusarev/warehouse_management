from domain.services import WarehouseService
from infrastructure.database import DATABASE_URL
from infrastructure.repositories import (
    SqlAlchemyOrderRepository,
    SqlAlchemyProductRepository,
)
from infrastructure.unit_of_work import SqlAlchemyUnitOfWork
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URL)
SessionFactory = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


def main() -> None:
    session = SessionFactory()
    product_repo = SqlAlchemyProductRepository(session)
    order_repo = SqlAlchemyOrderRepository(session)

    uow = SqlAlchemyUnitOfWork(session)

    warehouse_service = WarehouseService(product_repo, order_repo)
    with uow:
        new_product = warehouse_service.create_product(
            name="test1", quantity=1, price=100
        )
        uow.commit()
        print(f"create product: {new_product}")
        # todo add some actions


if __name__ == "__main__":
    main()

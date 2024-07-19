from sqlalchemy.orm import Session

from warehouse_management.domain.services import WarehouseService
from warehouse_management.infrastructure.repositories import (
    SqlAlchemyOrderRepository,
    SqlAlchemyProductRepository,
)
from warehouse_management.infrastructure.unit_of_work import SqlAlchemyUnitOfWork

# TODO подумать над тестом
def test_warehouse_servise(session: Session) -> None:
    product_repo = SqlAlchemyProductRepository(session)
    order_repo = SqlAlchemyOrderRepository(session)

    warehouse_service = WarehouseService(product_repo, order_repo)
    with SqlAlchemyUnitOfWork(session) as uow:
        new_product = warehouse_service.create_product(
            name="test1", quantity=1, price=100, category=10,
        )
        print(f"create product: {new_product}")
        uow.commit()
        assert True

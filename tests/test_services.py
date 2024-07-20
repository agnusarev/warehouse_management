from sqlalchemy.orm import Session

from warehouse_management.domain.services import WarehouseService
from warehouse_management.infrastructure.repositories import (
    # SqlAlchemyOrderRepository,
    SqlAlchemyProductRepository,
)

def test_services(session: Session) -> None:
    product_repo = SqlAlchemyProductRepository(session)

    warehouse_service = WarehouseService(product_repo)
    new_product = warehouse_service.create_product(
        name="test1", quantity=1, price=100, category=10,
    )
    assert new_product

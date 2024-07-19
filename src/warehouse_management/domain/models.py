from dataclasses import dataclass, field
from typing import List


@dataclass
class Product:
    id: int
    name: str
    quantity: int
    price: float
    category: int


@dataclass
class Category:
    id: int
    name: str
    description: str
    products: List[Product] = field(default_factory=list)

    def add_product(self, product: Product) -> None:
        self.products.append(product)


@dataclass
class Order:
    id: int
    products: List[Product] = field(default_factory=list)

    def add_product(self, product: Product) -> None:
        self.products.append(product)


@dataclass
class Customer:
    id: int
    first_name: str
    last_name: str
    address: str
    phone: str
    email: str
    staff_id: int


@dataclass
class Staff:
    id: int
    first_name: str
    last_name: str
    address: str
    phone: str
    email: str
    user_name: str
    role_id: int
    customers: List[Customer] = field(default_factory=list)


@dataclass
class Role:
    id: int
    name: str
    description: str
    staffs: List[Staff] = field(default_factory=list)

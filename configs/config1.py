from src.page import *


def config1():
    url = "https://www.geneevarojr.com/wp-content/uploads/2020/10/Sample-Retail-Invoice-Template.jpg?fit=1300%2C1838&ssl=1"
    page = construct_page(
        H(1, [V(6, id="title"), V(4, id="logo")]),
        H(2, id="address-1"),
        H(5, [V(1, id="address-2"), V(1, id="address-3"), V(1, id="address-4")]),
        H(12, id="table"),
        H(4, [V(6, id="paragraph"), V(4, id="total-table")]),
        H(5, id="paragraph"),
    )
    return page

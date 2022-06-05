import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def RolonSeals():
    page = construct_page(
        H(1, id="SellerInfo"),
        H(
            1.8,
            [
                V(5, id="BuyerInfo"),
                V(5, id="InvoiceInfo"),
            ],
        ),
        H(0.2, id="Notes"),
        H(3.2, id="Table"),
        H(2.8, id="Terms"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = RolonSeals()
    page.generate(1000, 800)
    page.show(save_path="layout_images/RolonSeals.png", texts="id")
    

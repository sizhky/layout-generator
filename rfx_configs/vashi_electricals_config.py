import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def VashiElectricals():
    page = construct_page(
        H(
            1,
            [
                V(7, id="SellerInfo"),
                V(3, id="OrderNo"),
            ],
        ),
        H(
            0.8,
            [
                V(1, id="BuyerAddress"),
                V(1, id="BuyerContact"),
            ],
        ),
        H(
            1,
            [
                V(1, id="InvoiceInfo"),
                V(1, id="PaymentType"),
            ],
        ),
        H(0.5, id="Comments"),
        H(1.2, id="Table"),
        H(0.8, id="Notes"),
        H(1.2, id="Terms"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = VashiElectricals()
    page.generate(1000, 800)
    page.show(save_path="layout_images/VashiElectricals.png", texts="id")
    

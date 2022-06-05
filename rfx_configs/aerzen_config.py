import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def Aerzen():
    page = construct_page(
        H(
            2,
            [
                V(
                    1.2,
                    [
                        H(1),
                        H(2, id="BuyerInfo"),
                    ],
                ),
                V(1),
                V(
                    1,
                    [
                        H(1, id="Logo"),
                        H(2, id="SellerInfo"),
                    ],
                ),
            ],
        ),
        H(1, id="InvoiceInfo"),
        H(1, id="Account"),
        H(2, id="Table"),
        H(
            0.5,
            [
                V(1.5),
                V(1, id="Total"),
            ],
        ),
        H(0, id="padding"),
        H(2, id="Footer"),
    )
    return page




if __name__ == "__main__":
    page = Aerzen()
    page.generate(1000, 800)
    page.show(save_path="layout_images/Aerzen.png", texts="id")
    

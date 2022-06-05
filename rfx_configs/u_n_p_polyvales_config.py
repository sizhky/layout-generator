import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def UNPPolyvales():
    page = construct_page(
        H(1, id="SellerName"),
        H(
            3,
            [
                V(
                    1,
                    [
                        H(1.3, id="SellerInfo"),
                        H(1.7, id="BuyerInfo"),
                    ],
                ),
                V(
                    1,
                    [
                        H(1.3, id="DueDate"),
                        H(1.7, id="ShipInfo"),
                    ],
                ),
            ],
        ),
        H(4, id="Table"),
        H(1.5, id="AmountBreakup"),
        H(
            0.5,
            [
                V(6, id="Notes"),
                V(4, id="Sign"),
            ],
        ),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = UNPPolyvales()
    page.generate(1000, 800)
    page.show(save_path="layout_images/UNPPolyvales.png", texts="id")
    

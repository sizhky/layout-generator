import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def Leser():
    page = construct_page(
        H(1, id="SellerName"),
        H(
            5,
            [
                V(
                    1,
                    [
                        H(2.5, id="BuyerInfo"),
                        H(1.5, id="Date"),
                        H(1, id="OrderNo"),
                    ],
                ),
                V(
                    1,
                    [
                        H(1, id="SellerContact"),
                        H(1, id="SellerPOC"),
                        H(1, id="BuyerContact"),
                    ],
                ),
            ],
        ),
        H(4, id="Notes"),
        H(1, id="Sign"),
        H(
            2,
            [
                V(1, id="SellerAddress"),
                V(1, id="SellerInfo"),
            ],
        ),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = Leser()
    page.generate(1000, 800)
    page.show(save_path="layout_images/Leser.png", texts="id")
    

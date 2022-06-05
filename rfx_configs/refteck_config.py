import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def Refteck():
    page = construct_page(
        H(
            1,
            [
                V(5, id="SellerName"),
                V(5, id="SellerInfo"),
            ],
        ),
        H(
            1.8,
            [
                V(5, id="BuyerInfo"),
                V(5, id="Total"),
            ],
        ),
        H(1, id="Notes"),
        H(6, id="Table"),
        H(0, id="padding"),
        H(0.5, id="Footer"),
    )
    return page




if __name__ == "__main__":
    page = Refteck()
    page.generate(1000, 800)
    page.show(save_path="layout_images/Refteck.png", texts="id")
    

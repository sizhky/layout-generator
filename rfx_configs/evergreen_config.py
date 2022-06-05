import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def Evergreen():
    page = construct_page(
        H(1, id="SellerName"),
        H(
            0.4,
            [
                V(2, id="Date"),
                V(2, id="DueDate"),
            ],
        ),
        H(
            1.6,
            [
                V(2, id="SellerInfo"),
                V(2, id="BuyerInfo"),
            ],
        ),
        H(5, id="Table"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = Evergreen()
    page.generate(1000, 800)
    page.show(save_path="layout_images/Evergreen.png", texts="id")
    

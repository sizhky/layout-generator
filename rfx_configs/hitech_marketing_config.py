import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def HitechMarketing():
    page = construct_page(
        H(1, id="SellerInfo"),
        H(
            1,
            [
                V(1, id="BuyerInfo"),
                V(1, id="Orderno"),
                V(1, id="Date"),
            ],
        ),
        H(1, id="Table"),
        H(1, id="Terms"),
        H(1, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = HitechMarketing()
    page.generate(1000, 800)
    page.show(save_path="layout_images/HitechMarketing.png", texts="id")
    

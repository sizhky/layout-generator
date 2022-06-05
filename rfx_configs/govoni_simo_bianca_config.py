import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def GovoniSimoBianca():
    page = construct_page(
        H(
            1,
            [
                V(1),
                V(1, id="SellerInfo"),
            ],
        ),
        H(1, id="BuyerInfo"),
        H(0.5, id="Notes"),
        H(2.5, id="Table"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = GovoniSimoBianca()
    page.generate(1000, 800)
    page.show(save_path="layout_images/GovoniSimoBianca.png", texts="id")
    

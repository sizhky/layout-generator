import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def NationalAccreditationBoard():
    page = construct_page(
        H(1, id="SellerName"),
        H(
            1.5,
            [
                V(7, id="BuyerInfo"),
                V(5, id="Date"),
            ],
        ),
        H(3.5, id="Notes"),
        H(0.5, id="Sign"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = NationalAccreditationBoard()
    page.generate(1000, 800)
    page.show(save_path="layout_images/NationalAccreditationBoard.png", texts="id")
    

import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def LamtechSolutions():
    page = construct_page(
        H(
            1,
            [
                V(1, id="Date"),
                V(1, id="SellerName"),
            ],
        ),
        H(1.5, id="BuyerInfo"),
        H(2.7, id="Notes"),
        H(1.2, id="Sign"),
        H(1.2, id="SellerPOC"),
        H(0, id="padding"),
        H(0.7, id="Footer"),
    )
    return page




if __name__ == "__main__":
    page = LamtechSolutions()
    page.generate(1000, 800)
    page.show(save_path="layout_images/LamtechSolutions.png", texts="id")
    

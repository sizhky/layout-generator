import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def AndersonGreenwoodCrosbySanmar():
    page = construct_page(
        H(1, id="SellerInfo"),
        H(
            1.3,
            [
                V(1, id="BuyerInfo"),
                V(1, id="DueDate"),
            ],
        ),
        H(1, id="Table"),
        H(
            1.3,
            [
                V(1, id="Notes"),
                V(1, id="AmountBreakup"),
            ],
        ),
        H(0.8, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = AndersonGreenwoodCrosbySanmar()
    page.generate(1000, 800)
    page.show(save_path="layout_images/AndersonGreenwoodCrosbySanmar.png", texts="id")
    

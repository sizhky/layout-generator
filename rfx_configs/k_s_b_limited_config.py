import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def KSBLimited():
    page = construct_page(
        H(
            1,
            [
                V(1, id="BuyerName"),
                V(1, id="SellerName"),
            ],
        ),
        H(0.5, id="Comments"),
        H(4.5, id="Table"),
    )
    return page




if __name__ == "__main__":
    page = KSBLimited()
    page.generate(1000, 800)
    page.show(save_path="layout_images/KSBLimited.png", texts="id")
    

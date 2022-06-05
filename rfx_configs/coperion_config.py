import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def Coperion():
    page = construct_page(
        H(
            1,
            [
                V(2, id="SellerName"),
                V(2, id="Header"),
            ],
        ),
        H(0.7, id="Date"),
        H(2.5, id="Table"),
        H(1.2, id="AmountBreakup"),
        H(3, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = Coperion()
    page.generate(1000, 800)
    page.show(save_path="layout_images/Coperion.png", texts="id")
    

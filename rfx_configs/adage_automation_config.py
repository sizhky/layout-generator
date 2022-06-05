import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def AdageAutomation():
    page = construct_page(
        H(
            1,
            [
                V(1, id="SellerName"),
                V(1, id="SellerInfo"),
            ],
        ),
        H(0.3, id="Header"),
        H(2, id="Table"),
        H(3, id="padding"),
        H(0.5, id="Footer"),
    )
    return page




if __name__ == "__main__":
    page = AdageAutomation()
    page.generate(1000, 800)
    page.show(save_path="layout_images/AdageAutomation.png", texts="id")
    

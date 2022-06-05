import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def YokogawaIndia():
    page = construct_page(
        H(
            1.4,
            [
                V(
                    2,
                    [
                        H(0.5, id="SellerName"),
                        H(0.7, id="BuyerName"),
                    ],
                ),
                V(1),
            ],
        ),
        H(1, id="Table"),
        H(1, id="Notes"),
        H(1.4, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = YokogawaIndia()
    page.generate(1000, 800)
    page.show(save_path="layout_images/YokogawaIndia.png", texts="id")
    

import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def Reliance():
    ## Seems like an internal reliance delivery
    page = construct_page(
        H(1),
        H(0.3, id="OrderNo"),
        H(
            1.5,
            [
                V(1, id="BuyerInfo"),
                V(1, id="ShipInfo"),
            ],
        ),
        H(1, id="Table"),
        H(2, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = Reliance()
    page.generate(1000, 800)
    page.show(save_path="layout_images/Reliance.png", texts="id")
    

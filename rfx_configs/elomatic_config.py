import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def Elomatic():
    page = construct_page(
        H(0.5, id="Header"),
        H(
            1,
            [
                V(3, id="BuyerInfo"),
                V(2, id="Header"),
                V(4),
            ],
        ),
        H(5, id="Table"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = Elomatic()
    page.generate(1000, 800)
    page.show(save_path="layout_images/Elomatic.png", texts="id")
    

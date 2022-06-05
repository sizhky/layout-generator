import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def BidHeavyMetalsTubes():
    page = construct_page(
        H(1, id="Header"),
        H(
            1,
            [
                V(1, id="BuyerInfo"),
                V(1, id="Date"),
            ],
        ),
        H(0.3, id="Notes"),
        H(4, id="Table"),
        H(2, id="Terms"),
        H(1, id="Footer"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = BidHeavyMetalsTubes()
    page.generate(1000, 800)
    page.show(save_path="layout_images/BidHeavyMetalsTubes.png", texts="id")
    

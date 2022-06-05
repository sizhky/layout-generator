import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def PriceSchedule():
    page = construct_page(
        H(
            0.3,
            [
                V(1),
                V(1, id="Header"),
                V(1, id="Date"),
                V(1),
            ],
        ),
        H(1.5, id="Table"),
        H(3, id="Terms"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = PriceSchedule()
    page.generate(1000, 800)
    page.show(save_path="layout_images/PriceSchedule.png", texts="id")
    

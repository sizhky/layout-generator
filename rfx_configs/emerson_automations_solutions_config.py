import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def EmersonAutomationsSolutions():
    page = construct_page(
        H(
            2,
            [
                V(1, id="BuyerInfo"),
                V(1),
                V(1, id="SellerInfo"),
            ],
        ),
        H(1, id="Table"),
        H(
            2,
            [
                V(1, id="Terms"),
                V(1),
            ],
        ),
        H(0.5, id="Sign"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = EmersonAutomationsSolutions()
    page.generate(1000, 800)
    page.show(save_path="layout_images/EmersonAutomationsSolutions.png", texts="id")
    

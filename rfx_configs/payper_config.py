import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def Payper():
    page = construct_page(
        H(
            1,
            [
                V(1, id="SellerInfo"),
                V(1, id="Header"),
            ],
        ),
        H(
            1.2,
            [
                V(1, id="Date"),
                V(1, id="BuyerInfo"),
            ],
        ),
        H(4.3, id="Table"),
        H(0.5, id="Amount"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = Payper()
    page.generate(1000, 800)
    page.show(save_path="layout_images/Payper.png", texts="id")
    

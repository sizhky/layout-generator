import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def AalidhraTextoolEngineers():
    page = construct_page(
        H(1, id="SellerInfo"),
        H(
            1,
            [
                V(2, id="BuyerName"),
                V(2, id="DueDate"),
            ],
        ),
        H(7.5, id="Table"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = AalidhraTextoolEngineers()
    page.generate(1000, 800)
    page.show(save_path="layout_images/AalidhraTextoolEngineers.png", texts="id")
    

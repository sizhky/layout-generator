import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def NirmalIndustrialControls():
    page = construct_page(
        H(1, id="SellerInfo"),
        H(0.2, id="Date"),
        H(
            1.8,
            [
                V(1, id="BuyerInfo"),
                V(1, id="OrderNo"),
            ],
        ),
        H(1, id="Table"),
        H(3, id="Terms"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = NirmalIndustrialControls()
    page.generate(1000, 800)
    page.show(save_path="layout_images/NirmalIndustrialControls.png", texts="id")
    

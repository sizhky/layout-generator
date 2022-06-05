import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def QuotationRefteck():
    page = construct_page(
        H(
            1,
            [
                V(1, id="SellerInfo"),
                V(1, id="Date"),
            ],
        ),
        H(0.5, id="Notes"),
        H(4, id="Table"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = QuotationRefteck()
    page.generate(1000, 800)
    page.show(save_path="layout_images/QuotationRefteck.png", texts="id")
    

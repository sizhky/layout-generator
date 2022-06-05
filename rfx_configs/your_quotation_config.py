import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def YourQuotation():
    page = construct_page(
        H(1, id="Header"),
        H(
            2,
            [
                V(1, id="SellerInfo"),
                V(1, id="Date"),
            ],
        ),
        H(0.5, id="BuyerName"),
        H(1, id="InvoiceInfo"),
        H(
            2,
            [
                V(1, id="Comments"),
                V(1, id="BuyerInfo"),
            ],
        ),
        H(1.5, id="Table"),
        H(
            1,
            [
                V(1),
                V(1, id="Amount"),
            ],
        ),
        H(
            1,
            [
                V(1, id="Terms"),
                V(1),
            ],
        ),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = YourQuotation()
    page.generate(1000, 800)
    page.show(save_path="layout_images/YourQuotation.png", texts="id")
    

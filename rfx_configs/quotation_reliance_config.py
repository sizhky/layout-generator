import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def QuotationReliance():
    page = construct_page(
        H(0.2, id="Header"),
        H(
            1,
            [
                V(1, id="BuyerInfo"),
                V(1, id="InvoiceInfo"),
            ],
        ),
        H(2.2, id="Table"),
        H(1.3, id="Notes"),
        H(1, id="Tax"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = QuotationReliance()
    page.generate(1000, 800)
    page.show(save_path="layout_images/QuotationReliance.png", texts="id")
    

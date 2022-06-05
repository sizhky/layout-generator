import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def QuotationSweloreEngineering():
    page = construct_page(
        H(1),
        H(0.3, id="Header"),
        H(
            1,
            [
                V(1, id="SellerInfo"),
                V(1, id="InvoiceInfo"),
            ],
        ),
        H(2, id="Table"),
        H(2, id="Terms"),
        H(0, id="padding"),
        H(1, id="Footer"),
    )
    return page




if __name__ == "__main__":
    page = QuotationSweloreEngineering()
    page.generate(1000, 800)
    page.show(save_path="layout_images/QuotationSweloreEngineering.png", texts="id")
    

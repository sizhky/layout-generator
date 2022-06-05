import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def QuotationReliance2():
    page = construct_page(
        H(
            1,
            [
                V(1, id="SellerAddress"),
                V(1, id="SellerAddress2"),
                V(1, id="TaxInfo"),
            ],
        ),
        H(0.5, id="Header"),
        H(
            1.2,
            [
                V(1, id="BuyerInfo"),
                V(1, id="Date"),
            ],
        ),
        H(0.5, id="Notes"),
        H(1.2, id="Table"),
        H(1.2, id="Terms"),
        H(0, id="padding"),
        H(0.7, id="Footer"),
    )
    return page




if __name__ == "__main__":
    page = QuotationReliance2()
    page.generate(1000, 800)
    page.show(save_path="layout_images/QuotationReliance2.png", texts="id")
    

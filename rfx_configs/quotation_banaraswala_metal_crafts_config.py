import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def QuotationBanaraswalaMetalCrafts():
    page = construct_page(
        H(1, id="Header"),
        H(
            3,
            [
                V(
                    2,
                    [
                        H(1, id="BuyerInfo"),
                        H(1.5, id="OrderNo"),
                    ],
                ),
                V(2, id="SellerPOC"),
            ],
        ),
        H(1.5, id="Table"),
        H(
            1,
            [
                V(4),
                V(6, id="AmountBreakup"),
            ],
        ),
        H(2, id="padding"),
        H(1, id="Footer"),
    )
    return page




if __name__ == "__main__":
    page = QuotationBanaraswalaMetalCrafts()
    page.generate(1000, 800)
    page.show(save_path="layout_images/QuotationBanaraswalaMetalCrafts.png", texts="id")
    

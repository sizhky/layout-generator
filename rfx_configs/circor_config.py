import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def Circor():
    page = construct_page(
        H(
            1,
            [
                V(6, id="Logo"),
                V(4, id="SellerInfo"),
            ],
        ),
        H(
            2.5,
            [
                V(1, id="BuyerInfo"),
                V(1, id="InvoiceInfo"),
            ],
        ),
        H(1, id="SellerPOC"),
        H(2, id="Table"),
        H(1, id="AmountBreakup"),
        H(0.5, id="Footer"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = Circor()
    page.generate(1000, 800)
    page.show(save_path="layout_images/Circor.png", texts="id")
    

import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def Quotation():
    page = construct_page(
        H(1),
        H(0.3, id="Header"),
        H(
            1.5,
            [
                V(1),
                V(1, id="InvoiceInfo"),
            ],
        ),
        H(
            0.5,
            [
                V(1, id="BuyerInfo"),
                V(1, id="ShipInfo"),
            ],
        ),
        H(1.3, id="Table"),
        H(
            0.7,
            [
                V(7),
                V(3, id="AmountBreakup"),
            ],
        ),
        H(2, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = Quotation()
    page.generate(1000, 800)
    page.show(save_path="layout_images/Quotation.png", texts="id")
    

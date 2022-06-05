import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def Simpex():
    page = construct_page(
        H(
            3,
            [
                V(
                    1,
                    [
                        H(2, id="Logo"),
                        H(0.5, id="BuyerName"),
                        H(1.5, id="BuyerInfo"),
                    ],
                ),
                V(
                    1,
                    [
                        H(2, id="InvoiceInfo"),
                        H(0.5, id="BuyerContact"),
                        H(1.5),
                    ],
                ),
            ],
        ),
        H(1, id="Notes"),
        H(1.5, id="Table"),
        H(
            1.5,
            [
                V(1, id="PaymentType"),
                V(1, id="AmountBreakup"),
            ],
        ),
        H(0, id="padding"),
        H(0.3, id="Footer"),
    )
    return page




if __name__ == "__main__":
    page = Simpex()
    page.generate(1000, 800)
    page.show(save_path="layout_images/Simpex.png", texts="id")
    

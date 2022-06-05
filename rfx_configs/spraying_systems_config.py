import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def SprayingSystems():
    page = construct_page(
        H(1, id="SellerName"),
        H(
            3,
            [
                V(2, id="BuyerName"),
                V(2, id="InvoiceInfo"),
            ],
        ),
        H(1, id="Notes"),
        H(1.5, id="Table"),
        H(3, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = SprayingSystems()
    page.generate(1000, 800)
    page.show(save_path="layout_images/SprayingSystems.png", texts="id")
    

import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def Mistras():
    page = construct_page(
        H(
            2,
            [
                V(1, id="TaxInfo"),
                V(1, id="SellerInfo"),
                V(1, id="Logo"),
            ],
        ),
        H(0.5, id="Header"),
        H(0.8, id="SellerInfo"),
        H(0.7, id="InvoiceInfo"),
        H(2, id="Table"),
        H(0.5, id="Terms"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = Mistras()
    page.generate(1000, 800)
    page.show(save_path="layout_images/Mistras.png", texts="id")
    

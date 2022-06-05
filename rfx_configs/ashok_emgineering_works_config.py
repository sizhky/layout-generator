import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def AshokEmgineeringWorks():
    page = construct_page(
        H(
            1,
            [
                V(1, id="Logo"),
                V(3, id="SellerInfo"),
                V(1),
            ],
        ),
        H(
            1.3,
            [
                V(1, id="BuyerInfo"),
                V(
                    1,
                    [
                        H(0.5, id="TaxInfo"),
                        H(1.2, id="DueDate"),
                    ],
                ),
            ],
        ),
        H(2.5, id="Table"),
        H(1.3, id="Notes"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = AshokEmgineeringWorks()
    page.generate(1000, 800)
    page.show(save_path="layout_images/AshokEmgineeringWorks.png", texts="id")
    

import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def CommercialProposal():
    page = construct_page(
        H(
            1,
            [
                V(2, id="Date"),
                V(2, id="Header"),
            ],
        ),
        H(
            1,
            [
                V(2, id="SellerInfo"),
                V(2),
            ],
        ),
        H(2, id="BuyerInfo"),
        H(1),
        H(1, id="Table"),
        H(1, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = CommercialProposal()
    page.generate(1000, 800)
    page.show(save_path="layout_images/CommercialProposal.png", texts="id")
    

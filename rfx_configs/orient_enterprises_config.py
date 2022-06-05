import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def OrientEnterprises():
    page = construct_page(
        H(
            3,
            [
                V(
                    1,
                    [
                        H(1, id="SellerInfo"),
                        H(
                            2,
                            [
                                V(1, id="BuyerInfo"),
                                V(1, id="ShipInfo"),
                            ],
                        ),
                    ],
                ),
                V(
                    1,
                    [
                        H(0.5, id="Header"),
                        H(0.5, id="OrderNo"),
                        H(
                            2,
                            [
                                V(
                                    1,
                                    [
                                        H(1, id="BuyerContact"),
                                        H(1, id="PaymentType"),
                                    ],
                                ),
                                V(
                                    1,
                                    [
                                        H(1, id="BuyerPOC1"),
                                        H(1, id="BuyerPOC2"),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
        H(2.5, id="Table"),
        H(1.5, id="Terms"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = OrientEnterprises()
    page.generate(1000, 800)
    page.show(save_path="layout_images/OrientEnterprises.png", texts="id")
    

import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def SunshineTechnologies():
    page = construct_page(
        H(
            1,
            [
                V(1, id="Logo"),
                V(1, id="SellerAddress"),
            ],
        ),
        H(
            7,
            [
                V(
                    1,
                    [
                        H(0.5, id="Date"),
                        H(0.7, id="BuyerName"),
                        H(1.3, id="Items"),
                        H(2, id="Terms"),
                        H(0.5, id="Sign"),
                    ],
                ),
                V(1),
            ],
        ),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = SunshineTechnologies()
    page.generate(1000, 800)
    page.show(save_path="layout_images/SunshineTechnologies.png", texts="id")
    

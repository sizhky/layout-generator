import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def DabirIndustries():
    page = construct_page(
        H(1, id="SellerInfo"),
        H(
            1,
            [
                V(1, id="SellerInfo"),
                V(1, id="Date"),
            ],
        ),
        H(1, id="Notes"),
        H(3, id="Table"),
        H(3, id="Terms"),
        H(1, id="Sign"),
    )
    return page




if __name__ == "__main__":
    page = DabirIndustries()
    page.generate(1000, 800)
    page.show(save_path="layout_images/DabirIndustries.png", texts="id")
    

import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def Lakhmichand():
    page = construct_page(
        H(1, id="SellerInfo"),
        H(
            1,
            [
                V(5, id="BuyerInfo"),
                V(5, id="Date"),
            ],
        ),
        H(1, id="Notes"),
        H(1.2, id="ServiceInfo"),
        H(1, id="Table"),
        H(1.8, id="Terms"),
        H(0.5, id="Sign"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = Lakhmichand()
    page.generate(1000, 800)
    page.show(save_path="layout_images/Lakhmichand.png", texts="id")
    

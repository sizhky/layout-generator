import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def DiatechElectricals():
    page = construct_page(
        H(
            1,
            [
                V(8),
                V(2, id="SellerName"),
            ],
        ),
        H(2.7, id="Table"),
        H(1.2, id="Sign"),
        H(3.7, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = DiatechElectricals()
    page.generate(1000, 800)
    page.show(save_path="layout_images/DiatechElectricals.png", texts="id")
    

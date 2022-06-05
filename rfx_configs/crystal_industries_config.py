import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def CrystalIndustries():
    page = construct_page(
        H(
            1,
            [
                V(8),
                V(2, id="Logo"),
            ],
        ),
        H(0.5, id="Header"),
        H(6.5, id="Table"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = CrystalIndustries()
    page.generate(1000, 800)
    page.show(save_path="layout_images/CrystalIndustries.png", texts="id")
    

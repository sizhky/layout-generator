import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def FCGPowerIndustries():
    page = construct_page(
        H(
            1,
            [
                V(1, id="Logo"),
                V(2),
                V(1, id="Date"),
            ],
        ),
        H(3, id="Table"),
        H(0.5, id="Total"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = FCGPowerIndustries()
    page.generate(1000, 800)
    page.show(save_path="layout_images/FCGPowerIndustries.png", texts="id")
    

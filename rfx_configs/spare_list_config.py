import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def SpareList():
    page = construct_page(
        H(1, id="Table"),
        H(4, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = SpareList()
    page.generate(1000, 800)
    page.show(save_path="layout_images/SpareList.png", texts="id")
    

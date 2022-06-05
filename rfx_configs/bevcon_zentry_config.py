import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def BevconZentry():
    page = construct_page(
        H(1, id="InvoiceInfo"),
        H(8, id="Table"),
        H(0, id="padding"),
        H(1, id="Footer"),
    )
    return page




if __name__ == "__main__":
    page = BevconZentry()
    page.generate(1000, 800)
    page.show(save_path="layout_images/BevconZentry.png", texts="id")
    

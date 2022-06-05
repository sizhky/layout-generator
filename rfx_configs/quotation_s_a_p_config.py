import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def QuotationSAP():
    page = construct_page(
        H(1, id="Header"),
        H(4, id="Table"),
        H(2, id="Notes"),
        H(3, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = QuotationSAP()
    page.generate(1000, 800)
    page.show(save_path="layout_images/QuotationSAP.png", texts="id")
    

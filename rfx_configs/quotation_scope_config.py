import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def QuotationScope():
    page = construct_page(
        H(0.3, id="Header"),
        H(0.3, id="Date"),
        H(1, id="BuyerInfo"),
        H(1.3, id="Table"),
        H(2.5, id="Terms"),
        H(0.6, id="Sign"),
    )
    return page




if __name__ == "__main__":
    page = QuotationScope()
    page.generate(1000, 800)
    page.show(save_path="layout_images/QuotationScope.png", texts="id")
    

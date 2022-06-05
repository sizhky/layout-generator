import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def QuotationSiemens():
    page = construct_page(
        H(
            1,
            [
                V(1),
                V(1, id="Orderno"),
                V(1, id="DueDate"),
            ],
        ),
        H(2.5, id="Table"),
        H(0.5, id="Amount"),
        H(2.5, id="Tax"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = QuotationSiemens()
    page.generate(1000, 800)
    page.show(save_path="layout_images/QuotationSiemens.png", texts="id")
    

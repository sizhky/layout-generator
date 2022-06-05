import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def QualityToolsBearing():
    page = construct_page(
        H(1, id="SellerInfo"),
        H(0.3, id="Header"),
        H(
            1.5,
            [
                V(1, id="BuyerInfo"),
                V(1, id="PaymentType"),
            ],
        ),
        H(0.3, id="BuyerName"),
        H(2, id="Table"),
        H(0, id="padding"),
        H(2.5, id="Footer"),
    )
    return page




if __name__ == "__main__":
    page = QualityToolsBearing()
    page.generate(1000, 800)
    page.show(save_path="layout_images/QualityToolsBearing.png", texts="id")
    

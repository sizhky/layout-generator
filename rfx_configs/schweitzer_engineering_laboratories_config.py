import sys
sys.path.append("/Users/yeshwanth.y/code/layout-generator")
from src.page import construct_page, H, V


def SchweitzerEngineeringLaboratories():
    page = construct_page(
        H(1, id="SellerInfo"),
        H(
            1.3,
            [
                V(1, id="BuyerName"),
                V(1, id="DueDate"),
            ],
        ),
        H(1.3, id="Table"),
        H(3.4, id="Notes"),
        H(0, id="padding"),
    )
    return page




if __name__ == "__main__":
    page = SchweitzerEngineeringLaboratories()
    page.generate(1000, 800)
    page.show(save_path="layout_images/SchweitzerEngineeringLaboratories.png", texts="id")
    

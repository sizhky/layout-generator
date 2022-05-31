from page import *

def config1():
	url = "https://i.pinimg.com/originals/4b/fe/f0/4bfef0682fc434a8f6462e388441f54d.png"
	page = construct_page(
        H(1, id="SellerName"),
        H(1,[V(1,id="SellerAddress"),V(1,id="Date")]),
        H(1,[V(1,id="SellerContact"),V(1,id="InvoiceNumber")]),
        H(1,id="BuyerName"),
        H(3,id="BuyerAddress"),
        H(1,id="BuyerContact"),
        H(10,id="Table"),
        H(3,[V(7),V(3,[H(1,id="Subtotal"),
                H(1,id="Tax"),
                H(1,id="Total")])]),
        H(4,id="Footer"),

    )
	return page

def config2():
	url = "https://www.deskera.com/blog/content/images/2020/12/Proforma_Invoice.png"
	page = construct_page(
    H(4,[
            V(7,
                [
                    H(2,id="Logo"),
                    H(2,id="Header")
                ]),
            V(3,
            [
                H(2,id = "SellerName"),
                H(1.5,id="SellerAddress")
            ])
        ]),
    H(4,[
        V(2,[
            H(1,id="BuyerName"),
            H(1,id="BuyerAddress")
        ]),
        V(2,[
            H(1,id="ShipName"),
            H(1,id="ShipAddress")
        ]),
        V(2,[
            H(1,id="InvoiceNumber"),
            H(1,id="Date")
        ]),
    ]),
    H(4,id="Table"),
    H(3,[
        V(7),
        V(3,[
            H(1,id="Subtotal"),
            H(1,id="Discount"),
            H(1,id="Tax"),
        ])
    ]),
    H(2,[
        V(7,id="Comments"),
        V(3,id="Total")
    ]),
    H(1,id="Footer"),
    )
	return page

def config3():
	url = "https://resources.tallysolutions.com/wp-content/uploads/2021/02/tax-invoice.jpg"
	page = construct_page(
    H(1,id="Header"),
    H(8,[
        V(5,[
            H(1,id="SellerName"),
            H(2,id="SellerAddress"),
            H(2,id="SellerContact"),
            H(1,id="BuyerName"),
            H(2,id="BuyerAddress"),
        ]),
        V(2.5,[
            H(1,id="InvoiceNumber"),
            H(1,id="RefNumber"),
            H(1,id="OrderNo")
        ]),
        V(2.5,[
            H(1,id="Date"),
            H(1,id="PaymentType"),
            H(1,id="VehicleNo")
        ])
    ]),
    H(4,id="Table"),
    H(1,[
        V(8),
        V(2,id="Total")
    ]),
    H(2,[
        V(4),
        V(2,id="CentralTax"),
        V(2,id="StateTax"),
        V(2,id="Tax")
    ]),
    H(1,id="Footer"),
    )

	return page

def config4():
	url = "https://www.invoiceberry.com/img/homepage/free_invoice_templates/new/formats/google_docs_sheets_invoice_template.png"
	page = construct_page(
    H(2,[
        V(6,id="Header"),
        V(4,id="Logo")
    ]),
    H(3,[
        V(4,[
            H(1,id="SellerName"),
            H(2,id="SellerAddress")
        ]),
        V(4,[
             H(1,id="BuyerName"),
             H(2,id="BuyerAddress")
        ]),
        V(2,[
             H(1,id="InvoiceNumber"),
             H(1,id="Date"),
             H(1,id="DueDate")
        ])
    ]),
    H(3,id="Table"),
    H(5,[
        V(7),
        V(3,[
             H(1,id="Subtotal"),
             H(1,id="Discount"),
             H(1,id="TaxRate"),
             H(1,id="Tax"),
             H(1,id="Total"),
             H(1,id="Balance")
        ])
    ]),
    H(1,id="Comments"),
    H(1,id="Footer"),
    )
    
	return page

def config5():
	url= "https://msofficegeek.com/wp-content/uploads/2021/12/GST-Invoice-Template-For-Retailers.png"
	page = construct_page(
    H(3,[
        V(2,id="Logo"),
        V(8,[
            H(1.5,id="SellerName"),
            H(1.5,id="SellerAddress")
        ])
    ]),
    H(1,[
        V(5,id="GSTIN"),
        V(5,id="Location")
    ]),
    H(0.5,id="Header"),
    H(1,[
        V(5,id="InvoiceNumber"),
        V(5,id="Date")
    ]),
    H(3,[
        V(5,[
            H(1,id="BuyerID"),
            H(1,id="BuyerName"),
            H(1,id="BuyerAddress")
        ]),
        V(5,[
            H(1,id="PaymentType"),
            H(1),
            H(1,id="DueDate")
        ]),
    ]),
    H(4,id="Table"),
    H(1,[
        V(5),
        V(2,id="Tax"),
        V(2,"Total")
    ]),
    H(3,[
        V(5,id="Comments"),
        V(5,[
            H(1,id="Tax"),
            H(1,id="Total")
        ])
    ]),
    H(1,[
        V(5,id="SellerSign"),
        V(5,id="BuyerSign")
    
    ]),
    H(1,id="Footer"),
    )

	return page

def config6():
	url = "https://www.invoicesimple.com/wp-content/uploads/2019/08/Screen-Shot-2019-08-30-at-11.35.16-AM.png"
	page = construct_page(
    H(3,[
        V(2,id="Logo"),
        V(4,[
            H(1,id="SellerName"),
            H(1,id="SellerAddress"),
            H(1,id="SellerContact")
        ]),
        V(4,[
            H(1,id="Date"),
            H(1,id="DueDate"),
            H(1,id="BuyerID")
        ])
    ]),
    H(3,[
        V(5,[
            H(1,id="BuyerName"),
            H(1,id="BuyerAddress"),
            H(1,id="BuyerContact")
        ]),
        V(5,[
            H(1,id="ShipName"),
            H(1,id="ShipAddress"),
            H(1,id="ShipContact")
        ])
    ]),
    H(3,id="ShipInfo"),
    H(3,id="Table"),

    H(4,[
        V(6,id="Comments"),
        V(4,[
            H(1,id="Subtotal"),
            H(1,id="Discount"),
            H(1,id="TaxRate"),
            H(1,id="Total")
        ])
    ]),
    H(1,id="BuyerSign"),
    )

	return page

def config7():
	url = "https://gogstbill.com/wp-content/uploads/2020/03/Template2-1.jpg"
	page = construct_page(
    H(4,[
        V(8,[
            H(2,id="SellerName"),
            H(2,[
                V(5,id="SellerAddress"),
                V(5,id="SellerContact")
            ]),
        ]),
        V(2,id="Logo")
    ]),
    H(1,id="Header"),
    H(3,[
        V(4,[
            H(1,id="BuyerName"),
            H(1,id="BuyerAddress"),
            H(1,id="BuyerContact")
        ]),
        V(3,[
            H(1,id="InvoiceNumber"),
            H(1,id="OrderNo"),
            H(1,id="DeliveryDate")
        ]),
        V(3,[
            H(1,id="Date"),
            H(1,id="InvoiceDate"),
            H(1,id="DueDate")
        ])
    ]),
    H(3,id="Table"),
    H(1, [
        V(4),
        V(2, id="TaxRate"),
        V(2, id="Tax"),
        V(2, id="Total")
    ]),
    H(3, [
            V(6,[
                H(2,id="BankDetails"),
                H(1,id="Terms")
            ]),
            V(4, id="SellerSign")
        ]),
    )

	return page

def config8():
	url = "https://www.billingsoftware.in/images/articles/invis1.jpg"
	



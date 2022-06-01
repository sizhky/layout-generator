from sympy import re
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
	page = construct_page(
    H(1.5,[
        V(20,id="Logo"),
        V(60,id="Header"),
        V(25,id="InvoiceInfo")
    ]),
    H(2,[
        V(3,id="SellerInfo"),
        V(3,id="BuyerInfo"),
        V(4,id="DeliveryInfo")
    ]),
    H(3,id="Table"),
    H(2,[
        V(7,id="Sign"),
        V(3,id="AmountBreakup")
    ]),
    H(1,id="Footer")
    )
	return page

def config9():
	url = "https://www.freshbooks.com/wp-content/uploads/invoice-template-word-blue.jpeg"
	page = construct_page(
    H(1,id="Header"),
    H(1,[
        V(2,id="SellerAddress"),
        V(2,id="SellerContact"),
        V(6)
    ]),
    H(1.2,id="BuyerInfo"),
    H(3,[
        V(2,id="InvoiceInfo"),
        V(8,id="Table")
    ]),
    H(2.5,[
        V(7.5),
        V(2.5,id="AmountBreakup")
    ]),
    H(0.5,id="Footer")
    )
	return page

def config10():
	url = "https://www.smartsheet.com/sites/default/files/2021-11/IC-Free-Printable-Construction-Invoice-Template.png"
	page = construct_page(
    H(1,id="Header"),
    H(9,[
        V(5,[
            H(1.2,id="SellerInfo"),
            H(1.2,id="BuyerInfo"),
            H(7,id="Table"),
            H(.6,id="Sign")
        ]),
        V(5,[
            H(1.2,id="InvoiceInfo"),
            H(1.2,id="PaymentMode"),
            H(1,id="Desc"),
            H(6,id="Table2"),
            H(2,id="AmountBreakup")
        ])
    ])
    )
	return page

def config11():
	url = "https://dwdqz3611m4qq.cloudfront.net/templates/Auto-Repair-Invoice-Template2-G.jpg"
	page = construct_page(
    H(2,[
        V(6,id="Logo"),
        V(4,id="SellerInfo")
    ]),
    H(1.5,[
        V(2,id="BuyerInfo"),
        V(5),
        V(2,id="InvoiceInfo")
    ]),
    H(3,id="Table"),
    H(2,[
        V(6,id="Notes"),
        V(4,id="Total")
    ]),
    H(2,id="Footer")
    )
	return page

def config12():
	url = "https://i.pinimg.com/originals/dc/2a/e8/dc2ae841f309fc2f287a3a87c0ca5161.gif"
	page = construct_page(
    H(2,id="SellerInfo"),
    H(1,id="InvoiceInfo"),
    H(3,id="Table"),
    H(1.5,[
        V(8,id="WordAmount"),
        V(2,id="Total")
    ])
    )
	return page

def config13():
	## Equal Problem
	url = "https://www.smartsheet.com/sites/default/files/blank-invoice-template.png"
	page = construct_page(
    H(1,[
        V(5,id="Logo"),
        V(5,id="Header")
    ]),
    H(1.5,[
        V(5,id="SellerInfo"),
        V(5,id="InvoiceInfo")
    ]),
    H(2,[
        V(5,id="BuyerInfo"),
        V(5,id="ShipInfo")
    ]),
    H(4,id="Table"),
    H(2,[
        V(5,id="Comments"),
        V(5,id="AmountBreakup")
    ])
    )
	return page

def config14():
	url = "https://apollo-singapore.akamaized.net/v1/files/55c854odhsf4-IN/image"
	page = construct_page(
    H(1,id="Header"),
    H(6,[
        V(1,[
            H(3,id="SellerInfo"),
            H(2,id="OrderNo"),
        ]),
        V(1,[
            H(2,id="BuyerInfo"),
            H(2,id="ShipInfo"),
            H(2,id="InvoiceInfo"),
        ]),
    ]),
    H(1,id="Table"),
    H(.3,id="WordAmount"),
    H(.5,id="Sign"),
    H(1.2,id="PaymentInfo"),
    )
	return page

def config15():
	url = "https://assets1.cleartax-cdn.com/s/img/20170906124223/TAX_INVOICE_IN00012_ClearTax-11-1024x1012.jpg"
	page = construct_page(
    H(1,[
        V(1,id="Logo"),
        V(4,id="SellerInfo"),
        V(2,id="InvoiceInfo"),
    ]),
    
    H(1,[
        V(1,id="BuyerName"),
        V(1,id="BuyerAddress"),
        V(1,id="ShipAddress"),
    ]),
    H(0.5,id="DeliveryInfo"),
    H(2,id="Table"),
    H(1.5,[
        V(6),
        V(2,id="AmountBreakup"),
    ]),
    H(1,id="Sign"),
    H(1,id="Footer")
    )
	return page

def config16():
	url="https://media.amazonwebservices.com/blog/aws_acct_invoice_jeff_barr_1.png"
	page = construct_page(
    H(1,id="Logo"),
    H(1),
    H(1,id="InvoiceInfo"),
    H(1.2,[
        V(1,id="BuyerInfo"),
        V(1,id="SellerInfo"),
    ]),
    H(2.5,id="Table"),
    H(3.3,id="Notes")
    )
	return page

def config17():
	url = "https://imgv2-1-f.scribdassets.com/img/document/167862026/original/9dcc6c3f6a/1652917816?v=1"
	page = construct_page(
    H(1,[
        V(2,id="Logo"),
        V(8,id="SellerInfo"),
    ]),
    H(2,[
        V(3,id="OrderInfo"),
        V(3,id="BuyerInfo"),
        V(3,id="ShipInfo"),
        V(1),
    ]),
    H(2,id="Table"),
    H(1,[
        V(6),
        V(4,id="Total")
    ]),
    H(6,id="Blank"),
    )
	return page

def config18():
	url = "https://cdn.spreadsheet123.com/images/ExcelTemplates/vehicle-repair-invoice_lg.png"
	page = construct_page(
    H(1,[
        V(6,id="SellerName"),
        V(4,id="Header"),
    ]),
    H(1,id="Date"),
    H(2.5,id="BuyerInfo"),
    H(2.5,id="Table"),
    H(2.5,id="Table2"),
    H(2,[
        V(7,id="Comments"),
        V(7,id="AmountBreakup"),
    ]),
    H(1,id="Footer")
    )
	return page

def config19():
	url = "https://www.invoicesimple.com/wp-content/uploads/2018/06/Invoice-Template-freelance.png"
	page = construct_page(
    H(1,[
        V(8,id="Header"),
        V(2,id="Logo"),
    ]),
    H(1,[
        V(6,id="SellerInfo"),
        V(4,id="InvoiceInfo"),
    ]),
    H(0.9,[
        V(8,id="BuyerInfo"),
        V(2,id="ProductInfo"),
    ]),
    H(2,id="Table"),
    H(1,[
        V(7),
        V(3,id="AmountBreakup"),
    ]),
    H(0.5,id="Footer")
    )
	return page

def config20():
	## Equal Problem
	url = "https://www.geneevarojr.com/wp-content/uploads/2020/10/T-Shirt-Work-Order-Template-1187x1536.jpg"
	page = construct_page(
    H(1,id="Header"),
    H(3,[
        V(5,id="SellerInfo"),
        V(5,id="BuyerInfo"),
    ]),
    H(2,[
        V(5,id="PaymentInfo"),
        V(5,id="Schedule"),
    ]),
    H(1.5,id="Table"),
    H(1.5,id="Table2"),
    H(2,[
        V(7,id="Sign"),
        V(3,id="AmountBreakup"),
    ]),
    )
	return page

def config21():
	url="https://www.geneevarojr.com/wp-content/uploads/2020/10/Staffing-Agency-Invoice-Template-1187x1536.jpg.webp"
	page = construct_page(
    H(0.5,id="Header"),
    H(2,[
        V(5,id="SellerInfo"),
        V(5,id="Logo"),
    ]),
    H(0.5,id="InvoiceInfo"),
    H(2,id="BuyerInfo"),
    H(4,id="Table"),
    H(1.5,id="Footer")
    )
	return page

def config22():
	url = "https://www.geneevarojr.com/wp-content/uploads/2020/10/Retail-Store-Receipt-Template-1068x1382.jpg"
	page = construct_page(
    H(1,id="Header"),
    H(2,[
        V(7,id="SellerInfo"),
        V(3,id="Logo"),
    ]),
    H(1,id="InvoiceInfo"),
    H(2,id="BuyerInfo"),
    H(4,id="Table"),
    H(1.5,id="Footer")
    )
	return page

def config23():
	url = "https://www.geneevarojr.com/wp-content/uploads/2020/10/Accounting-Invoice-Template.jpg"
	page = construct_page(
    H(1,id="Header"),
    H(1,[
        V(1,id="Logo"),
        V(1,id="InvoiceInfo"),
    ]),
    H(2.5,[
        V(1,id="SellerInfo"),
        V(1,id="BuyerInfo"),
    ]),
    H(3.5,id="Table"),
    H(1,[
        V(7,id="Notes"),
        V(3,id="AmountBreakup"),
    ]),
    H(1.5,id="Footer")
    )
	return page

def config24():
	## Equal Problem
	url = "https://www.geneevarojr.com/wp-content/uploads/2020/10/Sales-Invoice-Template.jpg"
	page = construct_page(
    H(1,[
        V(1,id="SellerName"),
        V(1,id="Header")
    ]),
    H(2,[
        V(1,id="SellerInfo"),
        V(1,id="InvoiceInfo"),
    ]),
    H(2,[
        V(1,id="BuyerInfo"),
        V(1,id="ShipInfo"),
    ]),
    H(3.5,id="Table"),
    H(1.5,[
        V(7,id="Notes"),
        V(3,id="AmountBreakup"),
    ]),
    )
	return page

def config25():
	url = ""
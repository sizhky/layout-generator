from sympy import re
from tenacity import retry_unless_exception_type
from page import *

'''

BuyerInfo {
	BuyerName
	BuyerAddress
	BuyerContact
}
SellerInfo {
	SellerName
	SellerAddress
	SellerContact
}
ShipInfo {
	ShipName
	ShipAddress
	ShipContact
}
AmountBreakup{
	Subtotal
	Discount (If any)
	TaxRate
	Tax
	Total
}

Header{
	for blank in ["Sales","Retail","Accounting",etc]
		"{} Invoice".format(blank)
}

ServiceInfo{
	"Meter number"
	"Meter readings and stuff
}

ServiceHistory{
	"Previous meter readings"
}

Notes = "Something Formal"-> Terms Conditions
Comments = "Informal" ->Greetings 

DueDate{
	can include 
	due date
	bill date
	invoice date
}

Date

Balance



'''



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
		V(1,id="BuyerInfo"),
		V(1,id="ProductInfo"),
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

#Starts here
def config25():
	url = "https://pbs.twimg.com/media/EhIm5RKUcAAOYU6.jpg"
	page = construct_page(
	H(1,[
		V(1,id="SellerName"),
		V(1.5),
		V(1,id="DueDate"),
	]),
	H(3,[
		V(4,[
			H(1,id="BuyerInfo"),
			H(2,id="BuyerContact"),
		]),
		V(6,[
			H(3,id="ServiceInfo"),
		]),
	]),
	H(3,id="Table"),
	H(2,id="AmountBreakup"),
	H(2,id="Footer"),
	)
	return page

def config26():
	url = "https://www.trustwave.com/images/slblog-03-02-2018-10-57-10/spiderlabs/168fe9ef-275b-4257-8fa9-46046d7402b0.png"
	page = construct_page(
	V(6,[
		H(1),
		H(1,id="Header"),
		H(1,id="BuyerName"),
		H(1,id="BuyerInfo"),
		H(2,id="Table"),
	]),
	
	V(4,[
		H(1,id="Logo"),
		H(1,id="SellerContact"),
		H(1),
		H(2,id="Total"),
		H(1),
	]),

	)
	return page

def config27():
	url = "https://newenglandcleanenergy.com/energymiser/wp-content/uploads/sites/2/2021/05/3-1-e1620745320756.png"
	page = construct_page(
	H(1,[
		V(4,[
			H(1,id="SellerName"),
			H(1,id="ServiceInfo"),
			H(0.8,id="ServiceHistory"),
			H(1,id="SellerContact"),
			H(1),
		]),
		
		V(6,[
			H(0.5,id="Total"),
			H(1.5,id="AmountBreakup"),
			H(2.8,id="Table"),
		]),
	]),
	H(0.2,id="Footer")
	)
	return page

def config28():
	url = "https://assets-us-01.kc-usercontent.com/7dd6b71d-d672-0004-6a4d-7043e1d0db33/dbb21025-abd5-48a2-bb00-44d5676d60c4/ElecBillSample2_Updated.PNG"
	page = construct_page(
	H(0.07,id="Logo"),
	H(1,[
		V(55,[
			H(0.8,id="BuyerInfo"),
			H(1,id="Comments"),
			H(1,id="ServiceHistory"),
			H(3,id="Table")
		]),        
		V(45,[
			H(0.8,id="ServiceInfo"),
			H(2,id="Total"),
			H(2,id="ServiceBreakup"),
			H(2,id="Notes"),
		]),
	]),
	)
	return page

def config29():
	url = "https://pud-ri.org/wp-content/uploads/2020/07/Sample-electric-Bill.jpg"
	page = construct_page(
	H(3,[
		V(1,[
			H(1,id="SellerInfo"),
			H(1,id="SellerContact"),
			H(1,id="BuyerInfo"),
		]),
		V(1, [
			H(1, id="Date"),
			H(1.2, id="ServiceInfo"),
			H(0.8),
		]),
	]),
	H(0.5,id="ServiceHistory"),
	H(1.5,[
		V(1,id="Graph"),
		V(1,id="Table")
	]),
	H(1,[
		V(1,id="Notes"),
		V(1,id="Total")
	]),
	H(1,[
		V(1,id="PaymentType"),
		V(1,id="SellerContact")
	]),
	)
	return page

def config30():
	url = "https://imgv2-1-f.scribdassets.com/img/document/452770181/original/dcf479821d/1648342467?v=1"
	page = construct_page(
	H(1,[
		V(1,id = "Date"),
		V(1,id = "AccountInfo"),
		V(1,id = "InvoiceInfo"),
		V(1,id = "SellerName"),
	]),
	H(3,id="BuyerInfo"),
	H(1.5,[
		V(1,id="Comments"),
		V(1,id="DueDate")
	]),
	H(1.5,id="Table"),
	H(2.5,id="Footer"),
	)
	return page

def config31():
	url = "https://okcoop.org/wp-content/uploads/2021/02/Bill-Sample-scaled.jpg"
	page = construct_page(
	H(1,[
		V(1,id = "SellerName"),
		V(1,id = "DueDate"),
	]),
	H(1.2,[
		V(1,id = "BuyerInfo"),
		V(1,id = "OutstandingBill"),
	]),
	H(0.5,id="ServiceHistory"),
	H(2.5,[
		V(1,[
			H(1.5,id="Graph"),
			H(1,id="Notes"),
		]),
		V(1,id = "AmountBreakup"),
	]),
	
	H(1.5,[
		V(1,id="BuyerContact"),
		V(1,id="Total")
	]),
	H(.5,id="Footer"),
	)
	return page

def config32():
	url = "https://www.cdn.fortisbc.com/libraries/images/default-source/accounts-and-billing/21-215-2_electric-bill-sample-2022.jpg?sfvrsn=fe3a7a4f_2"
	page = construct_page(
	H(1,[
		V(8,id = "SellerName"),
		V(2,id = "SellerContact"),
	]),
	H(4,[
		V(6,id="Table"),
		V(4,id = "AccountInfo"),
	]),
	H(1),
	H(4,[
		V(6,id="SellerInfo"),
		V(4,id = "Total"),
	]),
	)
	return page

def config33():
	url = "https://imgv2-1-f.scribdassets.com/img/document/403563346/original/84bf54ac4a/1649219969?v=1"
	page = construct_page(
	H(1.5,[
		V(1,id = "Logo"),
		V(1,id = "SellerInfo"),
		V(1),
		V(1,id = "OrderNo"),
	]),
	H(1,[
		V(1,id = "BuyerInfo"),
		V(1,id = "ShipInfo"),
		V(1),
	]),
	H(2,id="Table"),
	H(1,[
		V(6,id="Notes"),
		V(4,id = "Sign"),
	]),
	)
	return page

def config34():
	url = "https://imgv2-1-f.scribdassets.com/img/document/411174817/original/85fde6c5de/1652775741?v=1"
	page = construct_page(
	H(1,id="SellerName"),
	H(3,[
		V(1,id = "BuyerName"),
		V(1,id = "Date"),
	]),
	H(3,[
		V(1,id = "Account"),
		V(1,id = "Total"),
	]),
	H(1),
	H(2,id="ServiceInfo"),
	H(1,id="Sign"),
	H(1,id="InvoiceInfo"),
	)
	return page

def config35():
	url = "https://www.tescomobile.ie/img/understanding-your-bill/Customer-Bill-redesign-2021-Page-2.jpg"
	page = construct_page(
	H(2,[
		V(1,id = "SellerName"),
		V(1,id = "Date"),
	]),
	H(1,id="Amount"),
	H(3,[
		V(7,id = "ServiceInfo"),
		V(3,id = "ServiceBreakup"),
	]),
	H(1),
	H(0.5,id="Tax"),
	H(0.5,id="Balance"),
	H(0.5,id="Table"),
	H(3,id="Footer"),
	)
	return page

def config36():
	url = "https://imgur.com/sn6ODZ7"
	page = construct_page(
		H(2,id="SellerInfo"),
		H(1,id="BuyerInfo"),
		H(1,id="InvoiceInfo"),
		H(4,id="Table"),
		H(1,id="PaymentType"),
	)
	return page

def config37():
	url = "https://www.tescomobile.ie/img/understanding-your-bill/Customer-Bill-redesign-2021-Page-4.jpg"
	page = construct_page(
		H(1,[
			V(7,id="Logo"),
			V(3,id="Date")
		]),
		H(1,id="Table"),
		H(1,id="Table2"),
		H(1,id="Table3"),
		H(1,id="Table4"),
		H(1,id="Table5"),
		H(1,id="Table6"),
	)
	return page

def config38():
	url = "https://community.three.ie/t5/image/serverpage/image-id/4698iA1457951E80F792F?v=v2"
	page = construct_page(
		H(2,[
			V(1,id="DueDate"),
			V(1.5,id="Account"),
			V(1,id="Date"),
			V(1,id="Logo")
		]),
		H(3,id="Table"),
		H(6,id="AmountBreakup"),
		H(1.5,id="ServiceInfo"),
	)
	return page

def config39():
	url = "https://www.att.com/Common/images/Consumer_Wireless_standalone_062112_1.jpg"
	page = construct_page(
	H(1,[
		V(1,id="Logo"),
		V(1.5,id="SellerInfo"),
		V(1.5,id="Date"),
	]),
	H(5,[
		V(1,[
			H(2,id="Amount"),
			H(3,id="ServiceInfo"),
		]),
		V(1,[
			H(1.8,id="Notes"),
			H(1.4,id="Table"),
			H(1.8,id="ServiceHistory"),
		]),
	]),
	H(1,id="BuyerInfo"),
	)
	return page

def config40():
	url = "https://techbiote.com/wp-content/uploads/2021/05/vi-postpaid-downloaded-pdf-bill-1.jpg"
	page = construct_page(
	H(3,[
		V(65,[
			H(1,id="SellerInfo"),
			H(1.7,id="Account"),
		]),
		V(35,[
			H(1,id="Total"),
			H(1.7,id="DueDate"),
		]),
	]),
	H(1.3,id="AmountBreakup"),
	H(5,[
		V(1,id="ServiceInfo"),
		V(1,id = "Notes"),
	]),
	H(1,id="Footer"),
	)
	return page

def config41():
	url = "https://www.pdffiller.com/preview/100/293/100293271/large.png"
	page = construct_page(
	H(1,[
		V(2,id="Logo"),
		V(2,id="Header"),
	]),
	H(2,id="Notes"),
	H(1,id="BuyerInfo"),
	H(2,id="ServiceInfo"),
	H(1.5,id="Total"),
	H(0.5,id="Comments"),
	)
	return page

def config42():
	url = "https://imgv2-2-f.scribdassets.com/img/document/388234801/original/3c6dbc97ca/1612813254?v\u003d1"
	page = construct_page(
	H(1,id="Header"),
	H(1,id="BuyerName"),
	H(2,id="ServiceInfo"),
	H(2,id="InvoiceInfo"),
	H(3,[
		V(2,id="AmountBreakup"),
		V(2,id="PaymentType"),
	]),
	H(0.8,id="Notes"),
	)
	return page

def config43():
	url = "https://www.lenovo.com/content/dam/lenovo/pcsd/north-america/en/products/thinksystem/asset-server-x-new-invoice-example.pdf"
	page = construct_page(
	H(1,id="Header"),
	H(3,[
		V(2,[
			H(1.2,id="ShipInfo"),
			H(0.9,id="BuyerInfo"),
			H(0.9,id="Orderno"),
		]),
		V(2,[
			H(0.9,id="InvoiceInfo"),
			H(0.9,id="Account"),
			H(1.2,id="SellerInfo"),
		]),
	]),
	H(4,id="Table"),
	H(0.5,id="Notes"),
	H(2,id="Footer"),
	)
	return page

def config44():
	url = "https://getbillsmart.com/wp-content/uploads/2020/05/att-bill.jpg"
	page = construct_page(
	H(2,[
		V(2,id="BuyerInfo"),
		V(4,id="BuyerInfo"),
		V(4,id="Date"),
	]),
	H(8,[
		V(6,[
			H(3,id="Table"),
			H(2.5,id="ServiceInfo"),
			H(0.5,id="Amount"),
		]),
		V(4,id="Amount2"),
	]),
	)
	return page

def config45():
	url = "https://imgv2-1-f.scribdassets.com/img/document/147310337/original/284c9d0d73/1651747591?v=1"
	page = construct_page(
	H(1, [
		V(2, id="Logo"),
		V(4, id="SellerInfo"),
		V(3),
	]),
	H(1, [
		V(2, id="BuyerInfo"),
		V(2, id="ShipInfo"),
	]),
	H(0.7,id="PaymentType"),
	H(1.2,id="OrderNo"),
	H(0.8,id="Notes"),
	H(3.3,id="Table"),

	)
	return page

def config46():
	url = "https://www.pdffiller.com/preview/400/415/400415440/large.png"
	page = construct_page(
	H(1, [
		V(1, id="Logo"),
		V(1, id="Header"),
		V(1, id="SellerInfo"),
	]),
	H(1.5, [
		V(1, id="BuyerInfo"),
		V(2, id="DueDate"),
	]),
	H(0.7,id="ServiceHistory"),
	H(2.5, [
		V(1, id="Table"),
		V(2, id="Notes"),
	]),
	H(1.8,id="PaymentType"),
	)
	return page

def config47():
	url = "https://imgv2-1-f.scribdassets.com/img/document/205064886/original/ea912bb2b5/1652291172?v=1"
	page = construct_page(
	H(1,id="SellerInfo"),
	H(1.5, [
		V(1, id="BuyerInfo"),
		V(1, id="InvoiceInfo"),
	]),
	H(1.5,id="Table"),
	H(0.3,id="Amount"),
	H(1.5,id="Notes"),
	)
	return page

def config48():
	url = "https://imgv2-2-f.scribdassets.com/img/document/38736169/original/5132172a76/1652168776?v=1"
	page = construct_page(
	H(1,id="SellerInfo"),
	H(0.7, [
		V(1, id="SellerName"),
		V(1, id="OrderNo"),
	]),
	H(1.5, [
		V(1, id="BuyerInfo"),
		V(1, id="InvoiceInfo"),
	]),
	H(4.5,id="Table"),
	H(1.3,id="SellerInfo"),
	H(0.5,id="Notes"),

	)
	return page

def config49():
	url = "https://imgv2-1-f.scribdassets.com/img/document/53091924/original/b5635691d0/1650313678?v=1"
	page = construct_page(
	H(0.7, [
		V(1, id="SellerName"),
		V(1, id="Header"),
	]),
	H(1.5, [
		V(1, id="BuyerInfo"),
		V(1, id="InvoiceInfo"),
	]),
	H(1.3,id="ServiceHistory"),
	H(3.5, [
		V(1, id="Table"),
		V(1, id="Notes"),
	]),
	H(1),
	H(1.5,id="PaymentType"),
	)
	return page

def config50():
	url = "https://i.insider.com/5de58e87fd9db221e4201a64?width=1000&format=jpeg&auto=webp"
	page = construct_page(
	H(3),
	H(1.5,id="Total"),
	H(1,id="Subtotal"),
	H(3,id="AmountBreakup"),
	H(0.5,id="PaymentType"),
	
	)
	return page
	
def UNPPolyvales():
	page = construct_page(
	H(1,id="SellerName"),
	H(3,[
		V(1,[
			H(1.3,id="SellerInfo"),
			H(1.7,id="BuyerInfo"),
		]),
		V(1,[
			H(1.3,id="DueDate"),
			H(1.7,id="ShipInfo"),
		])
	]),
	H(4,id="Table"),
	H(1.5,id="AmountBreakup"),
	H(0.5,[
		V(6,id="Notes"),
		V(4,id="Sign"),

	])
	)
	return page

def BevconZentry():
	page = construct_page(
	H(1,id="InvoiceInfo"),
	H(8,id="Table"),
	H(1,id="Footer"),
	)
	return page

def Lakhmichand():
	page = construct_page(
	H(1,id="SellerInfo"),
	H(1,[
		V(5,id="BuyerInfo"),
		V(5,id="Date"),
	]),
	H(1,id="Notes"),
	H(1.2,id="ServiceInfo"),
	H(1,id="Table"),
	H(1.8,id="Terms"),
	H(0.5,id="Sign"),
	
	)
	return page

def RolonSeals():
	page = construct_page(
	H(1,id="SellerInfo"),
	H(1.8,[
		V(5,id="BuyerInfo"),
		V(5,id="InvoiceInfo"),
	]),
	H(0.2,id="Notes"),
	H(3.2,id="Table"),
	H(2.8,id="Terms"),

	)
	return page

def Refteck():
	page = construct_page(
	H(1,[
		V(5,id="SellerName"),
		V(5,id="SellerInfo"),
	]),
	H(1.8,[
		V(5,id="BuyerInfo"),
		V(5,id="Total"),
	]),
	H(1,id="Notes"),
	H(6,id="Table"),
	H(0.5,id="Footer"),
	)
	return page

def NationalAccreditationBoard():
	page = construct_page(
	H(1,id="SellerName"),
	H(1.5,[
		V(7,id="BuyerInfo"),
		V(5,id="Date"),
	]),
	H(3.5,id="Notes"),
	H(0.5,id="Sign"),

	)
	return page

def VashiElectricals():
	page = construct_page(
	H(1,[
		V(7,id="SellerInfo"),
		V(3,id="OrderNo"),
	]),
	H(0.8,[
		V(1,id="BuyerAddress"),
		V(1,id="BuyerContact"),
	]),
	H(1,[
		V(1,id="InvoiceInfo"),
		V(1,id="PaymentType"),
	]),
	H(0.5,id="Comments"),
	H(1.2,id="Table"),
	H(0.8,id="Notes"),
	H(1.2,id="Terms"),

	)
	return page
	
def Elomatic():
	page = construct_page(
	H(0.5,id="Header"),
	H(1,[
		V(3,id="BuyerInfo"),
		V(2,id="Header"),
		V(4),
	]),
	H(5,id="Table"),

	)
	return page

def Payper():
	page = construct_page(
	H(1,[
		V(1,id="SellerInfo"),
		V(1,id="Header"),
	]),
	H(1.2,[
		V(1,id="Date"),
		V(1,id="BuyerInfo"),
	]),
	H(4.3,id="Table"),
	H(0.5,id="Amount"),

	)
	return page

def Simpex():
	page = construct_page(
	H(3,[
		V(1,[
			H(2,id="Logo"),
			H(0.5,id="BuyerName"),
			H(1.5,id="BuyerInfo"),
		]),
		V(1,[
			H(2,id="InvoiceInfo"),
			H(0.5,id="BuyerContact"),
			H(1.5),
		]),
	]),
	H(1,id="Notes"),
	H(1.5,id="Table"),
	H(1.5,[
		V(1,id="PaymentType"),
		V(1,id="AmountBreakup"),
	]),
	H(.3,id="Footer"),

	)
	return page

def CrystalIndustries():
	page = construct_page(
	H(1,[
		V(8),
		V(2,id="Logo"),
	]),
	H(0.5,id="Header"),
	H(6.5,id="Table"),

	)
	return page

def AalidhraTextoolEngineers():
	page = construct_page(
	H(1,id="SellerInfo"),
	H(1,[
		V(2,id="BuyerName"),
		V(2,id="DueDate"),
	]),
	H(7.5,id="Table"),

	)
	return page

def Evergreen():
	page = construct_page(
	H(1,id="SellerName"),
	H(0.4,[
		V(2,id="Date"),
		V(2,id="DueDate"),
	]),
	H(1.6,[
		V(2,id="SellerInfo"),
		V(2,id="BuyerInfo"),
	]),
	H(5,id="Table"),

	)
	return page

def CommercialProposal():
	page = construct_page(
	H(1,[
		V(2,id="Date"),
		V(2,id="Header"),
	]),
	H(1,[
		V(2,id="SellerInfo"),
		V(2),
	]),
	H(2,id="BuyerInfo"),
	H(1),
	H(1,id="Table"),
	H(1),

	)
	return page

def GovoniSimoBianca():
	page = construct_page(
	H(1,[
		V(1),
		V(1,id="SellerInfo"),
	]),
	H(1,id="BuyerInfo"),
	H(0.5 ,id="Notes"),
	H(2.5,id="Table"),

	)
	return page

def Reliance():
	## Seems like an internal reliance delivery
	page = construct_page(
	H(1),
	H(0.3,id="OrderNo"),
	H(1.5,[
		V(1,id="BuyerInfo"),
		V(1,id="ShipInfo"),
	]),
	H(1,id="Table"),
	H(2),
	

	)
	return page

def Quotation():
	page = construct_page(
	H(1),
	H(0.3,id="Header"),
	H(1.5,[
		V(1),
		V(1,id="InvoiceInfo"),
	]),
	H(0.5,[
		V(1,id="BuyerInfo"),
		V(1,id="ShipInfo"),
	]),
	H(1.3,id="Table"),
	H(0.7,[
		V(7),
		V(3,id="AmountBreakup"),
	]),
	H(2),
	
	)
	return page

def PriceSchedule():
	page = construct_page(
	H(0.3,[
		V(1),
		V(1,id="Header"),
		V(1,id="Date"),
		V(1),
	]),
	H(1.5,id="Table"),
	H(3,id="Terms"),

	)
	return page

def YourQuotation():
	page = construct_page(
	H(1,id="Header"),
	H(2,[
		V(1,id="SellerInfo"),
		V(1,id="Date"),
	]),
	H(0.5,id="BuyerName"),
	H(1,id="InvoiceInfo"),
	H(2,[
		V(1,id="Comments"),
		V(1,id="BuyerInfo"),
	]),
	H(1.5,id="Table"),
	H(1,[
		V(1),
		V(1,id="Amount"),
	]),
	H(1,[
		V(1,id="Terms"),
		V(1),
	]),

	)
	return page

def Mistras():
	page = construct_page(
	H(2,[
		V(1,id="TaxInfo"),
		V(1,id="SellerInfo"),
		V(1,id="Logo"),
	]),
	H(0.5,id="Header"),
	H(0.8,id="SellerInfo"),
	H(0.7,id="InvoiceInfo"),
	H(2,id="Table"),
	H(0.5,id="Terms"),
	
	)
	return page

def QuotationRefteck():
	page = construct_page(
	H(1,[
		V(1,id="SellerInfo"),
		V(1,id="Date"),
	]),
	H(0.5,id="Notes"),
	H(4,id="Table"),
	
	)
	return page

def EmisshieldMaterial():
	page = construct_page(
	H(1,id="Logo"),
	H(0.7,id="SellerName"),
	H(1.5,[
		V(1,id="InvoiceInfo"),
		V(1,id="BuyerName"),
	]),
	H(2,id="Table"),
	H(0.5,id="Total"),
	H(1,id="Terms"),
	
	)
	return page

def SunshineTechnologies():
	page = construct_page(
	H(1,[
		V(1,id="Logo"),
		V(1,id="SellerAddress"),
	]),
	H(7,[
		V(1,[
			H(0.5,id="Date"),
			H(0.7,id="BuyerName"),
			H(1.3,id="Items"),
			H(2,id="Terms"),
			H(0.5,id="Sign"),
		]),
		V(1),
	]),
		
	)
	return page

def YokogawaIndia():	
	page = construct_page(
	H(1.4,[
		V(2,[
			H(0.5,id="SellerName"),
			H(0.7,id="BuyerName"),
		]),
		V(1),
	]),
	H(1,id="Table"),
	H(1,id="Notes"),
	H(1.4),
		
	)
	return page

def SpareList():
	page = construct_page(
	
	H(1,id="Table"),
	H(4),
		
	)
	return page

def FCGPowerIndustries():
	page = construct_page(
	H(1,[
		V(1,id="Logo"),
		V(2),
		V(1,id="Date"),
	]),
	H(3,id="Table"),
	H(0.5,id="Total"),
		
	)
	return page

def NirmalIndustrialControls():
	page = construct_page(
	H(1,id="SellerInfo"),
	H(0.2,id="Date"),
	H(1.8,[
		V(1,id="BuyerInfo"),
		V(1,id="OrderNo"),
	]),

	H(1,id="Table"),
	H(3,id="Terms"),
		
	)
	return page

def QuotationReliance():
	page = construct_page(
	H(0.2,id="Header"),
	H(1,[
		V(1,id="BuyerInfo"),
		V(1,id="InvoiceInfo"),
	]),
	H(2.2,id="Table"),
	H(1.3,id="Notes"),
	H(1,id="Tax"),
		
	)
	return page

def SchweitzerEngineeringLaboratories():
	page = construct_page(
	H(1,id="SellerInfo"),
	H(1.3,[
		V(1,id="BuyerName"),
		V(1,id="DueDate"),
	]),
	H(1.3,id="Table"),
	H(3.4,id="Notes"),		
	)
	return page

def AndersonGreenwoodCrosbySanmar():
	page = construct_page(
	H(1,id="SellerInfo"),
	H(1.3,[
		V(1,id="BuyerInfo"),
		V(1,id="DueDate"),
	]),
	H(1,id="Table"),
	H(1.3,[
		V(1,id="Notes"),
		V(1,id="AmountBreakup"),
	]),
	H(0.8),
	)
	return page

def QuotationSiemens():
	page = construct_page(
	H(1,[
		V(1),
		V(1,id="Orderno"),
		V(1,id="DueDate"),
	]),
	H(2.5,id="Table"),
	H(0.5,id="Amount"),
	H(2.5,id="Tax"),
	
	)
	return page

def AshokEmgineeringWorks():
	page = construct_page(
	H(1,[
		V(1,id="Logo"),
		V(3,id="SellerInfo"),
		V(1),
	]),
	H(1.3,[
		V(1,id="BuyerInfo"),
		V(1,[
			H(0.5,id="TaxInfo"),
			H(1.2,id="DueDate"),
		]),
	]),
	H(2.5,id="Table"),
	H(1.3,id="Notes"),
	
	)
	return page

def KSBLimited():
	page = construct_page(
	H(1,[
		V(1,id="BuyerName"),
		V(1,id="SellerName"),
	]),
	H(0.5,id="Comments"),
	H(4.5,id="Table"),
	)
	return page

def QuotationSweloreEngineering():
	page = construct_page(
	H(1),
	H(0.3,id="Header"),
	H(1,[
		V(1,id="SellerInfo"),
		V(1,id="InvoiceInfo"),
	]),
	H(2,id="Table"),
	H(2,id="Terms"),
	H(1,id="Footer"),
	)
	return page

def QuotationScope():
	page = construct_page(
	H(0.3,id="Header"),
	H(0.3,id="Date"),
	H(1,id="BuyerInfo"),
	H(1.3,id="Table"),
	H(2.5,id="Terms"),
	H(0.6,id="Sign"),
	)
	return page

def AdageAutomation():
	page = construct_page(
	H(1,[
		V(1,id="SellerName"),
		V(1,id="SellerInfo"),
	]),
	H(0.3,id="Header"),
	H(2,id="Table"),
	H(3),
	H(0.5,id="Footer"),
	)
	return page

def QualityToolsBearing():
	page = construct_page(
	H(1,id="SellerInfo"),
	H(0.3,id="Header"),
	H(1.5,[
		V(1,id="BuyerInfo"),
		V(1,id="PaymentType"),
	]),
	H(0.3,id="BuyerName"),
	H(2,id="Table"),
	H(2.5,id="Footer"),
	)
	return page

def HitechMarketing():
	page = construct_page(
	H(1,id="SellerInfo"),
	H(1,[
		V(1,id="BuyerInfo"),
		V(1,id="Orderno"),
		V(1,id="Date"),
	]),
	H(1,id="Table"),
	H(1,id="Terms"),
	H(1),
	)
	return page

def EmersonAutomationsSolutions():
	page = construct_page(
	H(2,[
		V(1,id="BuyerInfo"),
		V(1),
		V(1,id="SellerInfo"),
	]),
	H(1,id="Table"),
	H(2,[
		V(1,id="Terms"),
		V(1),
	]),
	H(0.5,id="Sign"),
	)
	return page

def Leser():
	page = construct_page(
	H(1,id="SellerName"),
	H(5,[
		V(1,[
			H(2.5,id="BuyerInfo"),
			H(1.5,id="Date"),
			H(1,id="OrderNo"),
		]),
		V(1,[
			H(1,id="SellerContact"),
			H(1,id="SellerPOC"),
			H(1,id="BuyerContact"),
		]),
	]),
	H(4,id="Notes"),
	H(1,id="Sign"),
	H(2,[
		V(1,id="SellerAddress"),
		V(1,id="SellerInfo"),
	]),
	)
	return page

def QuotationSAP():
	page = construct_page(
	H(1,id="Header"),
	H(4,id="Table"),
	H(2,id="Notes"),
	H(3),
	)
	return page

def Aerzen():
	page = construct_page(
	H(2,[
		V(1.2,[
			H(1),
			H(2,id="BuyerInfo"),
		]),
		V(1),
		V(1,[
			H(1,id="Logo"),
			H(2,id="SellerInfo"),
		]),
	]),
	
	H(1,id="InvoiceInfo"),
	H(1,id="Account"),
	H(2,id="Table"),
	H(0.5,[
		V(1.5),
		V(1,id="Total"),
	]),
	H(2,id="Footer"),

	)
	return page

def DabirIndustries():
	page = construct_page(
	H(1,id="SellerInfo"),
	H(1,[
		V(1,id="SellerInfo"),
		V(1,id="Date"),
	]),
	H(1,id="Notes"),
	H(3,id="Table"),
	H(3,id="Terms"),
	H(1,id="Sign"),

	)
	return page

def BidHeavyMetalsTubes():
	page = construct_page(
	H(1,id="Header"),
	H(1,[
		V(1,id="BuyerInfo"),
		V(1,id="Date"),
	]),
	H(0.3,id="Notes"),
	H(4,id="Table"),
	H(2,id="Terms"),
	H(1,id="Footer"),

	)
	return page

def OrientEnterprises():
	page = construct_page(
	H(3,[
		V(1,[
			H(1,id="SellerInfo"),
			H(2,[
				V(1,id="BuyerInfo"),
				V(1,id="ShipInfo"),
			]),
		]),
		V(1,[
			H(0.5,id="Header"),
			H(0.5,id="OrderNo"),
			H(2,[
				V(1,[
					H(1,id="BuyerContact"),
					H(1,id="PaymentType"),
				]),
				V(1,[
					H(1,id="BuyerPOC1"),
					H(1,id="BuyerPOC2"),
				]),
			]),
		]),
	]),
	H(2.5,id="Table"),
	H(1.5,id="Terms"),
	)
	return page

def QuotationReliance2():
	page = construct_page(
	H(1,[
		V(1,id="SellerAddress"),
		V(1,id="SellerAddress2"),
		V(1,id="TaxInfo"),
	]),

	H(0.5,id="Header"),
	H(1.2,[
		V(1,id="BuyerInfo"),
		V(1,id="Date"),
	]),
	H(0.5,id="Notes"),
	H(1.2,id="Table"),
	H(1.2,id="Terms"),
	H(0.7,id="Footer"),
	)
	return page

def LamtechSolutions():
	page = construct_page(
	H(1,[
		V(1,id="Date"),
		V(1,id="SellerName"),
	]),
	H(1.5,id="BuyerInfo"),
	H(2.7,id="Notes"),
	H(1.2,id="Sign"),
	H(1.2,id="SellerPOC"),
	H(0.7,id="Footer"),
	)
	return page

def DiatechElectricals():
	page = construct_page(
	H(1,[
		V(8),
		V(2,id="SellerName"),
	]),
	H(2.7,id="Table"),
	H(1.2,id="Sign"),
	H(3.7),
	)
	return page

def Coperion():
	H(1,[
		V(2,id="SellerName"),
		V(2,id="Header"),
	]),
	H(0.7,id="Date"),
	H(2.5,id="Table"),
	H(1.2,id="AmountBreakup"),
	H(3),
	)
	return page

def SprayingSystems():
	page = construct_page(
	H(1,id="SellerName"),
	H(3,[
		V(2,id="BuyerName"),
		V(2,id="InvoiceInfo"),
	]),
	H(1,id="Notes"),
	H(1.5,id="Table"),
	H(3),
	)
	return page

def QuotationBanaraswalaMetalCrafts():
	page = construct_page(
	H(1,id="Header"),
	H(3,[
		V(2,[
			H(1,id="BuyerInfo"),
			H(1.5,id="OrderNo"),
		]),
		V(2,id="SellerPOC"),
	]),
	H(1.5,id="Table"),
	H(1,[
		V(4),
		V(6,id="AmountBreakup"),
	]),
	H(2),
	H(1,id="Footer"),
	)
	return page

def Circor():
	page = construct_page(
	H(1,[
		V(6,id="Logo"),
		V(4,id="SellerInfo"),
	]),
	H(2.5,[
		V(1,id="BuyerInfo"),
		V(1,id="InvoiceInfo"),
	]),
	H(1,id="SellerPOC"),
	H(2,id="Table"),
	H(1,id="AmountBreakup"),
	H(0.5,id="Footer"),
	)
	return page


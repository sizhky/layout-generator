from src.page import *


def UNPPolyvalesConfig():
    page = construct_page(
        H(1, id="SellerName"),
        H(
            3,
            [
                V(
                    1,
                    [
                        H(1.3, id="SellerInfo"),
                        H(1.7, id="BuyerInfo"),
                    ],
                ),
                V(
                    1,
                    [
                        H(1.3, id="DueDate"),
                        H(1.7, id="ShipInfo"),
                    ],
                ),
            ],
        ),
        H(4, id="Table"),
        H(1.5, id="AmountBreakup"),
        H(
            0.5,
            [
                V(6, id="Notes"),
                V(4, id="Sign"),
            ],
        ),
        H(0, id="padding"),
    )
    return page


def BevconZentryConfig():
    page = construct_page(
        H(1, id="InvoiceInfo"),
        H(8, id="Table"),
        H(0, id="padding"),
        H(1, id="Footer"),
    )
    return page


def LakhmichandConfig():
    page = construct_page(
        H(1, id="SellerInfo"),
        H(
            1,
            [
                V(5, id="BuyerInfo"),
                V(5, id="Date"),
            ],
        ),
        H(1, id="Notes"),
        H(1.2, id="ServiceInfo"),
        H(1, id="Table"),
        H(1.8, id="Terms"),
        H(0.5, id="Sign"),
        H(0, id="padding"),
    )
    return page


def RolonSealsConfig():
    page = construct_page(
        H(1, id="SellerInfo"),
        H(
            1.8,
            [
                V(5, id="BuyerInfo"),
                V(5, id="InvoiceInfo"),
            ],
        ),
        H(0.2, id="Notes"),
        H(3.2, id="Table"),
        H(2.8, id="Terms"),
        H(0, id="padding"),
    )
    return page


def RefteckConfig():
    page = construct_page(
        H(
            1,
            [
                V(5, id="SellerName"),
                V(5, id="SellerInfo"),
            ],
        ),
        H(
            1.8,
            [
                V(5, id="BuyerInfo"),
                V(5, id="Total"),
            ],
        ),
        H(1, id="Notes"),
        H(6, id="Table"),
        H(0, id="padding"),
        H(0.5, id="Footer"),
    )
    return page


def NationalAccreditationBoardConfig():
    page = construct_page(
        H(1, id="SellerName"),
        H(
            1.5,
            [
                V(7, id="BuyerInfo"),
                V(5, id="Date"),
            ],
        ),
        H(3.5, id="Notes"),
        H(0.5, id="Sign"),
        H(0, id="padding"),
    )
    return page


def VashiElectricalsConfig():
    page = construct_page(
        H(
            1,
            [
                V(7, id="SellerInfo"),
                V(3, id="OrderNo"),
            ],
        ),
        H(
            0.8,
            [
                V(1, id="BuyerAddress"),
                V(1, id="BuyerContact"),
            ],
        ),
        H(
            1,
            [
                V(1, id="InvoiceInfo"),
                V(1, id="PaymentType"),
            ],
        ),
        H(0.5, id="Comments"),
        H(1.2, id="Table"),
        H(0.8, id="Notes"),
        H(1.2, id="Terms"),
        H(0, id="padding"),
    )
    return page


def ElomaticConfig():
    page = construct_page(
        H(0.5, id="Header"),
        H(
            1,
            [
                V(3, id="BuyerInfo"),
                V(2, id="Header"),
                V(4),
            ],
        ),
        H(5, id="Table"),
        H(0, id="padding"),
    )
    return page


def PayperConfig():
    page = construct_page(
        H(
            1,
            [
                V(1, id="SellerInfo"),
                V(1, id="Header"),
            ],
        ),
        H(
            1.2,
            [
                V(1, id="Date"),
                V(1, id="BuyerInfo"),
            ],
        ),
        H(4.3, id="Table"),
        H(0.5, id="Amount"),
        H(0, id="padding"),
    )
    return page


def SimpexConfig():
    page = construct_page(
        H(
            3,
            [
                V(
                    1,
                    [
                        H(2, id="Logo"),
                        H(0.5, id="BuyerName"),
                        H(1.5, id="BuyerInfo"),
                    ],
                ),
                V(
                    1,
                    [
                        H(2, id="InvoiceInfo"),
                        H(0.5, id="BuyerContact"),
                        H(1.5),
                    ],
                ),
            ],
        ),
        H(1, id="Notes"),
        H(1.5, id="Table"),
        H(
            1.5,
            [
                V(1, id="PaymentType"),
                V(1, id="AmountBreakup"),
            ],
        ),
        H(0, id="padding"),
        H(0.3, id="Footer"),
    )
    return page


def CrystalIndustriesConfig():
    page = construct_page(
        H(
            1,
            [
                V(8),
                V(2, id="Logo"),
            ],
        ),
        H(0.5, id="Header"),
        H(6.5, id="Table"),
        H(0, id="padding"),
    )
    return page


def AalidhraTextoolEngineersConfig():
    page = construct_page(
        H(1, id="SellerInfo"),
        H(
            1,
            [
                V(2, id="BuyerName"),
                V(2, id="DueDate"),
            ],
        ),
        H(7.5, id="Table"),
        H(0, id="padding"),
    )
    return page


def EvergreenConfig():
    page = construct_page(
        H(1, id="SellerName"),
        H(
            0.4,
            [
                V(2, id="Date"),
                V(2, id="DueDate"),
            ],
        ),
        H(
            1.6,
            [
                V(2, id="SellerInfo"),
                V(2, id="BuyerInfo"),
            ],
        ),
        H(5, id="Table"),
        H(0, id="padding"),
    )
    return page


def CommercialProposalConfig():
    page = construct_page(
        H(
            1,
            [
                V(2, id="Date"),
                V(2, id="Header"),
            ],
        ),
        H(
            1,
            [
                V(2, id="SellerInfo"),
                V(2),
            ],
        ),
        H(2, id="BuyerInfo"),
        H(1),
        H(1, id="Table"),
        H(1, id="padding"),
    )
    return page


def GovoniSimoBiancaConfig():
    page = construct_page(
        H(
            1,
            [
                V(1),
                V(1, id="SellerInfo"),
            ],
        ),
        H(1, id="BuyerInfo"),
        H(0.5, id="Notes"),
        H(2.5, id="Table"),
        H(0, id="padding"),
    )
    return page


def RelianceConfig():
    ## Seems like an internal reliance delivery
    page = construct_page(
        H(1),
        H(0.3, id="OrderNo"),
        H(
            1.5,
            [
                V(1, id="BuyerInfo"),
                V(1, id="ShipInfo"),
            ],
        ),
        H(1, id="Table"),
        H(2, id="padding"),
    )
    return page


def QuotationConfig():
    page = construct_page(
        H(1),
        H(0.3, id="Header"),
        H(
            1.5,
            [
                V(1),
                V(1, id="InvoiceInfo"),
            ],
        ),
        H(
            0.5,
            [
                V(1, id="BuyerInfo"),
                V(1, id="ShipInfo"),
            ],
        ),
        H(1.3, id="Table"),
        H(
            0.7,
            [
                V(7),
                V(3, id="AmountBreakup"),
            ],
        ),
        H(2, id="padding"),
    )
    return page


def PriceScheduleConfig():
    page = construct_page(
        H(
            0.3,
            [
                V(1),
                V(1, id="Header"),
                V(1, id="Date"),
                V(1),
            ],
        ),
        H(1.5, id="Table"),
        H(3, id="Terms"),
        H(0, id="padding"),
    )
    return page


def YourQuotationConfig():
    page = construct_page(
        H(1, id="Header"),
        H(
            2,
            [
                V(1, id="SellerInfo"),
                V(1, id="Date"),
            ],
        ),
        H(0.5, id="BuyerName"),
        H(1, id="InvoiceInfo"),
        H(
            2,
            [
                V(1, id="Comments"),
                V(1, id="BuyerInfo"),
            ],
        ),
        H(1.5, id="Table"),
        H(
            1,
            [
                V(1),
                V(1, id="Amount"),
            ],
        ),
        H(
            1,
            [
                V(1, id="Terms"),
                V(1),
            ],
        ),
        H(0, id="padding"),
    )
    return page


def MistrasConfig():
    page = construct_page(
        H(
            2,
            [
                V(1, id="TaxInfo"),
                V(1, id="SellerInfo"),
                V(1, id="Logo"),
            ],
        ),
        H(0.5, id="Header"),
        H(0.8, id="SellerInfo"),
        H(0.7, id="InvoiceInfo"),
        H(2, id="Table"),
        H(0.5, id="Terms"),
        H(0, id="padding"),
    )
    return page


def QuotationRefteckConfig():
    page = construct_page(
        H(
            1,
            [
                V(1, id="SellerInfo"),
                V(1, id="Date"),
            ],
        ),
        H(0.5, id="Notes"),
        H(4, id="Table"),
        H(0, id="padding"),
    )
    return page


def EmisshieldMaterialConfig():
    page = construct_page(
        H(1, id="Logo"),
        H(0.7, id="SellerName"),
        H(
            1.5,
            [
                V(1, id="InvoiceInfo"),
                V(1, id="BuyerName"),
            ],
        ),
        H(2, id="Table"),
        H(0.5, id="Total"),
        H(1, id="Terms"),
        H(0, id="padding"),
    )
    return page


def SunshineTechnologiesConfig():
    page = construct_page(
        H(
            1,
            [
                V(1, id="Logo"),
                V(1, id="SellerAddress"),
            ],
        ),
        H(
            7,
            [
                V(
                    1,
                    [
                        H(0.5, id="Date"),
                        H(0.7, id="BuyerName"),
                        H(1.3, id="Items"),
                        H(2, id="Terms"),
                        H(0.5, id="Sign"),
                    ],
                ),
                V(1),
            ],
        ),
        H(0, id="padding"),
    )
    return page


def YokogawaIndiaConfig():
    page = construct_page(
        H(
            1.4,
            [
                V(
                    2,
                    [
                        H(0.5, id="SellerName"),
                        H(0.7, id="BuyerName"),
                    ],
                ),
                V(1),
            ],
        ),
        H(1, id="Table"),
        H(1, id="Notes"),
        H(1.4, id="padding"),
    )
    return page


def SpareListConfig():
    page = construct_page(
        H(1, id="Table"),
        H(4, id="padding"),
    )
    return page


def FCGPowerIndustriesConfig():
    page = construct_page(
        H(
            1,
            [
                V(1, id="Logo"),
                V(2),
                V(1, id="Date"),
            ],
        ),
        H(3, id="Table"),
        H(0.5, id="Total"),
        H(0, id="padding"),
    )
    return page


def NirmalIndustrialControlsConfig():
    page = construct_page(
        H(1, id="SellerInfo"),
        H(0.2, id="Date"),
        H(
            1.8,
            [
                V(1, id="BuyerInfo"),
                V(1, id="OrderNo"),
            ],
        ),
        H(1, id="Table"),
        H(3, id="Terms"),
        H(0, id="padding"),
    )
    return page


def QuotationRelianceConfig():
    page = construct_page(
        H(0.2, id="Header"),
        H(
            1,
            [
                V(1, id="BuyerInfo"),
                V(1, id="InvoiceInfo"),
            ],
        ),
        H(2.2, id="Table"),
        H(1.3, id="Notes"),
        H(1, id="Tax"),
        H(0, id="padding"),
    )
    return page


def SchweitzerEngineeringLaboratoriesConfig():
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


def AndersonGreenwoodCrosbySanmarConfig():
    page = construct_page(
        H(1, id="SellerInfo"),
        H(
            1.3,
            [
                V(1, id="BuyerInfo"),
                V(1, id="DueDate"),
            ],
        ),
        H(1, id="Table"),
        H(
            1.3,
            [
                V(1, id="Notes"),
                V(1, id="AmountBreakup"),
            ],
        ),
        H(0.8, id="padding"),
    )
    return page


def QuotationSiemensConfig():
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


def AshokEmgineeringWorksConfig():
    page = construct_page(
        H(
            1,
            [
                V(1, id="Logo"),
                V(3, id="SellerInfo"),
                V(1),
            ],
        ),
        H(
            1.3,
            [
                V(1, id="BuyerInfo"),
                V(
                    1,
                    [
                        H(0.5, id="TaxInfo"),
                        H(1.2, id="DueDate"),
                    ],
                ),
            ],
        ),
        H(2.5, id="Table"),
        H(1.3, id="Notes"),
        H(0, id="padding"),
    )
    return page


def KSBLimitedConfig():
    page = construct_page(
        H(
            1,
            [
                V(1, id="BuyerName"),
                V(1, id="SellerName"),
            ],
        ),
        H(0.5, id="Comments"),
        H(4.5, id="Table"),
    )
    return page


def QuotationSweloreEngineeringConfig():
    page = construct_page(
        H(1),
        H(0.3, id="Header"),
        H(
            1,
            [
                V(1, id="SellerInfo"),
                V(1, id="InvoiceInfo"),
            ],
        ),
        H(2, id="Table"),
        H(2, id="Terms"),
        H(0, id="padding"),
        H(1, id="Footer"),
    )
    return page


def QuotationScopeConfig():
    page = construct_page(
        H(0.3, id="Header"),
        H(0.3, id="Date"),
        H(1, id="BuyerInfo"),
        H(1.3, id="Table"),
        H(2.5, id="Terms"),
        H(0.6, id="Sign"),
    )
    return page


def AdageAutomationConfig():
    page = construct_page(
        H(
            1,
            [
                V(1, id="SellerName"),
                V(1, id="SellerInfo"),
            ],
        ),
        H(0.3, id="Header"),
        H(2, id="Table"),
        H(3, id="padding"),
        H(0.5, id="Footer"),
    )
    return page


def QualityToolsBearingConfig():
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


def HitechMarketingConfig():
    page = construct_page(
        H(1, id="SellerInfo"),
        H(
            1,
            [
                V(1, id="BuyerInfo"),
                V(1, id="Orderno"),
                V(1, id="Date"),
            ],
        ),
        H(1, id="Table"),
        H(1, id="Terms"),
        H(1, id="padding"),
    )
    return page


def EmersonAutomationsSolutionsConfig():
    page = construct_page(
        H(
            2,
            [
                V(1, id="BuyerInfo"),
                V(1),
                V(1, id="SellerInfo"),
            ],
        ),
        H(1, id="Table"),
        H(
            2,
            [
                V(1, id="Terms"),
                V(1),
            ],
        ),
        H(0.5, id="Sign"),
        H(0, id="padding"),
    )
    return page


def LeserConfig():
    page = construct_page(
        H(1, id="SellerName"),
        H(
            5,
            [
                V(
                    1,
                    [
                        H(2.5, id="BuyerInfo"),
                        H(1.5, id="Date"),
                        H(1, id="OrderNo"),
                    ],
                ),
                V(
                    1,
                    [
                        H(1, id="SellerContact"),
                        H(1, id="SellerPOC"),
                        H(1, id="BuyerContact"),
                    ],
                ),
            ],
        ),
        H(4, id="Notes"),
        H(1, id="Sign"),
        H(
            2,
            [
                V(1, id="SellerAddress"),
                V(1, id="SellerInfo"),
            ],
        ),
        H(0, id="padding"),
    )
    return page


def QuotationSAPConfig():
    page = construct_page(
        H(1, id="Header"),
        H(4, id="Table"),
        H(2, id="Notes"),
        H(3, id="padding"),
    )
    return page


def AerzenConfig():
    page = construct_page(
        H(
            2,
            [
                V(
                    1.2,
                    [
                        H(1),
                        H(2, id="BuyerInfo"),
                    ],
                ),
                V(1),
                V(
                    1,
                    [
                        H(1, id="Logo"),
                        H(2, id="SellerInfo"),
                    ],
                ),
            ],
        ),
        H(1, id="InvoiceInfo"),
        H(1, id="Account"),
        H(2, id="Table"),
        H(
            0.5,
            [
                V(1.5),
                V(1, id="Total"),
            ],
        ),
        H(0, id="padding"),
        H(2, id="Footer"),
    )
    return page


def DabirIndustriesConfig():
    page = construct_page(
        H(1, id="SellerInfo"),
        H(
            1,
            [
                V(1, id="SellerInfo"),
                V(1, id="Date"),
            ],
        ),
        H(1, id="Notes"),
        H(3, id="Table"),
        H(3, id="Terms"),
        H(1, id="Sign"),
    )
    return page


def BidHeavyMetalsTubesConfig():
    page = construct_page(
        H(1, id="Header"),
        H(
            1,
            [
                V(1, id="BuyerInfo"),
                V(1, id="Date"),
            ],
        ),
        H(0.3, id="Notes"),
        H(4, id="Table"),
        H(2, id="Terms"),
        H(1, id="Footer"),
        H(0, id="padding"),
    )
    return page


def OrientEnterprisesConfig():
    page = construct_page(
        H(
            3,
            [
                V(
                    1,
                    [
                        H(1, id="SellerInfo"),
                        H(
                            2,
                            [
                                V(1, id="BuyerInfo"),
                                V(1, id="ShipInfo"),
                            ],
                        ),
                    ],
                ),
                V(
                    1,
                    [
                        H(0.5, id="Header"),
                        H(0.5, id="OrderNo"),
                        H(
                            2,
                            [
                                V(
                                    1,
                                    [
                                        H(1, id="BuyerContact"),
                                        H(1, id="PaymentType"),
                                    ],
                                ),
                                V(
                                    1,
                                    [
                                        H(1, id="BuyerPOC1"),
                                        H(1, id="BuyerPOC2"),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
        H(2.5, id="Table"),
        H(1.5, id="Terms"),
        H(0, id="padding"),
    )
    return page


def QuotationReliance2Config():
    page = construct_page(
        H(
            1,
            [
                V(1, id="SellerAddress"),
                V(1, id="SellerAddress2"),
                V(1, id="TaxInfo"),
            ],
        ),
        H(0.5, id="Header"),
        H(
            1.2,
            [
                V(1, id="BuyerInfo"),
                V(1, id="Date"),
            ],
        ),
        H(0.5, id="Notes"),
        H(1.2, id="Table"),
        H(1.2, id="Terms"),
        H(0, id="padding"),
        H(0.7, id="Footer"),
    )
    return page


def LamtechSolutionsConfig():
    page = construct_page(
        H(
            1,
            [
                V(1, id="Date"),
                V(1, id="SellerName"),
            ],
        ),
        H(1.5, id="BuyerInfo"),
        H(2.7, id="Notes"),
        H(1.2, id="Sign"),
        H(1.2, id="SellerPOC"),
        H(0, id="padding"),
        H(0.7, id="Footer"),
    )
    return page


def DiatechElectricalsConfig():
    page = construct_page(
        H(
            1,
            [
                V(8),
                V(2, id="SellerName"),
            ],
        ),
        H(2.7, id="Table"),
        H(1.2, id="Sign"),
        H(3.7, id="padding"),
    )
    return page


def CoperionConfig():
    page = construct_page(
        H(
            1,
            [
                V(2, id="SellerName"),
                V(2, id="Header"),
            ],
        ),
        H(0.7, id="Date"),
        H(2.5, id="Table"),
        H(1.2, id="AmountBreakup"),
        H(3, id="padding"),
    )
    return page


def SprayingSystemsConfig():
    page = construct_page(
        H(1, id="SellerName"),
        H(
            3,
            [
                V(2, id="BuyerName"),
                V(2, id="InvoiceInfo"),
            ],
        ),
        H(1, id="Notes"),
        H(1.5, id="Table"),
        H(3, id="padding"),
    )
    return page


def QuotationBanaraswalaMetalCraftsConfig():
    page = construct_page(
        H(1, id="Header"),
        H(
            3,
            [
                V(
                    2,
                    [
                        H(1, id="BuyerInfo"),
                        H(1.5, id="OrderNo"),
                    ],
                ),
                V(2, id="SellerPOC"),
            ],
        ),
        H(1.5, id="Table"),
        H(
            1,
            [
                V(4),
                V(6, id="AmountBreakup"),
            ],
        ),
        H(2, id="padding"),
        H(1, id="Footer"),
    )
    return page


def CircorConfig():
    page = construct_page(
        H(
            1,
            [
                V(6, id="Logo"),
                V(4, id="SellerInfo"),
            ],
        ),
        H(
            2.5,
            [
                V(1, id="BuyerInfo"),
                V(1, id="InvoiceInfo"),
            ],
        ),
        H(1, id="SellerPOC"),
        H(2, id="Table"),
        H(1, id="AmountBreakup"),
        H(0.5, id="Footer"),
        H(0, id="padding"),
    )
    return page

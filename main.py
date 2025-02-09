from best_buy_scraper import searchThroughBestBuy
from newegg_scraper import searchThroughNewegg
from micro_center_scraper import searchThroughMicroCenter

rtx_5090_best_buy_page = "https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&browsedCategory=abcat0507002&id=pcat17071&iht=n&ks=960&list=y&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~Nvidia%20GeForce%20RTX%205090&sc=Global&st=categoryid%24abcat0507002&type=page&usc=All%20Categories"
rtx_5090_page_newegg = "https://www.newegg.com/p/pl?N=100007709%20601469153"
rtx_5090_page_microcenter = "https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&N=4294966937+4294802166+4294802144&myStore=true"

bestbuyCSV = "bestbuydata.csv"
microcenterCSV = "microcenterdata.csv"
neweggCSV = "neweggdata.csv"

# Loop indefinitely, continuously gathering data
def main():
    try:
        while True:
            searchThroughBestBuy(rtx_5090_best_buy_page, bestbuyCSV)
            searchThroughMicroCenter(rtx_5090_page_microcenter, microcenterCSV)
            searchThroughNewegg(rtx_5090_page_newegg, neweggCSV)
    # Rerun event loop in the event of a critical failure
    except (Exception):
        main()

if __name__ == "__main__":
    main()
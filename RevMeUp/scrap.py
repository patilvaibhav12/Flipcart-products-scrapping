from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as uReq

#function to scrap data
def scrap(url):
    my_url = url
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    #creating page Soup
    page_soup = Soup(page_html, 'html.parser')

    #getting data of products on webpage
    containers = page_soup.findAll("div", {'class':'_1xHGtK _373qXS'})

    #getting product details one by one
    for container in containers:
        Name_Container = container.findAll("div",{"class":"_2WkVRV"})
        product_name = Name_Container[0].text.strip()

        Oprice_container = container.findAll("div",{"class":"_30jeq3"})
        Oprice = Oprice_container[0].text.strip()

        price = container.findAll("div",{"class":"_3I9_wc"})
        Orprice = price[0].text.strip()

        link = container.find('a')['href']

        trim_oprice = ''.join(Oprice.split(","))
        rm_rupee = trim_oprice.split("₹")
        final_price = "Rs." + rm_rupee[1]

        trim_orprice = ''.join(Orprice.split(","))
        rm_orupee = trim_orprice.split("₹")
        final_orprice = "Rs." + rm_orupee[1]

        final_link = "https://www.flipkart.com" + link

        #writting product details to csv file
        f.write(product_name + "," + final_price + ","+ final_orprice + "," + final_link + "\n")
        


if __name__ == "__main__":
    # number of pages of products to scrap
    pg_no = 3

    #creating csv file
    filename = "products.csv"
    f = open(filename, "w")
    headers = "Product_name,offer_price,Original_price,Product_URL\n"
    f.write(headers)

    #creating different urls to scrap products
    for i in range(1,pg_no+1):
        url = "https://www.flipkart.com/watches/wrist-watches/pr?sid=r18%2Cf13&offer=nb%3Amp%3A0419071722%2Cnb%3Amp%3A049d5f6c22%2Cnb%3Amp%3A04e7688022&hpid=5c5NGdP5xRYRUNRb-rb8m6p7_Hsxr70nj65vMAAFKlc%3D&fm=neo%2Fmerchandising&iid=M_c6d41647-c7a3-476c-9dd6-50ebca39e58b_4.A5N6E83IL3KE&ssid=gwapcezosw0000001622341865077&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_2_4.dealCard.OMU_A5N6E83IL3KE_3&otracker1=hp_omu_SECTIONED_manualRanking_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_2_NA_view-all_3&cid=A5N6E83IL3KE&page=" + str(i)
        scrap(url)
    f.close()



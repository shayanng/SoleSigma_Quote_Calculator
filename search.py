import time


def search_ads_quote(client_budget: float, addon: bool = True):
    if client_budget <= 5000 and addon is True:
        print("The Final Clint Quote: ", (500 + 150))
    elif client_budget <= 5000 and addon is False:
        print("The Final Clint Quote: ", 500)
    elif client_budget >= 5000 and addon is True:
        main_service = 500 + (client_budget - 5000) * 0.07
        print(main_service)
        if 5000 < client_budget < 10000:
            addon_service = 200
        elif 10000 < client_budget < 15000:
            addon_service = 250
        elif 15000 < client_budget < 20000:
            addon_service = 300
        elif 20000 < client_budget < 30000:
            addon_service = 400
        elif 30000 < client_budget < 40000:
            addon_service = 500
        elif 40000 < client_budget < 50000:
            addon_service = 600
        elif 50000 < client_budget < 60000:
            addon_service = 700
        elif 60000 < client_budget < 70000:
            addon_service = 800
        elif 70000 < client_budget < 80000:
            addon_service = 900
        elif 80000 < client_budget < 100000:
            addon_service = 1000
        elif client_budget > 100000:
            addon_service = 1500
        print("Addon Service Fee: ", addon_service)
        # addon_service = 150 + (client_budget-5000) * 0.07
        print("The Final Clint Quote: ", (main_service + addon_service))
    elif client_budget >= 5000 and addon is False:
        main_service = 500 + (client_budget - 5000) * 0.07
        print("The Final Clint Quote: ", main_service)


# print(search_ads_quote(5000, False))
# search_ads_quote(78000, True)
# print("########################")
# search_ads_quote(3000, True)
# print("########################")
# search_ads_quote(30000, False)
# print("########################")
# search_ads_quote(3000, False)


def quote_engine():
    input_budget = float(input("Type the budget of the client for the search advertising service: "))
    # print(type(input_budget))
    input_addon = input("Add Microsoft Advertising Addon? Answer with (yes|no): ")
    if input_addon == "no":
        input_addon = False
    elif input_addon == "yes":
        input_addon = True
    print("the quote is being calculated")
    time.sleep(1.5)
    search_ads_quote(input_budget, input_addon)


if __name__ == '__main__':
    quote_engine()

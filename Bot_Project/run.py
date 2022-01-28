
import imp
from locale import currency
from booking.booking import Booking


with Booking(teardown = False) as bot:
    bot.land_first_page()
    # bot.change_language(lang='en-gb')
    # bot.change_currency(currency='PKR')
    bot.search_place(place='Islamabad')
    bot.select_dates(checkin="2022-01-29", checkout="2022-01-30")
    bot.select_adults(3)
    bot.click_search()
    bot.apply_filter()
    bot.refresh()
    bot.show_results()
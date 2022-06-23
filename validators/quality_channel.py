from common.symbols import *
from common.icon_finder import get_crypto_icon

def quality_channel_validator(message):
    try:
        msg = message.split("\n\n")
        if msg[0] == '✳ New FREE signal':
            position_data = msg[1].split(' ')
            position = position_data[1]
            pairs = position_data[2]
            exchange = position_data[4]

            time = msg[2].split("\n")[1]

            order_data = msg[3].split("\n")
            enter = order_data[0].split(":")[1]
            tp = f'{order_data[2].split(":")[1]}\n      {order_data[3].split(":")[1]}\n      {order_data[4].split(":")[1]}'
            sl = order_data[5].split(":")[1]

            if position == 'Buy':
                logo = f"{green} **NEW BUY SIGNAL** {green} \n\n"
            else:
                logo = f"{red} **NEW SELL SIGNAL** {red} \n\n"

            raw_bid_name = pairs.split('/')[0].replace("#","")
            # logo_link = f'https://cryptoicons.org/api/color/{raw_bid_name}/200'
            logo_link = ""
            finded_logo = get_crypto_icon(raw_bid_name)

            if finded_logo:
                logo_link = finded_logo

            final_message = f"{logo}{gem} **Position**: {position} \n{money} **Pairs**: {pairs} \n" \
                            f"{dollar} **Exchange**: {exchange} \n" \
                            f"{rocket} **Enter**: `{enter}` \n{dart} **TP**: `{tp}` \n{no_entry} **Sl**: `{sl}` " \
                            f"\n\n\n{time} \n #quality_channel \n " \
                            f"@ravand_palantir \n\n{logo_link}".replace("'", "")

            return final_message
        return None
    except Exception as e:
        print(e)
        return None
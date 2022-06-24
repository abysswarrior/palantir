from common.symbols import *
from common.icon_finder import get_crypto_icon
from datetime import datetime
import re

def alpha_trade_channel_validator(message):
    try:
        msg = message.split("\n\n")

        position_data = msg[0].split('\n')
        pairs = position_data[0].replace('/', '/#')
        exchange = "#" + position_data[1].split(":")[1].upper().strip()
        position = position_data[2].split(":")[1].strip()

        time = datetime.utcnow().strftime("%d-%b-%Y %H:%M:%S UTC")

        order_data = msg[1].split('\n')
        enter = ""
        for data in order_data:
            try:
                if data != order_data[len(order_data) - 1]:
                    enter = enter + data.split(")")[1].strip() + "\n        "
                else:
                    enter = enter + data.split(")")[1].strip()
            except:
                continue

        tp_data = msg[2].split('\n')
        tp = ""
        for data in tp_data:
            try:
                if data != tp_data[len(tp_data) - 1]:
                    tp = tp + data.split(")")[1].strip() + "\n      "
                else:
                    tp = tp + data.split(")")[1].strip()
            except:
                continue

        sl_data = msg[3].split('\n')
        sl = ""
        for data in sl_data:
            try:
                if data != sl_data[len(sl_data) - 1]:
                    sl = sl + data.split(")")[1].strip() + "\n      "
                else:
                    sl = sl + data.split(")")[1].strip()
            except:
                continue

        if sl == "":
            sl = "NOT DEFINE"

        if re.search('long', position, re.IGNORECASE):
            logo = f"{green} **NEW BUY SIGNAL** {green} \n\n"
        else:
            logo = f"{red} **NEW SELL SIGNAL** {red} \n\n"

        raw_bid_name = pairs.split('/')[0].replace("#", "")
        # logo_link = f'https://cryptoicons.org/api/color/{raw_bid_name}/200'
        logo_link = ""
        finded_logo = get_crypto_icon(raw_bid_name)

        if finded_logo:
            logo_link = finded_logo

        final_message = f"{logo}{gem} **Position**: {position} \n{money} **Pairs**: {pairs} \n" \
                        f"{dollar} **Exchange**: {exchange} \n" \
                        f"{rocket} **Enter**:  `{enter}` \n{dart} **TP**:  `{tp}` \n{no_entry} **Sl**:  `{sl}` " \
                        f"\n\n\n{clock}{time} \n " \
                        f"@ravand_palantir \n\n{logo_link}".replace("'", "")

        return final_message
    except Exception as e:
        print(e)
        return None
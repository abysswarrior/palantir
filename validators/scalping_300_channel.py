from common.symbols import *
from common.icon_finder import get_crypto_icon
from datetime import datetime
import re

def scalipng_300_channel_validator(message):
    try:
        msg = message.split("\n\n")
        if msg[0] == '꧁༺ 𝓢𝓒𝓐𝓛𝓟𝓘𝓝𝓖 300 ༻꧂':
            position_data = msg[1].split('\n')
            position = f'{position_data[1].split(":")[1].strip()} {position_data[2].split(":")[1].strip()}'
            pairs = f"#{position_data[0].split('...')[1].replace('USDT', '').strip()}/USDT"
            exchange = "UNKNOWN"

            # enter_data = position_data[3].split(':')[1].replace('★', '').strip()
            # enter = f"{enter_data.split('-')[0]} - {enter_data.split('-')[1]}"
            enter = position_data[3].split(':')[1].replace('★', '').strip()

            time = datetime.utcnow().strftime("%d-%b-%Y %H:%M:%S UTC")

            tp_data = msg[3].split('\n')
            tp = f"{tp_data[5].split('-')[1].strip()}\n      {tp_data[6].split('-')[1].strip()}\n      {tp_data[7].split('-')[1].strip()}"
            sl = msg[2].split(':')[1].replace('🔥', '').strip()

            if re.search('long', position, re.IGNORECASE):
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
                            f"\n\n\n{clock} {time} \n " \
                            f"@ravand_palantir \n\n{logo_link}".replace("'", "")

            return final_message
        return None
    except Exception as e:
        print(e)
        return None
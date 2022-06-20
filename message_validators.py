def quality_channel_validator(message):
    try:
        msg = message.split("\n\n")
        if msg[0] == '✳ New FREE signal':
            position_data = msg[1].split(' ')
            position = position_data[1]
            pairs = position_data[2]
            exchange = position_data[3]

            time = msg[2].split("\n")[1]

            order_data = msg[3].split("\n")
            enter = order_data[0].split(":")[1]
            tp = f'{order_data[2].split(":")[1]}, {order_data[3].split(":")[1]}, {order_data[4].split(":")[1]}'
            sl = order_data[5].split(":")[1]

            final_message = f"Position: {position} '\n\n' Pairs: {pairs} '\n\n' Exchange: {exchange} '\n\n' " \
                            f"Time: {time}  '\n\n'" \
                            f"Enter: {enter} '\n\n' TP: {tp} '\n\n' Sl: {sl}".replace("'", "")
            return final_message, True
    except Exception as e:
        print(e)
        return None, False
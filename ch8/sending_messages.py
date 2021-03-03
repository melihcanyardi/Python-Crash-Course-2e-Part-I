messages = ['Hello!', 'Hi!', 'How are you?', 'Bye!']
sent_messages = []


def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


send_messages(messages, sent_messages)

print(messages)
print(sent_messages)

from pandas import DataFrame


with open('../data/Chats.txt', 'r') as file:
    chats: str = file.read()

df: DataFrame = DataFrame(columns=['sender', 'msg'])

# divide single string into multiple lines
chats: list = chats.split('\n')
chats = chats[1:]

# remove unnecessary data
for i in range(len(chats)):
    chats[i] = ' '.join(chats[i].split(' ')[4:])

# insert all the chats into the DataFrame
for chat in chats:
    sender: str = chat.split(':')[0]
    msg: str = ':'.join(chat.split(':')[1:])
    msg = msg[1:]
    
    # remove names from the data
    if sender == 'Shabd Saran': sender = 'Me'
    else: sender = 'Other'
    
    df = df.append({'sender': sender, 'msg': msg}, ignore_index=True)

# removing <Media omitted> lines
df.drop(df[df['msg'] == '<Media omitted>'].index, inplace=True)
df.reset_index(drop=True, inplace=True)  # reset index values

# grouping the conversations
drop_indices: list = []
for i in range(len(df) - 1):
    curr_sender: str = df['sender'].iloc[i]
    curr_index: int = i
    sentence: str = df['msg'].iloc[i]
    while i < len(df) - 1 and curr_sender == df['sender'].iloc[i+1]:
        sentence += '. ' + df['msg'].iloc[i+1]
        drop_indices.append(1 + curr_index)
        i += 1
    df['msg'].iloc[curr_index] = sentence
    i += 1
df.drop(index=drop_indices, axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)  # reset index values

# remove pairs with no replies
drop_indices: list = []
for i in range(len(df) - 1):
    if '' in [df['msg'].iloc[i], df['msg'].iloc[i+1]]:
        drop_indices.append(i)
        drop_indices.append(i+1)
    i += 2
df.drop(index=drop_indices, axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)  # reset index values

# storing data into train.from & trian.to
with open('train.from', 'a') as train_from:
    with open('train.to', 'a') as train_to:
        for i in range(len(df)):
            if 'Me' == df['sender'].iloc[i]:
                train_from.write(df['msg'].iloc[i] + '\n')
            else:
                train_to.write(df['msg'].iloc[i] + '\n')

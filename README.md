# Simple Chatbot
Simple Chatbot using Deep Learning with nmt-chatbot.

## About the data

Data was collected from WhatsApp personal chats. All the data used for this bot is personal data and was not obtained illegally.
WhatsApp chats can be downloaded from the app itself, go to any chat, select Settings -> More -> Export chat.

## nmt-chatbot

It's quite a famous repository, link [here](https://github.com/daniel-kukiela/nmt-chatbot). All the required deep learning algorithms were already written inside the repository. It just required two files `trains.from` and `train.to`.
Both these files had to be prepared from the collected data. Preprocessing code can be found [here](/src/preprocessing.py).
